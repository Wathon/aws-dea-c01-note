---
title: Amazon ECR, ECS & EKS (Containers on AWS)
type: aws-service
category: Containers
tags:
  - aws/service
  - dea-c01
  - containers
date: 2026-07-28
---

# 🐳 Amazon ECR, ECS & EKS

- **Category**: Containers & Compute
- **Primary Use Case**: Docker container registry, container orchestration (ECS Fargate vs EKS Kubernetes).
- **Slide Reference**: Pages 313–330 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[batch]]

---

## 1. High-Level Summary
Containers package code, dependencies, and configurations together to ensure applications run reliably across compute environments. In AWS data pipelines, custom container images stored in **ECR** are executed on **ECS** or **EKS** for custom ETL jobs, microservices, and Spark workloads.

---

## 2. Technical Comparison Matrix

| Component | AWS Service | Key Characteristics for Exam |
| --- | --- | --- |
| **Container Registry** | **Amazon ECR** | Managed Docker container registry. Vulnerability scanning, KMS encryption. |
| **Simple Orchestration** | **Amazon ECS** | AWS-native container management. Supports **EC2 Launch Type** (manage VMs) and **Fargate** (Serverless containers). |
| **Kubernetes Orchestration** | **Amazon EKS** | Managed open-source Kubernetes. Ideal for running **EMR on EKS** or native K8s data pipelines. |

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> - **EMR on EKS**: Running Spark applications on Amazon EKS allows sharing Kubernetes clusters across applications, increasing resource utilization and reducing cost!
> - **ECS Fargate**: Serverless container execution with zero EC2 instance management required.

---

## 📌 Related Notes
- [[emr]] — Running Spark on EKS
- [[batch]] — Running batch jobs in containers
