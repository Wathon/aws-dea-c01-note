---
title: DEA-C01 Service Decision Matrix & Comparisons
type: exam-tip
tags:
  - exam-tip
  - dea-c01
  - comparison
date: 2026-07-28
---

# ⚡ DEA-C01 Service Decision Matrix & Comparisons

Quick reference decision guide for resolving architectural choices on the AWS Certified Data Engineer Associate exam.

---

## 1. Storage & Database Choice Matrix

```mermaid
graph TD
    Data[Data Type?] --> Structured[Structured OLTP / Relational]
    Data --> Analytics[Structured OLAP / Warehousing]
    Data --> SemiStructured[NoSQL Key-Value / Document]
    Data --> DataLake[Object / Unstructured Data Lake]
    Data --> SharedFile[Shared POSIX File System]
    Data --> HighIOPSBlock[High-IOPS Scratch Block]

    Structured --> RDS[[RDS / Aurora]]
    Analytics --> Redshift[[Amazon Redshift]]
    SemiStructured --> DynamoDB[[Amazon DynamoDB]]
    DataLake --> S3[[Amazon S3]]
    SharedFile --> EFS[[Amazon EFS / FSx]]
    HighIOPSBlock --> InstStore[[EC2 Instance Store / EBS]]
```

### Storage Decision Matrix: S3 vs EBS vs EFS vs Instance Store vs FSx for Lustre

