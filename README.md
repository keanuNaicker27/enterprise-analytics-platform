**Executive Summary**

This repository contains a production-grade, multi-cloud data ecosystem. As a Staff-Level project, it demonstrates how to treat cloud providers as specialized compute nodes governed by a centralized Control Plane. The architecture prioritizes zero-egress analytics, automated governance, and infrastructure-as-code.

**Architecture Design**

1. Platform Map (The Layout)
A high-level view of our multi-cloud footprint, leveraging "Best of Breed" services from AWS, GCP, and Azure.

2. Data Lifecycle (The Journey)
Detailed lineage showing data moving from raw ingestion to executive-level reporting.

**Project Structure**
```python

.
├── 📁 architecture/             # System diagrams & lineage maps
│   ├── platform-overview.png
│   └── data-lifecycle.png
├── 📁 infrastructure/           # Global Control Plane (IaC)
│   ├── 📁 terraform/
│   │   └── main.tf              # Multi-cloud provider resources
│   └── 📁 github-actions/
│       └── ci-cd-pipeline.yml   # Automated linting & deployment
├── 📁 aws/                      # Ingestion & Heavy ETL
│   ├── 📁 glue/
│   │   └── glue_job.py          # PySpark transformation logic
│   └── 📁 redshift/
│       └── redshift_schema.sql  # Data warehouse definitions
├── 📁 gcp/                      # Advanced Analytics & ML
│   └── 📁 bigquery/
│       └── bigquery.sql    # Zero-egress cross-cloud queries
├── 📁 azure/                    # Enterprise Integration
│   ├── 📁 pipelines/
│   │   └── adf-pipeline.json    # Visual workflow definitions
│   └── 📁 synapse/
│       └── synapse.sql  # Azure-native reporting logic
├── 📁 scripts/                  # Tooling & Utilities
│   └── generate_data.py         # Synthetic 100-record JSON generator
├── 📁 datasets/                 # Sample Data
│   └── sample-data.json         # Raw nested event records
└── 📁 docs/                     # Strategic Documentation
    └── design-decisions.md      # Architecture Decision Records (ADRs)
```
    
**Key Technical Feature**s
1. Zero-Egress Analytics: Implementation of BigQuery Omni to query data residing in AWS S3 directly, eliminating costly cross-cloud data transfer fees.

2. Infrastructure as Code (IaC): Automated provisioning of global resources using Terraform, ensuring environment parity across providers.

3. DataOps & CI/CD: GitHub Actions pipeline that automates Python linting, SQL validation, and Terraform planning on every push.

4. Identity Federation: Advanced security using Workload Identity Federation (OIDC) to allow cross-cloud communication without storing long-lived JSON keys.

**Quick Start**
1. Generate Test Data:

```bash
# Bash Script
python scripts/generate_data.py # Creates 100 nested JSON records
```
2. Deploy Infrastructure:

```bash
# Bash Script
cd infrastructure/terraform
terraform init && terraform apply
```
3. Run ETL:

Upload aws/glue/glue_job.py to your AWS environment to process the generated sample-data.json.

**Design Philosophy**

This project follows the ADR (Architecture Decision Record) pattern. For a deep dive into why specific clouds were chosen for specific workloads, cost-benefit analyses, and security trade-offs, see the Design Decisions document.
