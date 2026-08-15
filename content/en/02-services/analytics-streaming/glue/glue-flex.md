---
title: AWS Glue Flex Execution Class
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - cost-optimization
date: 2026-08-15
---

# 💰 AWS Glue Flex Execution Class

- **Category**: Analytics / Cost Optimization
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-flex.md)
- **Primary Use Case**: Cost reduction for non-urgent, non-time-sensitive data integration workloads.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[glue-etl-jobs]]`

---

## 1. High-Level Summary

**AWS Glue Flex** is a job execution class that allows you to reduce the cost of your non-urgent data integration workloads by up to **35%**. Similar to Amazon EC2 Spot Instances, Glue Flex uses spare compute capacity in AWS. 

Because it uses spare capacity, start times and job completion times can vary, and AWS may reclaim the compute resources if capacity is needed elsewhere. Therefore, Glue Flex is strictly designed for **non-time-sensitive workloads**.

---

## 2. Standard vs. Flex Execution Class

| Feature | Standard Execution Class | Flex Execution Class |
| :--- | :--- | :--- |
| **Cost** | Baseline cost | **Up to 35% cheaper** |
| **Start Time** | Fast and predictable | Variable (can be delayed based on capacity) |
| **Job Interruption** | Highly unlikely | **Possible** (Compute resources can be reclaimed) |
| **Ideal Workloads** | Time-sensitive SLAs, streaming, critical daily reports | Nightly batch jobs, ad-hoc analysis, development/testing, historical backfills |
| **Supported Worker Types** | `G.1X`, `G.2X`, `G.4X`, `G.8X`, `G.025X` | `G.1X`, `G.2X` |

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Cost-optimize non-urgent, nightly batch ETL jobs where predictable start times are not required"** $\rightarrow$ **Use the AWS Glue Flex execution class**.
> - **"Save up to 35% on Glue PySpark jobs running historical backfills"** $\rightarrow$ **AWS Glue Flex**.
> - **"A job is mission-critical and must finish exactly at 8:00 AM every day"** $\rightarrow$ **DO NOT use Glue Flex; use the Standard execution class**.

---

## 📌 Related Notes
- `[[glue-etl-jobs]]` — AWS Glue ETL Jobs & Worker Types
- `[[cost-management]]` — General AWS Cost Optimization
