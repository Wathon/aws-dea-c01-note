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

    Structured --> RDS[[RDS / Aurora]]
    Analytics --> Redshift[[Amazon Redshift]]
    SemiStructured --> DynamoDB[[Amazon DynamoDB]]
    DataLake --> S3[[Amazon S3]]
```

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

---

## 📌 Master Hub Link
Return to main hub: [[index]]
