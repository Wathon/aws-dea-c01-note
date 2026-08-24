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
| **Domain 1: Data Ingestion and Processing** | **28%** | Batch vs Streaming ingestion, ETL pipelines, transformation, schema evolution, Glue, Kinesis, Lambda, MWAA, Step Functions | [[domain-1-ingestion-and-processing]] |
| **Domain 2: Data Store Management** | **26%** | Data store selection, schema design, Redshift, S3, DynamoDB, RDS/Aurora, OpenSearch, storage tiering & partitioning | [[domain-2-data-store-management]] |
| **Domain 3: Data Operations and Support** | **22%** | Pipeline automation, monitoring, CloudWatch, EventBridge, error handling, performance tuning, data quality (Glue DQ) | [[domain-3-data-operations-and-support]] |
| **Domain 4: Data Security and Governance** | **24%** | Identity & access management (IAM), encryption (KMS), governance (Lake Formation, DataZone), PII protection (Macie) | [[domain-4-data-security-and-governance]] |

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
- Big Data 5 V's၊ SQL joins/window functions များကို ပြန်လည်သုံးသပ်ခြင်း: [[big-data-fundamentals]], [[sql-and-version-control-review]]
- S3 Storage Classes၊ Lifecycle၊ Object Lock & Replication: [[s3]]
- Relational (RDS/Aurora) & NoSQL (DynamoDB, Redshift): [[rds-and-aurora]], [[dynamodb]], [[redshift]]

### Week 2: Ingestion, Compute & Analytics Pipelines
- Kinesis Data Streams / Firehose / MSK ဖြင့် Data Ingestion ပြုလုပ်ခြင်း: [[kinesis]], [[msk]]
- Serverless & Container Compute: [[lambda]], [[batch]], [[ecr-ecs-eks]], [[ec2-and-graviton]]
- AWS Glue ဖြင့် ETL ပြုလုပ်ခြင်း (Crawlers, Catalog, Jobs, DataBrew, Data Quality): [[glue]]
- Athena ဖြင့် Interactive Querying ပြုလုပ်ခြင်း & EMR ဖြင့် Big Data စီမံခြင်း: [[athena]], [[emr]]

### Week 3: Orchestration, Governance & Security
- Step Functions & MWAA (Airflow) ဖြင့် Workflow orchestration ပြုလုပ်ခြင်း: [[step-functions]], [[mwaa-airflow]]
- Lake Formation၊ IAM၊ KMS တို့ဖြင့် Governance & Access Control စီမံခြင်း: [[lake-formation]], [[iam]], [[kms-and-secrets]]
- Migration & Transfer: [[dms-and-sct]], [[datasync-and-snow]], [[application-discovery-and-mgn]], [[data-exchange]], [[transfer-family]]

### Week 4: Scenarios, Optimization & Exam Practice
- Cross-service decision matrix ကို ပြန်လည်သုံးသပ်ခြင်း: [[service-comparisons]]
- စာမေးပွဲတွင် မကြာခဏတွေ့ရတတ်သော High-frequency exam traps & keywords များ: [[high-frequency-exam-patterns]]
- Slide Exam Tips များကို ပြန်လည်သုံးသပ်ခြင်း: [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)

---

## 📌 Master Hub Link
Return to main hub: [[mm/index]]
