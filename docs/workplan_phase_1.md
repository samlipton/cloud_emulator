# Phase 1 — Foundations (14 Days)

## Objectives

At the end of Phase 1, you should have:

* a reproducible local cloud platform
* Docker mastery beyond basics
* LocalStack + Azurite running cleanly
* proper networking
* persistent volumes
* service discovery
* structured repository
* initial architecture diagrams
* production-like local workflows

The deliverable is a maintainable local cloud engineering platform.

---

# Day 1 — Docker Deep Fundamentals

## Goals  

* namespaces
* cgroups
* layers
* images
* volumes
* networks
* entrypoints
* bridge networking

## Study Material

* [Docker Overview Documentation](https://docs.docker.com/get-started/docker-overview/?utm_source=chatgpt.com)
* [Docker Networking](https://docs.docker.com/network/?utm_source=chatgpt.com)
* [Docker Storage Volumes](https://docs.docker.com/storage/volumes/?utm_source=chatgpt.com)
* [Containers From Scratch by Liz Rice](https://www.youtube.com/watch?v=8fi7uSYlOdc&utm_source=chatgpt.com) (This lecture is extremely important.)

## Practical Work

Build:
* one Python container
* one Redis container
* connect them manually

With:
* `docker build`
* `docker exec`
* `docker network`
* `docker volume`
* `docker inspect`

## Deliverables

* docs/day1-notes.md
* docker/python-api/
* docker/redis/

---

# Day 2 — Advanced Dockerfiles

## Goals

* multi-stage builds
* layer optimization
* caching
* security
* minimal images

## Study Material

* [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/?utm_source=chatgpt.com)
* [Distroless Images](https://github.com/GoogleContainerTools/distroless?utm_source=chatgpt.com)

## Practical Work

Build:
* optimized FastAPI container
* development image
* production image

Add:
* non-root user
* healthcheck
* `.dockerignore`

## Deliverables

* apps/api/
* Dockerfile.dev
* Dockerfile.prod

---

# Day 3 — Docker Compose Architecture

## Goals

* service orchestration
* dependency management
* startup order
* environment management
* internal DNS

## Study Material

* [Docker Compose Documentation](https://docs.docker.com/compose/?utm_source=chatgpt.com)

## Practical Work

Build:
* API
* Redis
* PostgreSQL

With:
* persistent volumes
* isolated network
* environment variables

## Deliverables

* docker-compose.yml
* .env.example

---

# Day 4 — Reverse Proxy + Networking

## Goals

* reverse proxies
* routing
* TLS
* ingress concepts
* internal vs external networking

## Study Material

* [NGINX Beginner Guide](https://nginx.org/en/docs/beginners_guide.html?utm_source=chatgpt.com)
* [Traefik Documentation](https://doc.traefik.io/traefik/?utm_source=chatgpt.com)

## Practical Work

Deploy:
* Traefik or NGINX
* route traffic to services
* expose dashboard
* create internal-only services

## Deliverables

* docker/reverse-proxy/

---

# Day 5 — LocalStack Fundamentals

## Goals

* AWS emulation boundaries
* supported services
* IAM limitations
* endpoint overrides

## Study Material

* [LocalStack Documentation](https://docs.localstack.cloud/?utm_source=chatgpt.com)
* [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/reference/?utm_source=chatgpt.com)

## Practical Work

Run:
* S3
* SQS
* DynamoDB

Interact using:
* AWS CLI
* boto3

## Deliverables

* docker/localstack/
* scripts/aws/

---

# Day 6 — Advanced LocalStack

## Goals

* Lambda emulation
* EventBridge
* API Gateway
* queue triggers

## Study Material

* [LocalStack Lambda Docs](https://docs.localstack.cloud/user-guide/aws/lambda/?utm_source=chatgpt.com)

## Practical Work

Implement (first real architecture): 
* upload file to S3
* emit queue event
* trigger Lambda
* write metadata to DynamoDB

## Deliverables

* apps/lambda-worker/

---

# Day 7 — Azurite Fundamentals

## Goals

* Azure Storage architecture
* blobs
* queues
* tables

## Study Material

* [Azurite Repository](https://github.com/Azure/Azurite?utm_source=chatgpt.com)
* [Azure Storage Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction?utm_source=chatgpt.com)

## Practical Work

Implement:
* blob uploads
* queue messaging
* metadata persistence

Use:
* Azure SDK for Python

## Deliverables

* docker/azurite/
* scripts/azure/

---

# Day 8 — Unified Cloud Abstraction

## Goals

* cloud adapters
* provider abstraction
* interchangeable backends

## Study Material

* [SOLID Principles Overview](https://en.wikipedia.org/wiki/SOLID?utm_source=chatgpt.com)

## Practical Work

Create:
```python
class StorageProvider:
    upload()
    download()
```

Then:
* AWS implementation
* Azure implementation

## Deliverables

* apps/shared/cloud/

---

# Day 9 — Observability Foundations

## Goals

* metrics
* logs
* traces
* exporters

## Study Material

* [Prometheus Introduction](https://prometheus.io/docs/introduction/overview/?utm_source=chatgpt.com)
* [Grafana Documentation](https://grafana.com/docs/?utm_source=chatgpt.com)

## Practical Work

Deploy:
* Prometheus
* Grafana

Expose:
* container metrics
* application metrics

## Deliverables

* docker/monitoring/

---

# Day 10 — Structured Logging

## Goals

* centralized logs
* correlation IDs
* JSON logging

## Study Material

* [OpenTelemetry Documentation](https://opentelemetry.io/docs/?utm_source=chatgpt.com)

## Practical Work

Add:
* structured logging middleware
* trace IDs
* request IDs

## Deliverables

* apps/shared/logging/

---

# Day 11 — Infrastructure Automation

## Goals

* avoid manual operations
* everything is scriptable

## Practical Work

Create:
* Makefile
* bootstrap scripts
* environment initialization

Test:
```bash
make up
make down
make reset
make logs
make test
```

## Study Material

* [GNU Make Manual](https://www.gnu.org/software/make/manual/make.html?utm_source=chatgpt.com)

## Deliverables

* Makefile
* infra/scripts/

---

# Day 12 — Testing the Platform

## Goals

* integration testing
* container testing
* endpoint testing

## Study Material

* [pytest Documentation](https://docs.pytest.org/?utm_source=chatgpt.com)
* [Testcontainers Python](https://testcontainers-python.readthedocs.io/?utm_source=chatgpt.com)

## Practical Work

Test:
* API
* queue flow
* storage flow
* Lambda flow

## Deliverables

* tests/integration/

---

# Day 13 — Documentation + Diagrams

## Goals

* professional documentation.

## Study Material

* [C4 Model Documentation](https://c4model.com/?utm_source=chatgpt.com)

## Practical Work

Create:
* context diagram
* container diagram
* component diagram

Document:
* architecture decisions
* tradeoffs
* limitations

## Deliverables

* docs/architecture.md
* diagrams/

---

# Day 14 — Refactoring + Production Polish

## Goals

* stabilize everything

## Practical Work

Refactor:
* naming
* folder structure
* configs
* environment variables

Improve:
* README
* onboarding
* screenshots
* examples

Add:
* badges
* quickstart
* troubleshooting

---

# Final Deliverable of Phase 1

## Functional platform

* Dockerized services
* Local AWS emulation
* Local Azure emulation
* reverse proxy
* persistent storage
* metrics/logging
* automated startup

## Engineering quality

* clean repository
* diagrams
* tests
* scripts
* reproducibility

## Portfolio value

* systems thinking
* DevOps maturity
* cloud architecture understanding
* software engineering rigor
* documentation quality

