---
title: Amazon VPC & AWS Networking
type: aws-service
category: Networking
tags:
  - aws/service
  - dea-c01
  - networking/vpc
date: 2026-07-28
---

# 🌐 Amazon VPC & AWS Networking for Data Engineers

- **Category**: Networking & Content Delivery
- **Primary Use Case**: Isolated network infrastructure, private subnets, security groups, PrivateLink / VPC Endpoints for private data flow.
- **Slide Reference**: Pages 590–617 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-4-data-security-and-governance]]

---

## 1. High-Level Summary
Data engineering resources (RDS, Redshift, EMR, Lambda, Glue) should reside inside private subnets within an **Amazon VPC** to isolate sensitive corporate data from public internet exposure.

---

## 2. Key Networking Components

### 1. Security Groups vs Network ACLs (NACLs)

| Feature | Security Group | Network ACL (NACL) |
| --- | --- | --- |
| **Operates At** | Instance level (ENI) | Subnet level |
| **Statefulness** | **Stateful** (Return traffic automatically allowed) | **Stateless** (Must explicitly allow inbound & outbound traffic) |
| **Rule Evaluation** | Evaluates all rules before allowing | Processed in numerical order (lowest rule # first) |
| **Deny Rules** | Supports ALLOW rules only | Supports explicit ALLOW and DENY rules |

---

### 2. VPC Endpoints (Gateway vs Interface Endpoints)
Allows private network connectivity from resources in a private VPC subnet to AWS services **without traversing the public internet or requiring an Internet Gateway / NAT Gateway**:

| Feature | Gateway Endpoint | Interface Endpoint (AWS PrivateLink) |
| --- | --- | --- |
| **Supported Services** | **Amazon S3** & **Amazon DynamoDB** ONLY | Glue, Redshift, KMS, Athena, Kinesis, Secrets Manager, etc. |
| **Cost** | **FREE** | Hourly rate + per-GB data processing fee |
| **Mechanism** | Target entry in VPC Route Table | Elastic Network Interface (ENI) with Private IP in subnet |

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Connect Glue / Lambda in Private Subnet to S3 without Internet Gateway**: Use an **S3 Gateway VPC Endpoint** (Free and highly secure).
> - **Private Redshift or Glue Connection**: Use **Interface VPC Endpoints**.

---

## 📌 Related Notes
- [[s3]] — S3 Gateway Endpoint target
- [[dynamodb]] — DynamoDB Gateway Endpoint target
