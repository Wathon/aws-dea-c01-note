---
title: AWS Glue Crawlers
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - crawler
date: 2026-08-15
---

# 🕷️ AWS Glue Crawlers

- **Category**: Analytics / Automated Schema Discovery
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-crawlers.md)
- **Primary Use Case**: Automatic Schema Inference, Partition Detection, and Data Catalog Population.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[glue-data-catalog]]` | `[[athena]]`

---

## 1. High-Level Summary

**AWS Glue Crawlers** automatically scan data stores (such as Amazon S3, Amazon RDS, DynamoDB, and Redshift), infer their schema, determine their data format (e.g., Parquet, JSON, CSV), and create corresponding metadata tables in the **[[glue-data-catalog]]**. Crawlers automate the tedious process of writing DDL (Data Definition Language) statements to create tables for data lakes.

---

## 2. Core Capabilities

### 1. Built-in and Custom Classifiers
- Crawlers use **Classifiers** to identify the data format. AWS Glue provides built-in classifiers for JSON, CSV, Parquet, ORC, Avro, and more.
- If a built-in classifier cannot recognize a proprietary format, you can create a **Custom Classifier** using Grok patterns.

### 2. Automated Partition Detection
- Crawlers automatically recognize Hive-style S3 prefixes (e.g., `s3://bucket/data/year=2026/month=08/`) and add them as partitions to the Data Catalog table.
- This prevents the need to manually run `MSCK REPAIR TABLE` in Athena every time new partitioned data arrives.

### 3. Include and Exclude Patterns
- By default, a crawler scans everything under the target S3 path. You can optimize this by specifying **Exclude Patterns** (e.g., `**/*.tmp` or `**/archive/**`) to prevent the crawler from scanning irrelevant or temporary files, which saves time and money.

### 4. IAM Roles & Security
- The crawler must be assigned an **IAM Role** that has `s3:GetObject` and `s3:ListBucket` permissions for the target S3 path.
- Without proper IAM permissions, the crawler will fail silently or return zero tables.

### 5. Handling Schema Evolution (Schema Drift)
Data formats change over time. Glue Crawlers can be configured to handle schema drift automatically:
- **Add new columns**: If new columns appear in the source data, the crawler can append them to the Data Catalog table definition.
- **Table Definition Updates**: You must explicitly configure the crawler setting: `Update the table definition in the data catalog` for it to adapt to schema changes.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Automate the discovery of new partitions added to S3 daily"** $\rightarrow$ **Schedule an AWS Glue Crawler**.
> - **"Source data occasionally adds new columns. How to ensure Athena can query them?"** $\rightarrow$ **Run a Glue Crawler with 'Update the table definition in the data catalog' enabled**.
> - **"Data in S3 is in a proprietary log format that standard tools cannot parse"** $\rightarrow$ **Create a Custom Classifier using Grok patterns and attach it to the Glue Crawler**.
> - **"Crawler is scanning temporary files and taking too long"** $\rightarrow$ **Use Exclude Patterns in the crawler definition**.
> - **"Crawler finishes successfully but finds 0 tables"** $\rightarrow$ **Check the IAM Role permissions for `s3:GetObject`**.

---

## 📌 Related Notes
- `[[glue]]` — AWS Glue Overview
- `[[glue-data-catalog]]` — Glue Data Catalog Metastore
- `[[data-modeling-and-partitioning]]` — S3 Partition Structures
- `[[athena]]` — Querying Discovered Data
