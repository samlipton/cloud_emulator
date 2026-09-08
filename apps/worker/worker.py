import json
import logging
import sys
from datetime import datetime, timezone

from aws import DYNAMODB_TABLE, SQS_QUEUE_NAME, dynamodb, s3, sqs

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format=json.dumps(
        {"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}
    ),
)
log = logging.getLogger("worker")


def queue_url() -> str:
    return sqs.get_queue_url(QueueName=SQS_QUEUE_NAME)["QueueUrl"]


def process_s3_record(record: dict) -> None:
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]
    file_id = key.split("/", 1)[0]

    head = s3.head_object(Bucket=bucket, Key=key)

    dynamodb.put_item(
        TableName=DYNAMODB_TABLE,
        Item={
            "file_id": {"S": file_id},
            "bucket": {"S": bucket},
            "key": {"S": key},
            "size": {"N": str(head["ContentLength"])},
            "content_type": {"S": head.get("ContentType", "application/octet-stream")},
            "uploaded_at": {"S": record["eventTime"]},
            "processed_at": {"S": datetime.now(timezone.utc).isoformat()},
        },
    )
    log.info("processed file_id=%s bucket=%s key=%s", file_id, bucket, key)


def handle_message(message: dict) -> None:
    body = json.loads(message["Body"])
    for record in body.get("Records", []):
        process_s3_record(record)


def main() -> None:
    url = queue_url()
    log.info("worker started, polling queue_url=%s", url)

    while True:
        response = sqs.receive_message(
            QueueUrl=url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
        )

        for message in response.get("Messages", []):
            try:
                handle_message(message)
            except Exception:
                log.exception(
                    "failed to process message_id=%s", message.get("MessageId")
                )
                continue

            sqs.delete_message(
                QueueUrl=url, ReceiptHandle=message["ReceiptHandle"]
            )


if __name__ == "__main__":
    main()
