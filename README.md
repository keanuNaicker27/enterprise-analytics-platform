**Executive Summary**
This project demonstrates a production-grade, multi-cloud data ecosystem designed for high availability, vendor agnosticism, and zero-egress analytics. Unlike traditional single-cloud stacks, this architecture treats cloud providers as specialized compute nodes governed by a centralized Control Plane.

**Architecture Design**
1. Platform Map (The Layout)
This view defines our multi-cloud footprint, leveraging the "Best of Breed" services from each provider.

2. Data Lifecycle (The Flow)
Ingestion (AWS): Raw event data is captured in S3 via Kinesis.

Transformation (AWS): AWS Glue (PySpark) handles heavy ETL, converting raw JSON to optimized Parquet.

Analytics (GCP): BigQuery Omni queries the S3 data lake directly, avoiding massive data transfer fees.

Orchestration (Azure): Azure Data Factory manages cross-cloud triggers and final delivery to Power BI.

**Key Technical Features**
Zero-Egress Strategy: Utilized BigQuery Omni to perform "in-place" analytics on AWS S3 data, significantly reducing monthly cloud networking costs.

Infrastructure as Code (IaC): 100% of the cross-cloud resources (S3, BQ Datasets, Resource Groups) are managed via Terraform to ensure environment parity and disaster recovery.

Secure Workload Identity: Implemented OIDC-based Workload Identity Federation to allow Glue Jobs to authenticate with GCP without the use of permanent, high-risk Service Account keys.

Centralized Governance: Design includes a metadata abstraction layer to ensure consistent schema definition across Redshift, BigQuery, and Synapse.

**Project Structure**

Enterprise-analytics-platform/
├── architecture/      # High-level system & lineage diagrams
├── infrastructure/    # Terraform modules for cross-cloud provisioning
├── aws/               # Glue ETL (PySpark) & Redshift (PostgreSQL) logic
├── gcp/               # BigQuery Omni SQL & Vertex AI configurations
├── azure/             # ADF Pipeline definitions (JSON) & Synapse SQL
├── datasets/          # Sample raw event data for testing
└── docs/              # Architecture Decision Records (ADRs)

**Getting Started**
Provision Infrastructure:

Bash

cd infrastructure/terraform
terraform init && terraform apply
Deploy ETL Logic:

Upload aws/glue_job.py to the Glue Script bucket.

Initialize the ADF pipeline in azure/.

Run Analytics:

Execute gcp/bigquery.sql to see cross-cloud query results in real-time.

**Design Philosophy**
For a deep dive into the "Why" behind these choices—including cost comparisons and security trade-offs—see my Design Decisions & ADRs.
