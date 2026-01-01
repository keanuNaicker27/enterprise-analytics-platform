# Architecture Decision Records (ADR)

### ADR 001: Multi-Cloud Strategy
**Context:** Need to utilize AWS for high-volume ingestion and GCP for Vertex AI/ML.

**Decision:** Use AWS S3 as the global landing zone and BigQuery Omni for cross-cloud analysis.

**Consequence:** Avoids $X,000/mo in data egress fees by querying S3 data directly from GCP.

### ADR 002: Security & Identity
**Decision:** Implemented Workload Identity Federation. 

**Logic:** AWS Glue assumes a GCP Service Account role via OIDC, eliminating the need for hardcoded JSON keys in the repo.
