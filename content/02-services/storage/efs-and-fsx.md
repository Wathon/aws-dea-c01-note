---
title: Amazon EFS & AWS FSx
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/file
date: 2026-07-28
---

# 📁 Amazon EFS & AWS FSx (Lustre, ONTAP, Windows, OpenZFS)

- **Category**: Shared File Storage
- **Primary Use Case**: Shared POSIX file systems for Linux compute clusters, high-performance computing (HPC) staging for ML and analytics.
- **Slide Reference**: Pages 139–154 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[s3]]

---

## 1. High-Level Summary
Shared file storage allows hundreds of concurrent compute instances (EC2, ECS, EKS, Lambda) to access a single shared POSIX-compliant file system simultaneously.

---

## 2. Technical Comparison: EFS vs FSx for Lustre

| Feature | Amazon EFS | AWS FSx for Lustre |
| --- | --- | --- |
| **Target OS / Protocol** | Linux (NFSv4) | High Performance Compute / Linux |
| **Performance** | Elastic auto-scaling throughput (MB/s) | **Massive parallel throughput** (hundreds of GB/s, millions of IOPS) |
| **S3 Integration** | Manual sync / AWS DataSync | **Native Seamless Hydration & Export to/from S3** |
| **Primary Data Use Case**| Multi-AZ shared application data, container persistent volumes | **HPC, High Performance ML Training, EMR Staging** |

---

## 3. Key FSx Flavors Overview
1. **FSx for Lustre**: Designed for **fast processing of massive data sets** (ML, HPC, financial modeling). Can link directly to S3 bucket to automatically present S3 objects as files!
2. **FSx for NetApp ONTAP**: Enterprise multi-protocol shared storage (NFS, SMB, iSCSI).
3. **FSx for Windows File Server**: Native SMB file storage for Windows environments.

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **FSx for Lustre + S3 Scenario**:
> - If an exam question mentions **processing massive datasets in parallel from S3 using sub-millisecond HPC file systems**, the answer is **FSx for Lustre with S3 integration**. Data is loaded transparently into FSx from S3 and results written back to S3!

---

## 📌 Related Notes
- [[s3]] — S3 Data Lake Integration
- [[emr]] — Staging data for EMR cluster processing
