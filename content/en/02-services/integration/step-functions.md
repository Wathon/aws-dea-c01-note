---
title: AWS Step Functions
type: aws-service
category: Integration
tags:
  - aws/service
  - dea-c01
  - integration/step-functions
date: 2026-07-28
---

# 🔄 AWS Step Functions (Visual Workflow Orchestration)

- **Category**: Application Integration / Orchestration
- **Primary Use Case**: Serverless visual state machine orchestration for multi-step data pipelines and ETL workflows.
- **Slide Reference**: Pages 526–529 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
AWS Step Functions is a low-code visual workflow service that allows data engineers to build distributed applications, automate processes, and orchestrate serverless data pipelines using AWS services (Lambda, Glue, EMR, Athena, ECS, DynamoDB, SQS, SNS).

---

## 2. Standard vs Express Workflows

| Feature | Standard Workflows | Express Workflows |
| --- | --- | --- |
| **Max Execution Time** | **Up to 1 year** | **Up to 5 minutes** |
| **Execution Rate** | Up to 2,000 / sec | Over 100,000 / sec |
| **Pricing Model** | State Transitions | Execution count & duration |
| **Ideal Use Case** | Long-running ETL pipelines, human approval flows | High-volume streaming event processing, micro-batching |

---

## 3. Error Handling & Retry Logic
Step Functions natively provides error handling constructs in JSON state definitions:
- **`Retry`**: Automatically retry failed tasks with exponential backoff (`IntervalSeconds`, `BackoffRate`, `MaxAttempts`).
- **`Catch`**: Catch specific error types (`States.ALL`, `Glue.ConcurrentRunsExceededException`) and fallback to a designated error handling state or notification step!

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> - **Orchestrating Lambda, Glue, and Redshift without custom polling code**: Use **AWS Step Functions**.
> - **Automated Retries on Transient Failures**: Configure `Retry` blocks inside Step Functions task definitions to handle rate limits or API throttles automatically.

---

## 📌 Related Notes
- [[mwaa-airflow]] — Step Functions vs Managed Airflow (MWAA)
- [[glue]] — Glue job execution in Step Functions
- [[lambda]] — Lambda task orchestration
