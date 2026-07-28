---
title: AWS Batch
type: aws-service
category: Compute
tags:
  - aws/service
  - dea-c01
  - compute/batch
date: 2026-07-28
---

# 📦 AWS Batch

- **Category**: Compute
- **Primary Use Case**: Fully managed batch computing for containerized workloads across EC2 / Fargate.
- **Slide Reference**: Pages 286–312 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[lambda]]

---

## 1. High-Level Summary
AWS Batch dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted.

---

## 2. Key Architecture Components
- **Job Definitions**: Specifies how jobs are to be run (Docker image, vCPU, memory, IAM role, environment variables).
- **Job Queues**: Priority-based queues holding jobs until compute resources are ready.
- **Compute Environments**: Managed or unmanaged sets of compute resources (EC2 instances or Fargate serverless containers). Can utilize **Spot Instances** for up to 90% cost savings!

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - Choose **AWS Batch** over Lambda when batch processing jobs run **longer than 15 minutes**, require specialized GPU compute, or run containerized C++/Python binaries.
> - Choose **AWS Batch with Spot Instances** for fault-tolerant batch workloads to minimize cost.

---

## 📌 Related Notes
- [[lambda]] — Serverless compute (max 15 mins)
- [[ecr-ecs-eks]] — Containerized job environments
