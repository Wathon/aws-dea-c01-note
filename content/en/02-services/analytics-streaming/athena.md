---
title: Amazon Athena
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
date: 2026-07-28
---

# 🏛️ Amazon Athena (Serverless Interactive SQL)

- **Category**: Analytics
- **Primary Use Case**: Interactive ad-hoc SQL queries on Amazon S3 data lakes using standard ANSI SQL.
- **Slide Reference**: Pages 365–382 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-2-data-store-management]]

---

## 1. High-Level Summary
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run ($5 per TB scanned).

---

## 2. Key Architecture & Features

### Integration with Glue Data Catalog
- Athena relies on table metadata stored in the **AWS Glue Data Catalog** (or Apache Hive metastore) to parse S3 files into structured tables.

### Optimization Techniques (Reducing Scanned Data = Lower Cost & Higher Speed)
1. **Columnar Data Formats**: Convert CSV/JSON into **Apache Parquet** or **Apache ORC** (scans only required columns).
2. **Compression**: Compress data with **Snappy**, **Zstd**, or **Gzip**.
3. **Partitioning & Partition Projection**:
   - Partitioning by date/category (`s3://bucket/year=2026/month=07/`).
   - **Partition Projection**: Calculates partition locations dynamically from table properties instead of running expensive `MSCK REPAIR TABLE` or Glue Crawlers!

### Advanced Athena Capabilities
- **CTAS (Create Table As Select)**: Saves query results as a new partitioned, compressed Parquet table in S3.
- **Athena Federated Query**: Query data across relational, non-relational, object, and custom data sources (DynamoDB, Redshift, MySQL, CloudWatch Logs) using Lambda connectors!
- **Athena Workgroups**: Separate query execution environments for cost allocation, enforcing per-query scan limits, and managing IAM permissions.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Rules for Athena**:
> - **Cost Optimization**: To reduce Athena cost, convert data to **Parquet/ORC**, compress with **Snappy**, and apply **Partitioning**.
> - **High-Frequency Partition Addition**: Use **Partition Projection** to bypass Glue Crawler runtime and metadata limits for fast-growing partitioned data lakes.
> - **Query Non-S3 Stores via SQL**: Use **Athena Federated Query**.

---

## 📌 Related Notes
- [[glue]] — Glue Catalog metadata for Athena
- [[s3]] — S3 object storage queried by Athena
- [[redshift]] — Athena (Ad-hoc S3 SQL) vs Redshift (Enterprise DW)
