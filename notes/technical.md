# Technical Notes

Here is an outlook into some technical elements of cloud computing

## External Services

Common external services to containerize in Docker (regardless of what the app is written in):

| Category         | Examples                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Database         | PostgreSQL, MySQL, MongoDB                                                                                                     |
| Cache            | Redis, Memcached                                                                                                               |
| Message Broker   | RabbitMQ, Apache Kafka                                                                                                         |
| Object Storage   | MinIO, Amazon S3                                                                                                               |
| Search Engine    | Elasticsearch, OpenSearch                                                                                                      |
| API Gateway      | NGINX, Traefik                                                                                                                 |
| LLM / AI Service | local models via [Ollama]                                                                                                      |
| Authentication   | Keycloak                                                                                                                       |
| Monitoring       | Prometheus, Grafana                                                                                                            |

## Architecture

The platform simulates a realistic cloud workflow.

```text
                ┌───────────────┐
                │     User      │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ API Gateway   │
                └───────┬───────┘
                        │
         ┌──────────────┼──────────────┐
         ▼                             ▼
 ┌───────────────┐            ┌───────────────┐
 │ AWS S3        │            │ Azure Blob    │
 │ LocalStack    │            │ Azurite       │
 └───────┬───────┘            └───────┬───────┘
         │                            │
         ▼                            ▼
 ┌───────────────┐            ┌───────────────┐
 │ SQS Queue     │            │ Azure Queue   │
 └───────┬───────┘            └───────┬───────┘
         │                            │
         ▼                            ▼
             ┌──────────────────┐
             │ Worker/Lambda    │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Metadata Store   │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Monitoring       │
             │ Logging          │
             │ Tracing          │
             └──────────────────┘
```
