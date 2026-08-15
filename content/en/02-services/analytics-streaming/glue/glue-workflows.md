---
title: AWS Glue Workflows
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - orchestration
date: 2026-08-15
---

# 🛤️ AWS Glue Workflows

- **Category**: Analytics / Orchestration
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-workflows.md)
- **Primary Use Case**: Orchestrating and scheduling multiple Glue Crawlers, Glue Jobs, and triggers.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[step-functions]]` | `[[mwaa-airflow]]`

---

## 1. High-Level Summary

**AWS Glue Workflows** allow you to create and visualize complex extract, transform, and load (ETL) activities involving multiple crawlers, jobs, and triggers. While services like **AWS Step Functions** or **Amazon MWAA (Apache Airflow)** can orchestrate tasks across the entire AWS ecosystem, **Glue Workflows** is purpose-built and scoped *specifically* for orchestrating components within AWS Glue.

---

## 2. Core Capabilities

### 1. Triggers
Workflows use triggers to start and coordinate execution. A trigger can be:
- **On-Demand**: Started manually.
- **Schedule-based**: Started at a specific time (e.g., cron expression).
- **Event-based**: Started when an EventBridge event occurs (e.g., a file lands in an S3 bucket).
- **Conditional**: Started only if previous jobs or crawlers in the workflow succeed, fail, or meet certain conditions.

### 2. Directed Acyclic Graphs (DAGs)
- Glue Workflows automatically generate a visual DAG representation of your ETL pipeline.
- You can monitor the entire workflow's progress in the AWS Management Console, seeing exactly which job succeeded, failed, or is currently running.

### 3. State Management
- Workflows can share state between jobs. You can define workflow properties (key-value pairs) that are accessible to every Glue job within the workflow. If Job A calculates a dynamic partition date, it can pass that value to Job B.

---

## 3. Glue Workflows vs. Step Functions vs. MWAA

| Feature | AWS Glue Workflows | AWS Step Functions | Amazon MWAA (Airflow) |
| :--- | :--- | :--- | :--- |
| **Scope** | Native Glue components ONLY (Jobs, Crawlers) | AWS-wide ecosystem (Lambda, ECS, EMR, SNS, etc.) | Cloud-agnostic / Multi-cloud ecosystem (Python DAGs) |
| **Complexity** | Simple ETL orchestration | Complex state machines, branching, human-in-the-loop | Complex data pipelines, custom operators |
| **Setup Overhead** | None (Built into Glue) | Low (JSON/ASL definitions) | High (Requires provisioning Airflow environments) |

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Need to orchestrate a Glue Crawler, followed by a Glue ETL job, followed by another Crawler, without managing external infrastructure"** $\rightarrow$ **AWS Glue Workflows**.
> - **"Need to trigger a Glue workflow automatically when a file lands in S3"** $\rightarrow$ **Use Amazon EventBridge to trigger the Glue Workflow**.
> - **"Need to orchestrate an AWS Batch job, an EMR cluster, and a Glue job"** $\rightarrow$ *Do not use Glue Workflows. Use **AWS Step Functions** or **MWAA***.

---

## 📌 Related Notes
- `[[step-functions]]` — General AWS orchestration
- `[[mwaa-airflow]]` — Managed Apache Airflow for complex data pipelines
