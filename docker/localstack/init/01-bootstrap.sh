#!/usr/bin/env bash
set -euo pipefail

echo "[bootstrap] creating S3 bucket: ${S3_BUCKET}"
awslocal s3 mb "s3://${S3_BUCKET}"

echo "[bootstrap] creating SQS queue: ${SQS_QUEUE_NAME}"
awslocal sqs create-queue --queue-name "${SQS_QUEUE_NAME}"

QUEUE_ARN=$(awslocal sqs get-queue-attributes \
  --queue-url "http://sqs.${AWS_REGION}.localhost.localstack.cloud:4566/000000000000/${SQS_QUEUE_NAME}" \
  --attribute-names QueueArn --query 'Attributes.QueueArn' --output text)

echo "[bootstrap] creating DynamoDB table: ${DYNAMODB_TABLE}"
awslocal dynamodb create-table \
  --table-name "${DYNAMODB_TABLE}" \
  --attribute-definitions AttributeName=file_id,AttributeType=S \
  --key-schema AttributeName=file_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

echo "[bootstrap] wiring S3 -> SQS event notifications"
awslocal s3api put-bucket-notification-configuration \
  --bucket "${S3_BUCKET}" \
  --notification-configuration '{
    "QueueConfigurations": [
      {
        "QueueArn": "'"${QUEUE_ARN}"'",
        "Events": ["s3:ObjectCreated:*"]
      }
    ]
  }'

echo "[bootstrap] done"
