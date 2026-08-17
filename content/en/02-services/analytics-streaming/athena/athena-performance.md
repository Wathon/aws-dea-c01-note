---
title: Athena Performance & Optimization
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - performance
date: 2026-08-17
---

# 🚀 Athena Performance & Optimization

- **Category**: Analytics / Optimization
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/athena/athena-performance)
- **Primary Use Case**: Reducing query costs and improving query latency by limiting the amount of data scanned from S3.
- **Hub Links**: `[[index]]` | `[[athena]]` | `[[s3]]`

---

## 1. High-Level Summary

Amazon Athena charges **$5 per Terabyte (TB) of data scanned**. Therefore, performance optimization in Athena is directly tied to **cost optimization**. Data Engineers must structure S3 data in a way that allows Athena to read *only* the data necessary for the query, ignoring irrelevant data. 

The core triad of Athena optimization is: **Columnar Formats**, **Compression**, and **Partitioning**.

---

## 2. The Core Optimization Techniques

### 1. Columnar Data Formats (Parquet & ORC)
- Standard formats like CSV and JSON are **row-based**. If a query only needs 2 columns out of a 100-column CSV file, Athena still has to scan the entire row (scanning 100% of the data).
- **Apache Parquet** and **Apache ORC** are **columnar**. Athena can fetch *only* the specific columns requested in the `SELECT` statement, ignoring the rest.
- **Exam Tip**: Always convert CSV/JSON to Parquet or ORC using AWS Glue to drastically reduce Athena scan costs.

### 2. Compression (Snappy / Zstd)
- Compressing data reduces the file size in S3, which means Athena scans fewer megabytes, directly lowering the cost and speeding up network I/O.
- **Snappy** is the default and recommended compression format for Parquet because it is highly splittable (Athena can read parts of the file in parallel).
- **Gzip** is less ideal for big data because it is not easily splittable unless used in specific configurations.

### 3. Data Partitioning
- Partitioning groups data into separate S3 folders based on a column's value (e.g., `s3://bucket/sales/year=2026/month=08/`).
- When a query includes a `WHERE year = '2026'` clause, Athena skips scanning any folders for other years.
- **Glue Crawler Integration**: If you add new partitions to S3, you must either run a Glue Crawler to update the catalog, or manually run `MSCK REPAIR TABLE` in Athena.

---

## 3. Advanced: Partition Projection

As a data lake grows to contain hundreds of thousands of partitions (e.g., hourly partitions over several years), running `MSCK REPAIR TABLE` or querying the Glue Data Catalog for partition metadata becomes extremely slow and expensive.

**Partition Projection** is a feature in Athena that calculates partition locations *dynamically* in-memory based on rules defined in the table properties, entirely bypassing the Glue Data Catalog metadata lookup.

### Benefits of Partition Projection:
- **No need to run `MSCK REPAIR TABLE`** when new partitions are added.
- **No need to run Glue Crawlers** to discover new daily/hourly partitions.
- **Massively speeds up queries** on highly partitioned tables.

```sql
-- Example of configuring Partition Projection in table properties
TBLPROPERTIES (
  'projection.enabled' = 'true',
  'projection.date.type' = 'date',
  'projection.date.range' = '2020-01-01,NOW',
  'projection.date.format' = 'yyyy-MM-dd',
  'storage.location.template' = 's3://my-bucket/data/${date}/'
)
```

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Reduce Athena cost and improve query performance"** $\rightarrow$ **Convert data to Parquet/ORC and compress with Snappy**.
> - **"Queries are failing due to a high number of partitions"** or **"MSCK REPAIR TABLE is taking too long"** $\rightarrow$ **Enable Partition Projection**.
> - **"Highly partitioned table with predictable patterns (like hourly/daily dates)"** $\rightarrow$ **Use Partition Projection**.

---

## 📌 Related Notes
- `[[athena]]` — Athena Overview
- `[[glue-crawlers]]` — Automating partition discovery
- `[[s3-performance]]` — S3 Prefix limits and optimization
