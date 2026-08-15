---
title: AWS Glue ETL Jobs & DynamicFrames
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - etl
  - spark
date: 2026-08-15
---

# ⚙️ AWS Glue ETL Jobs & DynamicFrames

- **Category**: Analytics / Distributed Processing
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-etl-jobs.md)
- **Primary Use Case**: Serverless Apache Spark Data Transformations, Incremental Data Processing, Handling Semi-Structured Data.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[emr]]` | `[[domain-3-data-processing]]`

---

## 1. High-Level Summary

**AWS Glue ETL Jobs** execute data transformation scripts in a serverless Apache Spark environment (PySpark or Scala) or a simple Python shell. Unlike **[[emr]]**, where you must provision, tune, and terminate clusters, AWS Glue provisions worker nodes instantly, allowing Data Engineers to focus purely on the transformation logic.

---

## 2. Core Concepts for DEA-C01

### 1. Glue DynamicFrames vs. Spark DataFrames
While standard Apache Spark uses DataFrames that require a strict, rigid schema, AWS Glue introduces **DynamicFrames**.
- **DynamicFrames** do not require a pre-defined schema. They evaluate the schema row-by-row on the fly.
- This is incredibly useful for **semi-structured JSON** data where fields might be missing, or where a column might be an `Integer` in one row and a `String` in another.
- Instead of throwing a schema mismatch error (like Spark DataFrames do), DynamicFrames create a "Choice" type that safely holds both formats, allowing you to resolve the ambiguity later using the `ResolveChoice` transform.

### 2. Job Bookmarks (Incremental Processing)
- **Glue Job Bookmarks** track which data has already been processed in previous job runs.
- When a Glue Job runs, it will only process the **new files** added to S3 since the last run.
- **Exam Tip**: This is the built-in, no-code mechanism for achieving incremental data processing without maintaining custom state tracking in DynamoDB or passing timestamps manually.

### 3. Worker Types (Capacity Planning)
AWS Glue provides different worker types based on the workload:
- **`G.1X`**: 1 DPU (Data Processing Unit), 4 vCPU, 16 GB memory. Good for standard Spark ETL.
- **`G.2X`**: 2 DPU, 8 vCPU, 32 GB memory. Recommended for memory-intensive workloads, heavy shuffles, or ML transforms.
- **`G.025X`**: 0.25 DPU. Used for small Python shell jobs or very light streaming workloads.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Process nested, semi-structured JSON with changing data types without failing"** $\rightarrow$ **Use AWS Glue DynamicFrames and `ResolveChoice`**.
> - **"Process only the newly arrived S3 files without maintaining custom tracking logic"** $\rightarrow$ **Enable AWS Glue Job Bookmarks**.
> - **"Need to run a serverless Spark job to aggregate 10 TB of data with heavy joins"** $\rightarrow$ **Use AWS Glue ETL Jobs with `G.2X` workers for memory-intensive processing**.

---

## 📌 Related Notes
- `[[glue]]` — AWS Glue Overview
- `[[glue-databrew]]` — Visual ETL alternatives
- `[[emr]]` — Amazon EMR (Cluster-based Spark alternative)
