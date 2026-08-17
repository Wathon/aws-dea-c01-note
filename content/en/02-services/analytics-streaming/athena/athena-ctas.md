---
title: Athena CTAS (Create Table As Select)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - etl
date: 2026-08-17
---

# 🔄 Athena CTAS (Create Table As Select)

- **Category**: Analytics / Lightweight ETL
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/athena/athena-ctas.md)
- **Primary Use Case**: Performing lightweight data transformations (ETL) using SQL to convert, partition, and compress data in S3.
- **Hub Links**: `[[index]]` | `[[athena]]` | `[[glue-etl-jobs]]`

---

## 1. High-Level Summary

**CTAS (Create Table As Select)** is a standard SQL statement supported by Amazon Athena. It allows you to run a query on an existing table and save the output of that query as a **completely new table** in Amazon S3, automatically adding the new table to the AWS Glue Data Catalog.

This makes Athena a powerful tool for **Lightweight ETL** (Extract, Transform, Load) operations without needing to provision Spark clusters or write complex Python/Scala code.

---

## 2. Core Capabilities & Use Cases

### 1. Data Format Conversion (CSV $\rightarrow$ Parquet)
If you receive raw CSV data, querying it repeatedly is slow and expensive. You can use a CTAS query to select the CSV data and write it out as compressed Parquet.

```sql
CREATE TABLE new_parquet_table
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://my-bucket/optimized-data/'
) AS
SELECT * FROM raw_csv_table;
```

### 2. Partitioning Data
You can restructure unpartitioned data into a partitioned directory structure in S3 to optimize future queries.

```sql
CREATE TABLE partitioned_sales
WITH (
  format = 'PARQUET',
  partitioned_by = ARRAY['year', 'month']
) AS
SELECT order_id, total, year, month FROM raw_sales;
```

### 3. Data Cleansing & Aggregation
You can filter out null records, join tables, or pre-calculate daily aggregations, saving the cleaned/aggregated dataset as a new table for business analysts to query quickly.

---

## 3. CTAS vs. AWS Glue ETL

When should you use Athena CTAS vs. AWS Glue?

| Feature | Athena CTAS | AWS Glue ETL (Spark) |
| :--- | :--- | :--- |
| **Skill Required** | Standard SQL | Python (PySpark) / Scala |
| **Complexity Limit** | Simple joins, filters, format conversion | Complex, multi-step transformations, ML transforms |
| **Execution Limit** | Fails if query takes > 30 minutes | Can run for hours (supports massive datasets) |
| **Cost** | Charged per TB scanned | Charged per DPU-hour (Compute time) |

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Convert CSV data to Parquet using only SQL without managing servers"** $\rightarrow$ **Use Athena CTAS**.
> - **"Create a subset of a massive table for analysts to query faster and cheaper"** $\rightarrow$ **Use an Athena CTAS query with aggregation**.
> - **"Transform data in S3 but the team only knows SQL"** $\rightarrow$ **Use Athena CTAS**.

> [!WARNING]
> **Exam Trap**:
> - Do not use Athena CTAS for complex ETL logic that requires thousands of transformations or takes hours to process. For heavy ETL, the exam answer will be **AWS Glue ETL** or **Amazon EMR**.

---

## 📌 Related Notes
- `[[athena]]` — Athena Overview
- `[[glue-etl-jobs]]` — Heavyweight Spark ETL
- `[[athena-performance]]` — Why Parquet and partitioning matter
