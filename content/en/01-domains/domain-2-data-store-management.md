---
title: "Domain 2: Data Store Management"
type: domain
tags:
  - domain/storage
  - dea-c01
  - exam-prep
date: 2026-07-28
---

# 🗄️ Domain 2: Data Store Management (Weight: 26%)

- **Domain ID**: Domain 2
- **Focus**: Choosing appropriate data stores, designing data schemas, managing data lifecycles, and optimizing storage performance and cost.
- **Hub Links**: [[en/index|index]] | [[en/00-hub/dea-c01-roadmap|dea-c01-roadmap]] | [[en/00-hub/service-catalog|service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 2.1: Choose data storage solutions
- **Object Storage**: [[en/02-services/storage/s3/s3|s3]] (S3 Standard, Intelligent-Tiering, Glacier, S3 Express One Zone).
- **Block & File Systems**: [[en/02-services/storage/ebs-and-instance-store|ebs-and-instance-store]] (EBS gp3/io2, Instance Store), [[en/02-services/storage/efs-and-fsx|efs-and-fsx]] (EFS, FSx for Lustre), [[en/02-services/storage/ebs-vs-efs-vs-instance-store|ebs-vs-efs-vs-instance-store]] (Storage Comparison Matrix).
- **Data Warehousing**: [[en/02-services/database/redshift|redshift]] (Redshift Provisioned RA3, Redshift Serverless, Redshift Spectrum).
- **NoSQL & Specialized Databases**: [[en/02-services/database/dynamodb|dynamodb]], [[en/02-services/database/nosql-specialized-databases|nosql-specialized-databases]] (ElastiCache, Timestream, Neptune, OpenSearch).

### Task Statement 2.2: Design data models and schema evolution
- **Relational vs Dimensional Modeling**: Star schema vs Snowflake schema in [[en/02-services/database/redshift|redshift]].
- **Partition Keys & Sort Keys**:
  - Primary key design, Partition keys, Sort keys, LSI/GSI in [[en/02-services/database/dynamodb|dynamodb]].
  - Distribution keys (EVEN, KEY, ALL) and Sort keys (COMPOUND, INTERLEAVED) in [[en/02-services/database/redshift|redshift]].
- **Schema Evolution & Cataloging**: Using [[en/02-services/analytics-streaming/glue/glue|glue]] Schema Registry and Data Catalog to handle schema drift.

### Task Statement 2.3: Manage data lifecycles & storage optimization
- **S3 Lifecycle Management**: Transition rules (Standard -> Standard-IA -> Glacier Flexible / Deep Archive), expiration rules.
- **S3 Object Lock & Immutability**: WORM (Write Once Read Many) for compliance (Governance mode vs Compliance mode).
- **Compaction & Vacuuming**: VACUUM and ANALYZE operations in [[en/02-services/database/redshift|redshift]] for reclaimed storage and query optimization.

---

## 🛠️ Essential AWS Services in Domain 2

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **Amazon S3** | Data Lake Object Storage | Central data lake storage, lifecycle tiering, S3 Express One Zone | [[en/02-services/storage/s3/s3|s3]] |
| **Amazon Redshift** | Petabyte-Scale DW | OLAP queries, RA3 managed storage, Redshift Spectrum for S3 querying | [[en/02-services/database/redshift|redshift]] |
| **Amazon DynamoDB** | Serverless NoSQL | Low-latency key-value store, DynamoDB Streams for CDC | [[en/02-services/database/dynamodb|dynamodb]] |
| **Amazon RDS & Aurora** | Hosted OLTP Databases | Relational database workloads, Aurora Serverless v2, Read Replicas | [[en/02-services/database/rds-and-aurora|rds-and-aurora]] |
| **FSx for Lustre** | High-Perf File Storage | Fast parallel file system for HPC & EMR/S3 staging | [[en/02-services/storage/efs-and-fsx|efs-and-fsx]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 2

> [!IMPORTANT]
> **Redshift Distribution Key Selection**:
> - **KEY Distribution**: Distribute rows based on values in a single column (e.g., `customer_id` matching join key). Ideal for joining large tables!
> - **ALL Distribution**: Duplicate the entire table to every compute node. Ideal for small, infrequently updated dimension tables (< 2-3 million rows).
> - **EVEN Distribution**: Round-robin distribution. Default for tables not joined frequently or where no clear join key exists.

> [!TIP]
> **S3 Express One Zone**:
> - Single-AZ storage class designed for **consistent single-digit millisecond latency** and up to 10x lower latency than S3 Standard. Ideal for high-throughput analytics (EMR, Athena, SageMaker checkpointing).

---

## 📌 Checklist for Domain 2
- [ ] Review slide pages: 76-154 (Storage) and 155-265 (Database) in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- [ ] Complete service notes: [[en/02-services/storage/s3/s3|s3]], [[en/02-services/database/redshift|redshift]], [[en/02-services/database/dynamodb|dynamodb]], [[en/02-services/database/rds-and-aurora|rds-and-aurora]]
- [ ] Review concepts: [[en/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]], [[en/03-concepts/data-formats-and-compression|data-formats-and-compression]]
