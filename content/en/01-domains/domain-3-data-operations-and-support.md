---
title: "Domain 3: Data Operations and Support"
type: domain
tags:
  - domain/operations
  - dea-c01
  - exam-prep
date: 2026-07-28
---

# ⚙️ Domain 3: Data Operations and Support (Weight: 22%)

- **Domain ID**: Domain 3
- **Focus**: Automating data pipelines, monitoring data quality, troubleshooting errors, maintaining system performance, and cost management.
- **Hub Links**: [[index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 3.1: Automate data processing workloads
- **Event-Driven Automation**: Using [[cloudwatch-and-eventbridge]] (EventBridge rules, S3 Event Notifications) to trigger [[lambda]] or [[glue]] jobs.
- **Infrastructure as Code (IaC)**: Deploying pipeline infrastructure reproducibly using [[cdk-cloudformation]] (AWS CDK, CloudFormation, SAM).

### Task Statement 3.2: Monitor data pipelines and evaluate metrics
- **CloudWatch Monitoring**:
  - Monitoring metrics, setting CloudWatch Alarms for Glue job failures or SQS DLQ depth.
  - Analyzing log streams using CloudWatch Logs Insights: [[cloudwatch-and-eventbridge]].
- **Auditing & Event Tracking**: Using AWS CloudTrail to log API actions across pipeline components.

### Task Statement 3.3: Ensure data quality and handle pipeline errors
- **Data Quality Rule Enforcement**:
  - Utilizing [[glue]] Data Quality (DQDL — Data Quality Definition Language) to audit, monitor, and enforce quality rules on dataset columns automatically.
- **Error Handling & Dead Letter Queues (DLQ)**:
  - Configuring DLQs in [[sqs-and-sns]] and [[lambda]] for failed event retention and retry handling.
  - Retry logic and catch blocks in [[step-functions]].

### Task Statement 3.4: Optimize performance and manage costs
- **Resource Sizing & Provisioning**: Right-sizing EMR clusters, Glue DPUs (Data Processing Units), and Redshift Concurrency Scaling.
- **Cost Monitoring**: Using [[cost-management]] (AWS Cost Explorer, AWS Budgets, Savings Plans, Resource Tagging).

---

## 🛠️ Essential AWS Services in Domain 3

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS EventBridge** | Event Router / Automation | Trigger Step Functions or Glue workflows on S3 file creation or cron schedule | [[cloudwatch-and-eventbridge]] |
| **Amazon CloudWatch** | Logs, Metrics & Alarms | Pipeline performance alerting, log pattern matching via Insights | [[cloudwatch-and-eventbridge]] |
| **AWS Glue Data Quality** | Data Validation | Write DQDL rules to prevent bad data from reaching data warehouses | [[glue]] |
| **AWS SQS DLQ** | Failed Event Capture | Store unprocessable messages for asynchronous debugging | [[sqs-and-sns]] |
| **AWS Cost Explorer** | Cost Visibility | Identify highest-cost data engineering resources and set budgets | [[cost-management]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 3

> [!IMPORTANT]
> **AWS Glue Data Quality (DQDL)**:
> - Allows defining rules like `Completeness "customer_id" > 0.99`, `ColumnValues "status" in ["PENDING", "COMPLETED"]`.
> - Rules can fail pipeline jobs or route bad records to quarantine S3 buckets without writing custom validation code!

> [!TIP]
> **Handling Lambda Execution Failures**:
> - Asynchronous Lambda triggers (e.g. S3 event) automatically retry twice. After retries fail, events should be sent to an **SQS DLQ** or **Lambda Destinations (On Failure)**.

---

## 📌 Checklist for Domain 3
- [ ] Review slide pages: 618-670 (Monitoring & Governance) and 756-768 (Cost Management) in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- [ ] Complete service notes: [[cloudwatch-and-eventbridge]], [[glue]], [[sqs-and-sns]], [[cost-management]]
- [ ] Review IaC: [[cdk-cloudformation]]
