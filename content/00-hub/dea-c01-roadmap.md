---
title: AWS DEA-C01 Certification Roadmap
type: hub
tags:
  - roadmap
  - dea-c01
  - exam-prep
date: 2026-07-28
---

# 🎯 AWS Certified Data Engineer – Associate (DEA-C01) Exam Roadmap

The **AWS Certified Data Engineer – Associate (DEA-C01)** validates expertise in data-driven solutions, data architecture, data ingestion, transformation, storage management, operations, security, and governance.

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
- Review Big Data 5 V's, SQL joins/window functions: [[big-data-fundamentals]], [[sql-and-version-control-review]]
- S3 Storage Classes, Lifecycle, Object Lock & Replication: [[s3]]
- Relational (RDS/Aurora) & NoSQL (DynamoDB, Redshift): [[rds-and-aurora]], [[dynamodb]], [[redshift]]

### Week 2: Ingestion & Analytics Pipelines
- Data Ingestion with Kinesis Data Streams / Firehose / MSK: [[kinesis]], [[msk-kafka]]
- ETL with AWS Glue (Crawlers, Catalog, Jobs, DataBrew, Data Quality): [[glue]]
- Interactive Querying with Athena & Big Data with EMR: [[athena]], [[emr]]

### Week 3: Orchestration, Governance & Security
- Workflow orchestration with Step Functions & MWAA (Airflow): [[step-functions]], [[mwaa-airflow]]
- Governance & Access Control with Lake Formation, IAM, KMS: [[lake-formation]], [[iam]], [[kms-and-secrets]]
- Migration & Transfer: [[dms-and-sct]], [[datasync-and-snow]], [[application-discovery-and-mgn]], [[data-exchange]], [[transfer-family]]

### Week 4: Scenarios, Optimization & Exam Practice
- Review cross-service decision matrix: [[service-comparisons]]
- High-frequency exam traps & keywords: [[high-frequency-exam-patterns]]
- Slide Exam Tips review: [[AWSCertifiedDataEngineerSlides.pdf]]

---

## 📌 Master Hub Link
Return to main hub: [[index]]
