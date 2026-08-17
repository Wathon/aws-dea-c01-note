---
title: AWS Glue Data Quality
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - data-quality
date: 2026-08-15
---

# ✅ AWS Glue Data Quality

- **Category**: Analytics / Data Governance
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/glue/glue-data-quality)
- **Primary Use Case**: Automated Data Validation, Rules-based Anomaly Detection, Halting Bad Pipelines.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[data-validation-and-profiling]]`

---

## 1. High-Level Summary

**AWS Glue Data Quality** allows Data Engineers to measure and monitor the quality of data residing in their data lakes and pipelines. Instead of writing complex, custom PySpark code to assert data correctness, you use a declarative language called **DQDL (Data Quality Definition Language)**. This service can automatically evaluate data at rest in the Data Catalog or in transit within a Glue ETL Job.

---

## 2. Core Capabilities

### 1. Data Quality Definition Language (DQDL)
DQDL is a purpose-built language to express rules easily. Example rules include:
- `Completeness "email" > 0.98` (Ensure 98% of rows have an email address).
- `IsUnique "user_id"` (Ensure no duplicate IDs).
- `ColumnValues "status" in ["ACTIVE", "INACTIVE", "PENDING"]`.

### 2. Integration with Glue ETL Jobs
When integrated into a Glue ETL pipeline, Data Quality acts as a gatekeeper. You can configure the job to:
- **Publish metrics** to CloudWatch.
- **Fail the job** immediately if critical rules fail (preventing bad data from reaching the data warehouse).
- **Quarantine bad records** by routing them to a specific "dead-letter" S3 prefix for manual review, while allowing good records to continue.

### 3. Data Catalog Evaluation
You can also run Data Quality rules directly against tables in the **[[glue-data-catalog]]** on a schedule to monitor the health of data at rest over time.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Need to validate that data in a pipeline does not contain null values without writing custom code"** $\rightarrow$ **Use AWS Glue Data Quality and write DQDL rules**.
> - **"Halt the ETL pipeline if the completeness of a critical column drops below 95%"** $\rightarrow$ **Configure AWS Glue Data Quality to fail the job upon rule failure**.
> - **"Route rows failing validation to a quarantine S3 bucket while letting valid rows proceed"** $\rightarrow$ **Use AWS Glue Data Quality to split the dataset based on evaluation results**.

---

## 📌 Related Notes
- `[[glue]]` — AWS Glue Overview
- `[[glue-etl-jobs]]` — Integration with Glue ETL Jobs
- `[[data-validation-and-profiling]]` — Concept: Data Validation vs Profiling
