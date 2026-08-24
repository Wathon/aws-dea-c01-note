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
- **Hub Links**: [[index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 2.1: Choose data storage solutions
- **Object Storage**: [[s3]] (S3 Standard, Intelligent-Tiering, Glacier, S3 Express One Zone).
- **Block & File Systems**: [[ebs-and-instance-store]] (EBS gp3/io2, Instance Store), [[efs-and-fsx]] (EFS, FSx for Lustre), [[ebs-vs-efs-vs-instance-store]] (Storage Comparison Matrix).
- **Data Warehousing**: [[redshift]] (Redshift Provisioned RA3, Redshift Serverless, Redshift Spectrum).
- **NoSQL & Specialized Databases**: [[dynamodb]], [[nosql-specialized-databases]] (ElastiCache, Timestream, Neptune, OpenSearch).

### Task Statement 2.2: Design data models and schema evolution
- **Relational vs Dimensional Modeling**: Star schema vs Snowflake schema in [[redshift]].
- **Partition Keys & Sort Keys**:
  - Primary key design, Partition keys, Sort keys, LSI/GSI in [[dynamodb]].
  - Distribution keys (EVEN, KEY, ALL) and Sort keys (COMPOUND, INTERLEAVED) in [[redshift]].
- **Schema Evolution & Cataloging**: Using [[glue]] Schema Registry and Data Catalog to handle schema drift.

### Task Statement 2.3: Manage data lifecycles & storage optimization
- **S3 Lifecycle Management**: Transition rules (Standard -> Standard-IA -> Glacier Flexible / Deep Archive), expiration rules.
- **S3 Object Lock & Immutability**: WORM (Write Once Read Many) for compliance (Governance mode vs Compliance mode).
- **Compaction & Vacuuming**: VACUUM and ANALYZE operations in [[redshift]] for reclaimed storage and query optimization.

---

## 🛠️ Essential AWS Services in Domain 2

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **Amazon S3** | Data Lake Object Storage | Central data lake storage, lifecycle tiering, S3 Express One Zone | [[s3]] |
| **Amazon Redshift** | Petabyte-Scale DW | OLAP queries, RA3 managed storage, Redshift Spectrum for S3 querying | [[redshift]] |
| **Amazon DynamoDB** | Serverless NoSQL | Low-latency key-value store, DynamoDB Streams for CDC | [[dynamodb]] |
| **Amazon RDS & Aurora** | Hosted OLTP Databases | Relational database workloads, Aurora Serverless v2, Read Replicas | [[rds-and-aurora]] |
| **FSx for Lustre** | High-Perf File Storage | Fast parallel file system for HPC & EMR/S3 staging | [[efs-and-fsx]] |

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
- [ ] Complete service notes: [[s3]], [[redshift]], [[dynamodb]], [[rds-and-aurora]]
- [ ] Review concepts: [[data-modeling-and-partitioning]], [[data-formats-and-compression]]
