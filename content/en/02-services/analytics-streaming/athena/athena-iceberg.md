---
title: Athena ACID Transactions (Apache Iceberg)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - iceberg
date: 2026-08-17
---

# 🧊 Athena ACID Transactions (Apache Iceberg)

- **Category**: Analytics / Data Lake Formats
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/athena/athena-iceberg)
- **Primary Use Case**: Enabling row-level updates, deletes, and time-travel queries on S3 data lakes with ACID guarantees.
- **Hub Links**: `[[index]]` | `[[athena]]` | `[[domain-2-data-store-management]]`

---

## 1. High-Level Summary

By default, Amazon S3 and standard Athena tables are **append-only** or **overwrite**. Updating or deleting a single row in a 10 GB Parquet file traditionally requires rewriting the entire file.

Amazon Athena supports **Apache Iceberg**, an open table format for huge analytic datasets that brings database-like features to S3 data lakes. With Iceberg, Athena can perform **ACID (Atomicity, Consistency, Isolation, Durability) transactions**.

---

## 2. Core Capabilities

### 1. Row-Level Operations (UPDATE, DELETE, MERGE)
Instead of rewriting entire partitions just to fix a single bad record or delete a user's data (e.g., for GDPR compliance), Iceberg allows you to run standard SQL `UPDATE`, `DELETE`, and `MERGE INTO` statements directly in Athena.

### 2. Time-Travel Queries
Iceberg maintains a transaction log of every change made to the table. This allows you to query the table *as it existed at a specific point in time* in the past.
- **Exam Tip**: Useful for auditing, rolling back accidental deletions, or reproducing machine learning models on historical data.

```sql
-- Query data as it looked yesterday
SELECT * FROM iceberg_table FOR SYSTEM_TIME AS OF (current_timestamp - interval '1' day);
```

### 3. Concurrent Writers (ACID Guarantees)
If multiple AWS Glue jobs, EMR clusters, and Athena users try to write to the same S3 table simultaneously, Iceberg guarantees that readers will never see partial or corrupted data (Isolation) and that concurrent writes won't corrupt the table (Consistency).

### 4. Schema Evolution
You can safely add, drop, rename, or reorder columns without having to rewrite underlying data files or breaking downstream queries.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Need to perform row-level UPDATEs and DELETEs on S3 data lake for GDPR compliance"** $\rightarrow$ **Use Apache Iceberg with Athena**.
> - **"Need to run 'time-travel' queries to see what the data looked like 3 days ago"** $\rightarrow$ **Use Apache Iceberg table formats**.
> - **"Concurrent writers causing data corruption in S3"** $\rightarrow$ **Migrate the table format to Apache Iceberg for ACID transactions**.

---

## 📌 Related Notes
- `[[athena]]` — Athena Overview
- `[[athena-performance]]` — General performance tuning
- `[[glue-etl-jobs]]` — You can also use Glue with Iceberg
