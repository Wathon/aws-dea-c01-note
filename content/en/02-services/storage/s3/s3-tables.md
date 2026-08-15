---
title: Amazon S3 Tables
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/s3
  - apache-iceberg
  - analytics
date: 2026-08-07
---

# 📊 Amazon S3 Tables

- **Category**: Tabular Object Storage & Data Lake Architecture
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/storage/s3/s3-tables.md)
- **Primary Use Case**: Managed Apache Iceberg Tables, Automated Data Lake Maintenance, High-Throughput ACID Transactions
- **Slide Reference**: Pages 77–138 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[s3]] | [[athena]] | [[lake-formation]] | [[glue]]

---

## 1. High-Level Summary

**Amazon S3 Tables** is a purpose-built storage bucket type designed specifically for storing tabular data formatted as **Apache Iceberg** tables. It is the first object storage optimized specifically for table-based analytics, delivering up to **3x faster query performance** and **10x higher transactions per second (TPS)** compared to traditional general-purpose S3 buckets. S3 Tables automates background table optimization (compaction, snapshot expiration, unreferenced file pruning), removing the operational burden of managing Apache Iceberg data lakes manually.

---

## 2. Architecture & Hierarchy

```mermaid
graph TD
    subgraph S3Tables["Amazon S3 Tables Architecture"]
        TB["S3 Table Bucket (e.g. arn:aws:s3tables:us-east-1:123456789012:bucket/analytics-db)"]

        subgraph NamespaceLayer["Namespace Layer"]
            NS1["Namespace: sales"]
            NS2["Namespace: marketing"]
        end

        subgraph TableLayer["Table Layer (Apache Iceberg)"]
            T1["Table: transactions"]
            T2["Table: customers"]
            T3["Table: campaigns"]
        end

        subgraph Maintenance["Automated Background Maintenance"]
            COMP["Automatic File Compaction (Merges Small Parquet Files)"]
            SNAP["Automatic Snapshot Expiration"]
            ORPH["Orphan / Unreferenced File Pruning"]
        end
    end

    TB --> NS1
    TB --> NS2
    NS1 --> T1
    NS1 --> T2
    NS2 --> T3
    T1 -.-> COMP
    T1 -.-> SNAP
    T1 -.-> ORPH
```

### Table Bucket Hierarchy

1. **Table Bucket**: A dedicated, specialized S3 bucket type scoped exclusively for table storage (`s3tables`).
2. **Namespace**: A logical grouping container for tables within a Table Bucket (equivalent to a schema or database in traditional relational databases).
3. **Table**: An individual **Apache Iceberg** table stored as Parquet files with Iceberg metadata, manifests, and snapshot histories.

---

## 3. Core Features & Capabilities

### 1. Automated Table Maintenance (Zero Operational Overhead)

In standard S3 buckets, Apache Iceberg tables accumulate millions of small data files and obsolete metadata snapshots over time, degrading query performance unless manual Glue ETL / EMR compaction scripts are run.  
**S3 Tables automatically performs background optimization**:

- **Automatic File Compaction**: Merges small Parquet data files into optimal sizes ($128\text{ MB}$–$512\text{ MB}$) continuously in the background without affecting active queries.
- **Snapshot Expiration**: Automatically purges old Iceberg snapshots according to retention policies.
- **Unreferenced File Cleanup (Vacuum)**: Identifies and deletes orphan data files not attached to active Iceberg metadata manifests.

### 2. High-Concurrency ACID Transactions & Performance

- **10x Higher Transactions per Second (TPS)**: Optimizes metadata locks and commit operations, supporting thousands of concurrent writes/updates without commit conflict failures.
- **Up to 3x Faster Query Performance**: Built-in metadata indexing and automated layout optimization accelerate query planning in engines like [[athena]], [[redshift]], and [[emr]] Spark.

### 3. Integrated Governance with AWS Lake Formation

- S3 Tables natively integrates with **AWS Lake Formation**.
- Fine-grained access control can be enforced down to the **column-level**, **row-level**, and **cell-level** using Lake Formation Tag-Based Access Control (LF-TBAC).

### 4. Built-in S3 Intelligent-Tiering Integration

- **Native Storage Tiering**: Amazon S3 Tables use **S3 Intelligent-Tiering** as their built-in storage foundation for object data files (Parquet).
- **Automated Cost Optimization**:
  - Automatically moves data files between access tiers based on real-time query patterns:
    - **Frequent Access Tier**: Default for newly written objects and actively queried partitions.
    - **Infrequent Access Tier**: Automatically moves files not accessed for 30 consecutive days (saves up to 40%).
    - **Archive Instant Retrieval Tier**: Automatically moves files not accessed for 90 consecutive days (saves up to 68%).
  - **Zero Retrieval Fees & Millisecond Performance**: Maintains consistent millisecond retrieval performance across all access tiers without retrieval fee penalties, allowing historical table partitions to age out automatically while remaining instantly queryable.
  - **Zero Lifecycle Rule Overhead**: Fully managed by S3 Tables without needing custom S3 Lifecycle rules.

### 5. Table Replication (CRR & SRR)