| Storage Service | Protocol / Model | Scope / Durability | Persistence on STOP | Primary Data Engineering Role |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon S3** | Object (REST API) | Multi-AZ (11 9's) | ✅ Persistent | Central Data Lake, Bronze/Silver/Gold analytics tables |
| **Amazon EBS** | Block device (Network) | Single-AZ (99.9%+) | ✅ Persistent | Hosted relational databases, Kafka commit logs, OS boot |
| **EC2 Instance Store** | Block device (PCIe Bus) | Host Server (Single Disk) | ❌ **WIPED** | **Spark shuffle partition cache, MapReduce spills, temp buffers** |
| **Amazon EFS** | POSIX File (NFSv4.1) | Multi-AZ (11 9's) | ✅ Persistent | **Multi-AZ shared directories, Lambda model storage, EKS/ECS PVs** |
| **AWS FSx for Lustre** | High-Perf Parallel File | Single-AZ (Linked S3) | ✅ Persistent in S3 | **Sub-ms HPC processing, distributed ML training, EMR staging** |

> 🔗 **Deep Dive Reference**: See [[ebs-vs-efs-vs-instance-store]] for comprehensive lifecycle, throughput, and architecture breakdowns.

---

## 2. Ingestion & Streaming Matrix

| Use Case | AWS Service Choice | Key Keyword Trigger |
| --- | --- | --- |
| **Real-time custom stream processing (Retention up to 365 days)** | [[kinesis]] (Data Streams) | Multi-consumer, sub-second latency, custom processing code |
| **Zero-code streaming delivery to S3 / Redshift / OpenSearch** | [[kinesis]] (Data Firehose) | Micro-batching, direct delivery, automatic Parquet transformation |
| **Open-source Kafka streaming ecosystem** | [[msk-kafka]] (Amazon MSK) | Apache Kafka compatibility, Kafka Connect |
| **Ingesting data from SaaS (Salesforce, ServiceNow)** | [[appflow]] (AWS AppFlow) | No-code SaaS connector, PrivateLink security |
| **Migrating databases with continuous replication** | [[dms-and-sct]] (AWS DMS + CDC) | Heterogeneous database migration, minimal downtime |

---

## 3. Query Engine Matrix: Athena vs Redshift Spectrum vs EMR

| Feature | Amazon Athena | Redshift Spectrum | Amazon EMR |
| --- | --- | --- | --- |
| **Infrastructure** | Fully Serverless | Runs on Redshift cluster nodes | Provisioned EC2 or EMR Serverless |
| **Query Engine** | Trino / Presto | Redshift MPP Engine | Apache Spark / Hive / Presto |
| **Data Location** | Amazon S3 | S3 + Redshift Local Tables | S3 (via EMRFS) or HDFS |
| **Pricing** | $5 per TB scanned | $5 per TB scanned (+ Redshift cluster) | Per-second cluster node pricing |
| **Best For** | Ad-hoc SQL queries on S3 | Joining S3 data lake with Redshift DW tables | Heavy custom Spark processing, machine learning |

---

## 4. Security & Governance Matrix

| Security Goal | Primary AWS Service |
| --- | --- |
| **Column & Row-Level Security on S3 Data Lake** | [[lake-formation]] (AWS Lake Formation) |
| **Automated PII Scanning in S3 (SSNs, Credit Cards)** | [[macie-and-cloudtrail]] (Amazon Macie) |
| **Database Credential Rotation** | [[kms-and-secrets]] (AWS Secrets Manager) |
| **Private S3 access without Internet Gateway** | [[vpc-and-networking]] (S3 Gateway VPC Endpoint) |
| **Centralized Cross-Service Backup & WORM Immutability** | [[aws-backup]] (AWS Backup & Vault Lock) |

---

## 5. Migration & Data Transfer Decision Matrix

```mermaid
graph TD
    MigrationScenario[Migration Scenario?] --> RelationalDB[Relational / DW Migration]
    MigrationScenario --> BulkFiles[Bulk Files / Object Migration]
    MigrationScenario --> ClientUploads[External B2B / Global Ingestion]

    RelationalDB --> HeteroCheck{Heterogeneous?}
    HeteroCheck -->|"Yes (Oracle/SQL Server to Aurora/Redshift)"| SCT_DMS["[[dms-and-sct]] (AWS SCT + AWS DMS CDC)"]
    HeteroCheck -->|"No (Postgres to Aurora Postgres)"| Native_DMS["[[dms-and-sct]] (AWS DMS or Native Logical Replication)"]

    BulkFiles --> BandwidthCheck{Transfer Time > 1-2 Weeks?}
    BandwidthCheck -->|"Yes (> 1-2 Weeks / Offline)"| SnowFam["[[datasync-and-snow]] (AWS Snowball Edge / Snowmobile)"]
    BandwidthCheck -->|"No (Continuous / Network WAN)"| DataSync["[[datasync-and-snow]] (AWS DataSync)"]

    ClientUploads --> UseCaseCheck{Workload Type?}
    UseCaseCheck -->|"B2B Partner SFTP into S3/EFS"| TransferFam["[[datasync-and-snow]] (AWS Transfer Family)"]
    UseCaseCheck -->|"Hybrid Local Cache Backed by S3"| StorageGW["[[datasync-and-snow]] (AWS Storage Gateway)"]
    UseCaseCheck -->|"Accelerate Global Internet Uploads"| S3TA["[[s3-performance]] (S3 Transfer Acceleration)"]
```

| Migration & Transfer Requirement | Recommended Service | Key Keyword / Criteria | Deep Dive Link |
| :--- | :--- | :--- | :--- |
| **Heterogeneous DB schema and code conversion** | **AWS SCT** | Convert PL/SQL, stored procedures, data types | [[dms-and-sct]] |
| **Live database replication & CDC streaming to S3/Kinesis** | **AWS DMS** | Minimal downtime, full load + CDC, `Op` column | [[dms-and-sct]] |
| **Mass data warehouse unload (Teradata/Oracle to Redshift)** | **SCT Data Extraction Agents** | Multi-TB/PB parallel unloads to S3/Snowball | [[dms-and-sct]] |
| **Automated NFS/SMB/HDFS scheduled sync to S3/EFS/FSx** | **AWS DataSync** | Preserves POSIX metadata, 10x faster than rsync | [[datasync-and-snow]] |
| **Large offline physical migration (>10 TB to Petabytes)** | **AWS Snowball Edge** | Network transfer exceeds 1–2 weeks | [[datasync-and-snow]] |
| **Exabyte-scale data center evacuation** | **AWS Snowmobile** | 100 PB per 45ft shipping container truck | [[datasync-and-snow]] |
| **On-premises local file share cache backed by S3** | **AWS Storage Gateway** | Real-time hybrid cached NFS/SMB access | [[datasync-and-snow]] |
| **Legacy SFTP/FTPS file exchange directly into S3/EFS** | **AWS Transfer Family** | Zero client modification, fully managed SFTP | [[datasync-and-snow]] |

---

## 📌 Master Hub Link
Return to main hub: [[index]]
