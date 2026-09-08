import uuid
from datetime import datetime, timezone

from botocore.exceptions import ClientError
from fastapi import FastAPI, HTTPException, UploadFile

from app.aws import DYNAMODB_TABLE, S3_BUCKET, dynamodb, s3

app = FastAPI(title="Cloud Emulator API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
async def upload(file: UploadFile):
    file_id = str(uuid.uuid4())
    key = f"{file_id}/{file.filename}"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=await file.read(),
        ContentType=file.content_type or "application/octet-stream",
    )

    return {
        "file_id": file_id,
        "bucket": S3_BUCKET,
        "key": key,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/files/{file_id}")
def get_file(file_id: str):
    try:
        item = dynamodb.get_item(
            TableName=DYNAMODB_TABLE, Key={"file_id": {"S": file_id}}
        ).get("Item")
    except ClientError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Not processed yet or file_id does not exist",
        )

    return {
        "file_id": item["file_id"]["S"],
        "bucket": item["bucket"]["S"],
        "key": item["key"]["S"],
        "size": int(item["size"]["N"]),
        "content_type": item["content_type"]["S"],
        "uploaded_at": item["uploaded_at"]["S"],
        "processed_at": item["processed_at"]["S"],
    }
