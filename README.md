# Cloud Platform Core

A production-inspired local cloud platform that emulates AWS essential services using Docker. The goal is to provide a hands-on environment for learning and experimenting on modern cloud engineering.

---

## Overview

This project reproduces common cloud-native architectures locally using:

* AWS-compatible services via LocalStack
* Docker and Docker Compose
* Infrastructure-as-Code
* CI/CD pipelines

The repository is designed as both:

1. A learning platform with progressively advanced topics.
2. A portfolio project showcasing practical cloud engineering skills.

---

## Objectives

### Cloud Engineering

* AWS service integration
* Event-driven architectures
* Serverless computing
* Infrastructure automation
* Container orchestration

### DevOps

* Docker
* CI/CD pipelines
* Infrastructure as Code
* Automated testing
* Monitoring and logging

### Software Engineering

* Clean architecture
* Modular design
* Documentation
* Reproducibility
* Testing

---

## Repository Structure

```text
cloud_emulator/
├── docker/
│   ├── localstack/
│   ├── monitoring/
│   └── reverse-proxy/
├── infra/
│   ├── bootstrap/
│   └── scripts/
├── apps/
│   ├── api/
│   └── worker/
├── diagrams/
├── tests/
├── .github/
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## Quickstart

The current slice implements the first half of the event-driven file processing
example below: upload → S3 → SQS → worker → DynamoDB.

```bash
cp .env.example .env
make up
```

Upload a file:

```bash
curl -F file=@README.md http://localhost:8000/upload
# {"file_id": "...", "bucket": "uploads", "key": ".../README.md", ...}
```

Fetch the metadata once the worker has processed it:

```bash
curl http://localhost:8000/files/<file_id>
```

Other commands:

```bash
make logs   # tail all service logs
make test   # run the integration test suite against the running stack
make down   # stop the stack
make reset  # wipe volumes and rebuild from scratch
```

---

## Example Use Case

### Event-Driven File Processing

1. User uploads a file.
2. File is stored in S3 Blob Storage.
3. Storage event generates a queue message.
4. Worker consumes the message.
5. Metadata is extracted.
6. Results are stored in a database.
7. Metrics and logs are collected.
8. Dashboards visualize platform activity.

This architecture demonstrates common cloud patterns used in production systems.

---

## Production Considerations

This project intentionally runs locally.

A production deployment would typically replace:

| Local Component | Production Equivalent         |
| --------------- | ----------------------------- |
| LocalStack      | AWS Managed Services          |
| Docker Compose  | Kubernetes                    |
| Local Volumes   | Managed Storage               |

The objective is to learn architectural concepts while maintaining a fully reproducible development environment.

---

## Future Extensions

* Observability stack
* Security layer
* ...

---

## License

MIT License

---

## Disclaimer

This project is intended for education, experimentation, and portfolio development. It does not attempt to fully replicate AWS or Azure behavior and should not be used as a substitute for production cloud environments.

