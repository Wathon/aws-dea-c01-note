---
title: AWS Identity and Access Management (IAM)
type: aws-service
category: Security
tags:
  - aws/service
  - dea-c01
  - security/iam
date: 2026-07-28
---

# 🔑 AWS IAM (Identity and Access Management)

- **Category**: Security, Identity, & Compliance
- **Primary Use Case**: Least-privilege identity access management, service execution roles, cross-account access.
- **Slide Reference**: Pages 542–559 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-4-data-security-and-governance]]

---

## 1. High-Level Summary
AWS IAM provides fine-grained access control across all AWS resources. Data engineers must configure IAM Users, Roles, Policies, and Service-Linked Roles to securely grant pipeline components (Lambda, Glue, EMR, Redshift) permissions to read/write data in S3 and other data stores.

---

## 2. Key Architecture Concepts

### IAM Entities
- **IAM Policies**: JSON documents defining `Effect` (Allow/Deny), `Principal`, `Action` (e.g. `s3:GetObject`), and `Resource` (ARN).
- **IAM Roles**: Assumable identities with specific permissions granted temporarily to AWS Services (e.g. EC2 Instance Profile, Glue Execution Role, Lambda Execution Role) or cross-account users.
- **Cross-Account Roles**: Allows an IAM principal in Account A to assume a role in Account B to process data stored in Account B's S3 data lake.

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Principle of Least Privilege**: Never grant `s3:*` or `AdministratorAccess`. Explicitly define precise actions like `s3:GetObject` on specific bucket ARNs.
> - **Explicit Deny Overrides All**: An explicit `Deny` in any policy evaluation always overrides any `Allow` permissions!

---

## 📌 Related Notes
- [[lake-formation]] — Fine-grained Lake Formation permissions vs IAM
- [[kms-and-secrets]] — KMS Key Policy integration with IAM
