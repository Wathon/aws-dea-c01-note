---
title: "Domain 4: Data Security and Governance"
type: domain
tags:
  - domain/security
  - dea-c01
  - exam-prep
date: 2026-07-28
---

# 🔒 Domain 4: Data Security and Governance (Weight: 24%)

- **Domain ID**: Domain 4
- **Focus**: Enforcing data protection at rest and in transit, identity access management, fine-grained permissions, governance, compliance, and PII identification.
- **Hub Links**: [[index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 4.1: Apply authentication, authorization, and access control
- **Identity & Access Management (IAM)**:
  - Least privilege principles, execution roles for Lambda/Glue/EMR, cross-account access via IAM roles: [[iam]].
  - Fine-grained IAM database authentication for RDS, Aurora, and Redshift.
- **Data Lake Access Control**:
  - Centralized fine-grained access control using [[lake-formation]].
  - Column-level, row-level, and cell-level security.
  - Tag-Based Access Control (LF-TBAC).

### Task Statement 4.2: Apply data protection & encryption mechanisms
- **Encryption at Rest**:
  - S3 Server-Side Encryption: SSE-S3 (AWS managed key), SSE-KMS (Customer Master Key), SSE-C (Customer provided key): [[kms-and-secrets]].
  - Redshift, DynamoDB, RDS, EBS, and EFS KMS encryption.
- **Encryption in Transit**:
  - Enforcing TLS/SSL for database connections, S3 bucket policies enforcing `aws:SecureTransport`.
- **Secrets Management**:
  - Managing database credentials with [[kms-and-secrets]] (Secrets Manager vs SSM Parameter Store).

### Task Statement 4.3: Ensure governance, compliance, and PII protection
- **PII Detection & Privacy**:
  - Automated PII scanning in S3 using [[macie-and-cloudtrail]] (Amazon Macie).
  - Sensitive data identification in [[glue]] ETL jobs (Glue Sensitive Data Detection).
- **Data Cataloging & Discovery**:
  - Centralized enterprise governance using AWS DataZone and [[lake-formation]] Data Catalog.

### Task Statement 4.4: Network security & isolation
- **Network Isolation**:
  - Isolating data resources within private subnets in Amazon VPC: [[vpc-and-networking]].
  - Private routing without Internet Gateways using **VPC Endpoints** (Gateway Endpoints for S3 & DynamoDB; Interface Endpoints / PrivateLink for Glue, KMS, Redshift).

---

## 🛠️ Essential AWS Services in Domain 4

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS Lake Formation** | Data Lake Governance | Column/Row-level access control on S3 data lake via Glue Catalog | [[lake-formation]] |
| **AWS KMS** | Key Management & Encryption | Managing KMS keys for SSE-KMS encryption across all storage services | [[kms-and-secrets]] |
| **AWS Secrets Manager** | Database Credential Rotation | Automatic rotation of Redshift/RDS password credentials | [[kms-and-secrets]] |
| **Amazon Macie** | Machine Learning PII Discovery | Discovering sensitive PII data (SSN, credit card) in S3 buckets | [[macie-and-cloudtrail]] |
| **VPC Endpoints** | Private Network Access | Connect S3/DynamoDB/Glue privately without traversing public internet | [[vpc-and-networking]] |
| **AWS Backup** | Centralized Data Protection | Policy-driven multi-service backups, Vault Lock WORM compliance & cross-account DR | [[aws-backup]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 4

> [!IMPORTANT]
> **Lake Formation vs IAM vs S3 Bucket Policies**:
> - If requirement is **column-level or row-level security for Athena/Redshift Spectrum queries on S3**: Choose **AWS Lake Formation**. Standard S3 bucket policies and IAM can ONLY grant object-level access (read/write file), NOT row/column filtering!

> [!TIP]
> **Secrets Manager vs SSM Parameter Store**:
> - Choose **AWS Secrets Manager** when requirement includes **automatic database credential rotation** (integrates natively with RDS, Aurora, Redshift).
> - Choose **SSM Parameter Store** for standard parameters/configuration strings at zero or lower cost when automatic rotation is NOT needed.

---

## 📌 Checklist for Domain 4
- [ ] Review slide pages: 542-589 (Security) and 590-617 (Networking) in [[AWSCertifiedDataEngineerSlides.pdf]]
- [ ] Complete service notes: [[lake-formation]], [[iam]], [[kms-and-secrets]], [[macie-and-cloudtrail]], [[vpc-and-networking]], [[aws-backup]]
