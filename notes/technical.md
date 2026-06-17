# Technical Notes

Here is an outlook into some technical elements of cloud computing

## External Micro-Services

For most production applications, ordered by how frequently they are needed:

| Rank | Category                    | Typical Examples                                               | Importance                                                |
| ---- | --------------------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| 1    | Backend / API Service       | Python, Java Spring Boot, Go, Node.js                          | Core business logic; application cannot exist without it  |
| 2    | Database                    | PostgreSQL, MySQL, MongoDB                                     | Persistent storage; nearly universal                      |
| 3    | Frontend                    | React, Angular, Vue                                            | Required for most user-facing applications                |
| 4    | API Gateway / Reverse Proxy | Nginx, Traefik                                                 | Routing, TLS termination, load balancing                  |
| 5    | Cache                       | Redis, Memcached                                               | Common performance optimization                           |
| 6    | Authentication              | Keycloak                                                       | Very common for enterprise apps                           |
| 7    | Background Worker           | Celery, Sidekiq, BullMQ                                        | Async processing and scheduled tasks                      |
| 8    | Message Broker              | RabbitMQ, Apache Kafka                                         | Needed once services become distributed                   |
| 9    | Monitoring                  | Prometheus, Grafana                                            | Essential in mature production environments               |
| 10   | Logging                     | ELK Stack, Grafana Loki                                        | Usually added after monitoring                            |
| 11   | Object Storage              | MinIO, Amazon Web Services S3                                  | Needed for files, images, models, backups                 |
| 12   | Search Engine               | Elasticsearch, OpenSearch                                      | Useful only when advanced search is required              |
| 13   | LLM / AI Service            | [Ollama](https://ollama.com?utm_source=chatgpt.com), vLLM, TGI | Emerging but still niche compared to databases and caches |

For a portfolio project that demonstrates modern cloud-native architecture without excessive complexity, a very representative stack would be:

Frontend    \
    ↓       \
API Service \
    ↓       \
PostgreSQL
+ Redis
+ Keycloak
+ Prometheus/Grafana

and later:
+ RabbitMQ
+ Worker
+ MinIO

## Architecture

The platform simulates a realistic cloud workflow.

```text
                ┌───────────────┐
                │     User      │
                └───────┬───────┘
                        ▼
                ┌───────────────┐
                │ API Gateway   │
                └───────┬───────┘
         ┌──────────────┼──────────────┐
         ▼                             ▼
 ┌───────────────┐            ┌───────────────┐
 │ AWS S3        │            │ Azure Blob    │
 │ LocalStack    │            │ Azurite       │
 └───────┬───────┘            └───────┬───────┘
         ▼                            ▼
 ┌───────────────┐            ┌───────────────┐
 │ SQS Queue     │            │ Azure Queue   │
 └───────┬───────┘            └───────┬───────┘
         ▼                            ▼
             ┌──────────────────┐
             │ Worker/Lambda    │
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ Metadata Store   │
             └────────┬─────────┘
                      ▼
             ┌──────────────────┐
             │ Monitoring       │
             │ Logging          │
             │ Tracing          │
             └──────────────────┘
```

## Network

Good practices for ports in containerized systems:
- Use conventional ports inside containers:
  - e.g. 80 (HTTP), 443 (HTTPS), 5432 (PostgreSQL)
  - Keeps services predictable and portable
- Never hardcode host ports in images
  - Host mapping belongs to deployment, not Dockerfile
- Avoid conflicts on the host
  - Each exposed service must use a unique host port
  - e.g. -p 8080:80, -p 8081:80
- Use high host ports for dev
  - Typically > 1024 (e.g. 3000, 8000, 8080, 5000)
  - Avoids clashes with system services
- Standardize per service
  - Example convention:
    - API → 8000
    - Frontend → 3000
    - Admin → 8080
- Use reverse proxy in production
  - Expose only 80/443 externally (via NGINX/Traefik)
  - Internal services keep private ports
- Avoid random ports unless testing
  - p 0:80 is fine for quick experiments, not reproducibility

Core idea:
- container ports = semantic/service-level
- host ports = environment/deployment-level

