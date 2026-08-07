# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) Digital Garden

A digital garden and personal knowledge base for the **AWS Certified Data Engineer – Associate (DEA-C01)** certification exam, built with **Quartz** and deployed automatically via **GitHub Pages**.

Based on the official course slides by **Stephane Maarek & Frank Kane** (`AWSCertifiedDataEngineerSlides.pdf`).

---

## 🛠️ Local Development & Quartz Commands

All notes are written in Markdown and stored in `./content/`. Quartz compiles them into static web pages in `./public/`.

```bash
# Install dependencies
npm install

# Build static site locally
npx quartz build

# Preview site locally with live reload (http://localhost:8080)
npx quartz build --serve
```

---

## 📂 Workspace Structure (`./content/`)

`./content/` is the single source of truth for all notes, media, and lab materials.

- **`content/00-hub/`**: Master Maps of Content (MOCs), certification roadmap, service catalog, and lab materials index.
- **`content/01-domains/`**: Breakdown of the 4 official DEA-C01 exam domains & task statements.
- **`content/02-services/`**: Deep-dive notes for AWS Data Engineering services:
  - `storage/s3/`: S3 Overview, Performance, Encryption, Access Points, Tables, and Storage Lens.
  - `storage/`: EBS, Instance Store, EFS, and FSx.
  - `analytics-streaming/`: Athena, Glue, EMR, Kinesis, MSK Kafka, OpenSearch, QuickSight.
  - `database/`: Redshift, DynamoDB, RDS & Aurora, ElastiCache, Timestream, Neptune.
  - `integration/`: SQS, SNS, Step Functions, MWAA Airflow, AppFlow.
  - `compute-containers/`: Lambda, Batch, ECR, ECS, EKS.
  - `security-governance/`: Lake Formation, IAM, KMS, Secrets Manager, Macie, CloudTrail.
  - `migration/`: DMS, SCT, DataSync, Snow Family.
  - `networking-monitoring/`: VPC, Endpoints, CloudWatch, EventBridge.
  - `ml-dev-cost/`: SageMaker, CDK, CloudFormation, Cost Explorer, Budgets.
- **`content/03-concepts/`**: Core data engineering principles (Big Data V's, Parquet/ORC/Avro, Partitioning, Data Quality, SQL).
- **`content/04-exam-tips/`**: Decision matrices, service comparisons, and high-frequency exam scenarios.
- **`content/materials/`**: Hands-on lab scripts (Bash CLI), sample datasets (CSV/JSON/TXT), CloudFormation/CDK templates, and SQL exercises.
- **`content/journal/`**: Daily study logs.
- **`content/docs/`**: Reference PDF slides (`AWSCertifiedDataEngineerSlides.pdf`).

---

## 🚢 Automated Deployment

Pushing changes to the `main` branch automatically triggers the **GitHub Actions workflow** (`.github/workflows/deploy.yml`), which builds the site with Quartz and publishes it to GitHub Pages.

---

## 🔗 Key Links

- **Central Hub**: `content/00-hub/index.md`
- **Certification Blueprint**: `content/00-hub/dea-c01-roadmap.md`
- **AWS Service Index**: `content/00-hub/service-catalog.md`
- **Decision Matrix**: `content/04-exam-tips/service-comparisons.md`
- **Hands-on Lab Index**: `content/00-hub/lab-materials-index.md`
