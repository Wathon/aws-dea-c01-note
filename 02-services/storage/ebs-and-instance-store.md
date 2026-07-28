---
title: Amazon EBS & EC2 Instance Store
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/block
date: 2026-07-28
---

# 💾 Amazon EBS & EC2 Instance Store

- **Category**: Storage (Block Storage)
- **Primary Use Case**: High-IOPS block storage for EC2 instances, temporary scratch storage for processing nodes.
- **Slide Reference**: Pages 139–154 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[s3]]

---

## 1. High-Level Summary
Block storage solutions provide dedicated storage volumes attached directly to compute instances (EC2). Data engineers must understand the trade-offs between **EC2 Instance Store** (ephemeral, maximum IOPS) and **Amazon EBS** (persistent, network-attached block storage) for data pipelines and database hosting.

---

## 2. Technical Comparison: EBS vs Instance Store

| Feature | Amazon EBS (Elastic Block Store) | EC2 Instance Store |
| --- | --- | --- |
| **Persistence** | Persistent (survives instance stop/termination) | **Ephemeral** (data LOST on instance stop/termination) |
| **Connection** | Network-attached volume | Physically attached to host server |
| **Performance** | High (up to 256,000 IOPS with `io2 Block Express`) | **Ultra-High / Lowest Latency** (Millions of IOPS) |
| **Backups** | Automated EBS Snapshots to S3 | Manual script to copy data out before stop |
| **Use Case** | Databases (RDS/EC2), persistent application storage | Buffer/Cache, scratch space, temporary processing |

---

## 3. Key EBS Volume Types for Data Engineering

1. **General Purpose SSD (`gp3`)**:
   - Baseline 3,000 IOPS and 125 MB/s throughput included free. Scalable up to 16,000 IOPS independently of storage capacity. Standard cost-effective volume.
2. **Provisioned IOPS SSD (`io2` / `io2 Block Express`)**:
   - Designed for mission-critical OLTP databases requirement high IOPS (up to 256,000 IOPS).
3. **Throughput Optimized HDD (`st1`)**:
   - Low-cost HDD volume designed for **frequent, throughput-intensive big data workloads**, MapReduce, log processing, and Kafka storage.
4. **Cold HDD (`sc1`)**:
   - Lowest cost HDD for infrequently accessed sequential workloads / archives.

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> - **Temporary High-Speed Scratch Storage**: Choose **EC2 Instance Store** when buffer/scratch disk throughput is paramount and data persistence on instance stop is NOT required (e.g. Spark worker shuffle space).
> - **Big Data Sequential Throughput on EC2**: Choose **EBS `st1`** for cost-effective big data streaming & logging.

---

## 📌 Related Notes
- [[s3]] — Persistent object storage
- [[efs-and-fsx]] — Shared network file systems