- **Cross-Region (CRR) & Same-Region Replication (SRR)**: S3 Tables support asynchronous replication of Table Buckets across AWS Regions or within the same Region.
- **Iceberg Catalog & Data Sync**: Replicates both underlying Parquet data files AND Apache Iceberg table metadata/snapshot histories to destination table buckets while maintaining transactional consistency.
- **Use Cases**: Disaster recovery, multi-region analytical data distribution, compliance data residency, and low-latency local querying for global teams.

---

## 4. Security & Access Control Architecture

### 1. Multi-Layer Security Model

```mermaid
graph TD
    subgraph SecurityLayer["Security Layer Structure"]
        Auth["IAM & S3 Table Resource Policies (s3tables:*)"]
        Network["VPC PrivateLink Endpoints (com.amazonaws.region.s3tables)"]
        Gov["AWS Lake Formation (Column/Row/Cell Security & LF-TBAC)"]
        Encrypt["Encryption at Rest (SSE-S3 / SSE-KMS) & TLS In Transit"]
    end

    Auth --> Network
    Network --> Gov
    Gov --> Encrypt
```

### 2. Detailed Security Breakdown

- **S3 Table Resource Policies**: JSON access control policies applied at the Table Bucket or Namespace level (`s3tables:CreateTable`, `s3tables:GetTableData`, `s3tables:PutTableData`).
- **AWS Lake Formation Governance**: Enforces fine-grained row-level filtering, column masking, and cell-level security using Tag-Based Access Control (LF-TBAC).
- **Encryption at Rest & In Transit**: Data files and metadata manifests are encrypted at rest using SSE-S3 or SSE-KMS. All network communications enforce HTTPS/TLS 1.3.
- **VPC Endpoints (PrivateLink)**: Private connectivity from Amazon VPCs to S3 Tables over AWS PrivateLink endpoints (`com.amazonaws.<region>.s3tables`), preventing data lake traffic from traversing the public internet.

| Feature                 | S3 Standard                  | S3 Express One Zone             | Amazon S3 Tables                                |
| ----------------------- | ---------------------------- | ------------------------------- | ----------------------------------------------- |
| **Primary Format**      | General Unstructured Objects | High-Throughput Objects         | **Apache Iceberg Tabular Data**                 |
| **Latency**             | Double-digit ms              | **Single-digit ms (Single AZ)** | Millisecond analytics I/O                       |
| **Compaction**          | Manual (Glue/Athena CTAS)    | Manual                          | **Fully Automatic Background Compaction**       |
| **Metadata Management** | Object Key Prefixes          | Object Key Prefixes             | **Native Iceberg Catalog & Snapshot Pruning**   |
| **Ideal Query Engines** | Athena, Glue, Redshift, EMR  | SageMaker, Spark Checkpoints    | **Athena, Spark, Redshift, Snowflake, Iceberg** |

---

## 5. Analytics Ecosystem Integration

Amazon S3 Tables seamlessly integrates with both AWS native services and open-source analytical tools via standard Apache Iceberg REST catalog interfaces:

- **[[athena]]**: Query S3 Tables directly using standard ANSI SQL (`SELECT`, `INSERT`, `UPDATE`, `MERGE INTO`).
- **AWS Glue Data Catalog**: S3 Tables automatically register their schemas in the AWS Glue Data Catalog.
- **[[redshift]]**: Query S3 Tables using Redshift Spectrum or Serverless zero-copy integration.
- **[[emr]] & Apache Spark**: Read and write Iceberg tables using `pyspark` or Spark SQL with native pushdown optimizations.
- **Third-Party Engines**: Snowflake, Starburst/Trino, Databricks via standard Apache Iceberg endpoints.

---

## 6. DEA-C01 Exam Tips & Decision Triggers

> [!IMPORTANT]
> **Key Exam Decision Rules**:
>
> - **Store Apache Iceberg tables in S3 with automated file compaction & snapshot maintenance**: Choose **Amazon S3 Tables**.
> - **High-concurrency streaming ingestion into Apache Iceberg on S3**: Choose **Amazon S3 Tables** (provides 10x higher commit TPS).
> - **Eliminate manual Glue ETL compaction scripts for data lake tables**: Migrate tables to **Amazon S3 Tables**.
> - **Automatic cost optimization for aging table partitions without retrieval fees**: S3 Tables automatically use **S3 Intelligent-Tiering** for underlying data objects.
> - **Row- and Column-level security on S3 Tables**: Enforce via **AWS Lake Formation integration**.
> - **Replicate Apache Iceberg tables across AWS regions for DR & compliance**: Enable **S3 Tables Cross-Region Replication (CRR)** (replicates data files + Iceberg catalog metadata).
> - **Private connectivity to S3 Tables from VPC without public internet routing**: Use **AWS PrivateLink VPC Endpoints (`com.amazonaws.<region>.s3tables`)**.

---

## 📌 Related Notes

- [[s3]] — Amazon S3 Overview & Storage Classes
- [[s3-performance]] — S3 Request Limits & Compaction Techniques
- [[athena]] — Querying Iceberg & S3 Data Lakes
- [[glue]] — Glue Data Catalog & ETL Compaction
- [[lake-formation]] — Fine-Grained Governance for Data Lakes
