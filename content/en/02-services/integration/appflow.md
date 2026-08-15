---
title: AWS AppFlow
type: aws-service
category: Integration
tags:
  - aws/service
  - dea-c01
  - integration/appflow
date: 2026-07-28
---

# 🔗 AWS AppFlow (SaaS Data Integration)

- **Category**: Application Integration
- **Primary Use Case**: Fully managed secure transfer of data between SaaS applications (Salesforce, ServiceNow, Slack, Google Analytics) and AWS services (S3, Redshift).
- **Slide Reference**: Pages 530–537 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
AWS AppFlow allows data engineers to securely transfer data between Software-as-a-Service (SaaS) applications and AWS data stores (Amazon S3, Amazon Redshift) at scale without writing custom API connectors or managing infrastructure.

---

## 2. Key Features
- **Triggers**: On-Demand, Scheduled (cron), or Event-Driven (e.g. Salesforce object update).
- **Transformations**: Column mapping, masking PII fields, filtering records, and data validation during transfer.
- **Security**: Private link support over AWS PrivateLink (prevents data from traversing the public internet).

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Ingesting Salesforce / ServiceNow data directly into S3 or Redshift**: Choose **AWS AppFlow** (zero code, native SaaS connectors).

---

## 📌 Related Notes
- [[s3]] — Target S3 bucket endpoint
- [[redshift]] — Target Redshift data warehouse endpoint
