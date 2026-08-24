---
title: Amazon CloudWatch & Amazon EventBridge
type: aws-service
category: Monitoring
tags:
  - aws/service
  - dea-c01
  - monitoring/cloudwatch
date: 2026-07-28
---

# 📈 Amazon CloudWatch & Amazon EventBridge

- **Category**: Management, Governance & Monitoring
- **Primary Use Case**: Metrics, log aggregation, CloudWatch Logs Insights, event routing, pipeline automation rules.
- **Slide Reference**: Pages 618–670 in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-3-data-operations-and-support]]

---

## 1. High-Level Summary
Amazon CloudWatch provides monitoring and telemetry data for AWS infrastructure. Amazon EventBridge (formerly CloudWatch Events) is a serverless event bus used to route real-time data events between AWS services to trigger data pipeline tasks automatically.

---

## 2. Technical Features

### 1. Amazon CloudWatch Features
- **CloudWatch Metrics**: Performance data collected automatically from AWS services (e.g. CPU utilization, SQS `ApproximateNumberOfMessagesVisible`).
- **CloudWatch Alarms**: Triggers notifications (via SNS) or auto-scaling actions when metrics breach thresholds.
- **CloudWatch Logs Insights**: Interactive SQL-like query engine to search, filter, and analyze log events stored in CloudWatch Logs (e.g., searching Lambda error tracebacks).

### 2. Amazon EventBridge Features
- **Event Rules**: Match incoming JSON events (e.g. S3 object creation, Glue job state change) and route to targets (Step Functions, Lambda, SNS).
- **Scheduled Rules (Cron)**: Execute pipelines on recurring cron schedules.
- **EventBridge Schema Registry**: Discovers and stores event schemas to generate code bindings in Python, Java, or TypeScript.

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Triggering a Step Functions workflow when an S3 file drops**: Use **Amazon EventBridge rule** matching `s3:ObjectCreated` event.
> - **Search through gigabytes of Lambda log stream lines**: Use **CloudWatch Logs Insights**.

---

## 📌 Related Notes
- [[step-functions]] — Trigger target for EventBridge
- [[lambda]] — Lambda logging into CloudWatch
