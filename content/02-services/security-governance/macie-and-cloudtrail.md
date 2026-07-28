---
title: Amazon Macie & AWS CloudTrail
type: aws-service
category: Security
tags:
  - aws/service
  - dea-c01
  - security/compliance
date: 2026-07-28
---

# 🔍 Amazon Macie & AWS CloudTrail

- **Category**: Security, Identity, & Compliance
- **Primary Use Case**: Machine learning PII detection in S3 (Macie), auditing API calls and administrative actions (CloudTrail).
- **Slide Reference**: Pages 630–670 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-4-data-security-and-governance]]

---

## 1. High-Level Summary
Maintaining data security compliance requires discovering unencrypted PII data in S3 using **Amazon Macie** and auditing pipeline operations across AWS services using **AWS CloudTrail**.

---

## 2. Technical Feature Breakdown

### Amazon Macie (PII Discovery)
- Uses machine learning and pattern matching to evaluate S3 buckets for sensitive data such as Personally Identifiable Information (PII) — Credit Card numbers, Social Security Numbers (SSN), passports, API keys.
- Generates findings and alerts in EventBridge when unencrypted or exposed PII is detected.

### AWS CloudTrail (API Audit Logging)
- Records API calls made by users, roles, or AWS services across your infrastructure.
- **Management Events**: Control plane operations (e.g. `CreateBucket`, `RunInstances`).
- **Data Events**: High-volume data plane operations (e.g. `s3:GetObject`, `s3:PutObject`, `Lambda:Invoke`). Data events are NOT enabled by default due to log volume/cost!

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Detecting PII in S3 Data Lake automatically**: Use **Amazon Macie**.
> - **Tracking who modified a Glue crawler or deleted an S3 bucket**: Inspect **AWS CloudTrail Management Events**.

---

## 📌 Related Notes
- [[s3]] — Target S3 buckets evaluated by Macie & CloudTrail
- [[cloudwatch-and-eventbridge]] — Alerting on Macie findings via EventBridge
