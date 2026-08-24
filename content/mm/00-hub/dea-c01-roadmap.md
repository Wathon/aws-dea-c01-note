---
title: AWS DEA-C01 Certification Roadmap (မြန်မာဘာသာ)
type: hub
tags:
  - roadmap
  - dea-c01
  - exam-prep
  - burmese
date: 2026-07-28
---

# 🎯 AWS Certified Data Engineer – Associate (DEA-C01) Exam Roadmap (မြန်မာဘာသာ)

- **Language / ဘာသာစကား**: [English (Original)](/en/00-hub/dea-c01-roadmap) | **မြန်မာဘာသာ (Burmese)**

**AWS Certified Data Engineer – Associate (DEA-C01)** သည် data-driven solutions များ၊ data architecture၊ data ingestion၊ transformation၊ storage management၊ operations၊ security နှင့် governance ဆိုင်ရာ ကျွမ်းကျင်မှုများကို စစ်ဆေးအတည်ပြုပေးပါသည်။

---

## 📊 Exam Structure & Weightings

```mermaid
pie title DEA-C01 Domain Weightings
    "Domain 1: Data Ingestion and Processing" : 28
    "Domain 2: Data Store Management" : 26
    "Domain 3: Data Operations and Support" : 22
    "Domain 4: Data Security and Governance" : 24
```

| Domain | Weighting | Key Focus Areas | Note Link |
| --- | --- | --- | --- |
| **Domain 1: Data Ingestion and Processing** | **28%** | Batch vs Streaming ingestion, ETL pipelines, transformation, schema evolution, Glue, Kinesis, Lambda, MWAA, Step Functions | [[mm/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]] |
| **Domain 2: Data Store Management** | **26%** | Data store selection, schema design, Redshift, S3, DynamoDB, RDS/Aurora, OpenSearch, storage tiering & partitioning | [[mm/01-domains/domain-2-data-store-management|domain-2-data-store-management]] |
| **Domain 3: Data Operations and Support** | **22%** | Pipeline automation, monitoring, CloudWatch, EventBridge, error handling, performance tuning, data quality (Glue DQ) | [[mm/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]] |
| **Domain 4: Data Security and Governance** | **24%** | Identity & access management (IAM), encryption (KMS), governance (Lake Formation, DataZone), PII protection (Macie) | [[mm/01-domains/domain-4-data-security-and-governance|domain-4-data-security-and-governance]] |

---

## 📅 Recommended 4-Week Study Strategy

```mermaid
gantt
    title DEA-C01 Study Plan
    dateFormat  YYYY-MM-DD
    section Fundamentals & Storage
    Big Data & SQL Concepts    :a1, 2026-07-28, 3d
    S3 & Database Deep Dives   :a2, after a1, 4d
    section Ingestion & Processing
    Glue, Athena & EMR         :b1, after a2, 5d
    Kinesis & Streaming        :b2, after b1, 4d
    section Ops, Governance & ML
    Lake Formation & IAM       :c1, after b2, 4d
    Step Functions & MWAA      :c2, after c1, 3d
    section Final Review
    Service Comparisons & Mocks:d1, after c2, 5d
```

### Week 1: Fundamentals & Core Data Stores
- Big Data 5 V's၊ SQL joins/window functions များကို ပြန်လည်သုံးသပ်ခြင်း: [[mm/03-concepts/big-data-fundamentals|big-data-fundamentals]], [[mm/03-concepts/sql-and-version-control-review|sql-and-version-control-review]]
- S3 Storage Classes၊ Lifecycle၊ Object Lock & Replication: [[mm/02-services/storage/s3/s3|s3]]
- Relational (RDS/Aurora) & NoSQL (DynamoDB, Redshift): [[mm/02-services/database/rds-and-aurora|rds-and-aurora]], [[mm/02-services/database/dynamodb|dynamodb]], [[mm/02-services/database/redshift|redshift]]

### Week 2: Ingestion, Compute & Analytics Pipelines
- Kinesis Data Streams / Firehose / MSK ဖြင့် Data Ingestion ပြုလုပ်ခြင်း: [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]], [[mm/02-services/analytics-streaming/msk/msk|msk]]
- Serverless & Container Compute: [[mm/02-services/compute-containers/lambda|lambda]], [[mm/02-services/compute-containers/batch|batch]], [[mm/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]], [[mm/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]]
- AWS Glue ဖြင့် ETL ပြုလုပ်ခြင်း (Crawlers, Catalog, Jobs, DataBrew, Data Quality): [[mm/02-services/analytics-streaming/glue/glue|glue]]
- Athena ဖြင့် Interactive Querying ပြုလုပ်ခြင်း & EMR ဖြင့် Big Data စီမံခြင်း: [[mm/02-services/analytics-streaming/athena/athena|athena]], [[mm/02-services/analytics-streaming/emr/emr|emr]]

### Week 3: Orchestration, Governance & Security
- Step Functions & MWAA (Airflow) ဖြင့် Workflow orchestration ပြုလုပ်ခြင်း: [[mm/02-services/integration/step-functions/step-functions|step-functions]], [[mm/02-services/integration/mwaa-airflow|mwaa-airflow]]
- Lake Formation၊ IAM၊ KMS တို့ဖြင့် Governance & Access Control စီမံခြင်း: [[mm/02-services/security-governance/lake-formation|lake-formation]], [[mm/02-services/security-governance/iam|iam]], [[mm/02-services/security-governance/kms-and-secrets|kms-and-secrets]]
- Migration & Transfer: [[mm/02-services/migration/dms-and-sct|dms-and-sct]], [[mm/02-services/migration/datasync-and-snow|datasync-and-snow]], [[mm/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]], [[mm/02-services/migration/data-exchange|data-exchange]], [[mm/02-services/migration/transfer-family|transfer-family]]

### Week 4: Scenarios, Optimization & Exam Practice
- Cross-service decision matrix ကို ပြန်လည်သုံးသပ်ခြင်း: [[mm/04-exam-tips/service-comparisons|service-comparisons]]
- စာမေးပွဲတွင် မကြာခဏတွေ့ရတတ်သော High-frequency exam traps & keywords များ: [[mm/04-exam-tips/high-frequency-exam-patterns|high-frequency-exam-patterns]]
- Slide Exam Tips များကို ပြန်လည်သုံးသပ်ခြင်း: [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)

---

## 📌 Master Hub Link
Return to main hub: [[mm/index|index]]
