---
title: AWS KMS, Secrets Manager & Parameter Store
type: aws-service
category: Security
tags:
  - aws/service
  - dea-c01
  - security/kms
date: 2026-07-28
---

# 🔐 AWS KMS, Secrets Manager & Parameter Store

- **Category**: Security / Encryption
- **Primary Use Case**: Encryption key management (KMS), database credential rotation (Secrets Manager), configuration parameters.
- **Slide Reference**: Pages 560–575 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-4-data-security-and-governance]]

---

## 1. High-Level Summary
Data security at rest relies on **AWS Key Management Service (KMS)** for cryptographic envelope encryption. Credential management for databases (Redshift, RDS) uses **AWS Secrets Manager** to eliminate hardcoded password credentials in data pipelines.

---

## 2. Technical Encryption Breakdown

### S3 Encryption Methods Matrix

| Method | Key Managed By | Key Usage | Ideal Use Case |
| --- | --- | --- | --- |
| **SSE-S3** | AWS (Amazon S3) | AES-256 managed keys | Default zero-configuration encryption at rest |
| **SSE-KMS** | Customer & AWS (KMS) | KMS Customer Master Key (CMK) | Audit trail via CloudWatch/CloudTrail, key rotation control |
| **DSSE-KMS** | Customer & AWS (KMS) | Dual-layer envelope encryption | Strict regulatory compliance requiring dual-layer encryption |
| **SSE-C** | Customer (Provided in request header) | Customer provides raw encryption key | Custom compliance requiring full key control outside AWS |

---

### Secrets Manager vs Parameter Store

| Feature | AWS Secrets Manager | SSM Parameter Store |
| --- | --- | --- |
| **Automatic Rotation** | **Native automatic rotation** for RDS, Aurora, Redshift via Lambda | Manual or custom script rotation required |
| **Cost** | $0.40 per secret / month | **Free** (Standard parameters) |
| **Primary Use Case** | Database passwords, API credentials | App configuration parameters, license keys |

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **KMS Throttling Errors in Large Analytics Jobs**: If EMR or Glue jobs scan millions of S3 objects encrypted with SSE-KMS and hit `KMS.KMSInvalidStateException` throttling, enable **S3 Bucket Keys** to reduce KMS API calls by up to 99%!

---

## 📌 Related Notes
- [[s3]] — S3 SSE-S3/SSE-KMS encryption
- [[redshift]] — Database password rotation via Secrets Manager
