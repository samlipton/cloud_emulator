import os

import boto3


def _client(service: str):
    return boto3.client(
        service,
        region_name=os.environ["AWS_REGION"],
        endpoint_url=os.environ["LOCALSTACK_ENDPOINT"],
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )


s3 = _client("s3")
dynamodb = _client("dynamodb")

S3_BUCKET = os.environ["S3_BUCKET"]
DYNAMODB_TABLE = os.environ["DYNAMODB_TABLE"]
