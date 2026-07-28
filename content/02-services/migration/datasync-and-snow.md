---
title: AWS DataSync & AWS Snow Family
type: aws-service
category: Migration
tags:
  - aws/service
  - dea-c01
  - migration/transfer
date: 2026-07-28
---

# 🚚 AWS DataSync & AWS Snow Family

- **Category**: Migration & Transfer
- **Primary Use Case**: Large-scale online file transfer & offline physical device data migration.
- **Slide Reference**: Pages 276–285 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
Moving large datasets into AWS requires choosing between network-based online transfer (**AWS DataSync**) and physical appliance-based offline transfer (**AWS Snowball Family**) depending on network bandwidth, dataset size, and time constraints.

---

## 2. Technical Comparison & Decision Matrix

| Feature | AWS DataSync | AWS Snowcone | AWS Snowball Edge | AWS Snowmobile |
| --- | --- | --- | --- | --- |
| **Type** | Online Network Transfer | Physical Appliance | Physical Appliance | Physical Truck |
| **Capacity** | Unlimited (Network bounded) | 8 TB | 80 TB (Storage/Compute) | **100 Petabytes** |
| **Network Needed** | Active WAN Connection | Optional (offline ship) | Offline physical shipping | Offline physical shipping |
| **Use Case** | Scheduled file copy (NFS/SMB to S3/EFS/FSx) | Edge collection / small offsite data | Large dataset migration (> 10TB to PBs) | Exabyte-scale data center migration |

---

## 3. High-Yield Decision Formulas

### Transfer Time Calculation Formula:
$$\text{Transfer Time} = \frac{\text{Data Size (Bits)}}{\text{Network Bandwidth (Bits/Second)}}$$

> [!IMPORTANT]
> **Rule of Thumb for Exam**:
> - If network bandwidth available takes **more than 1-2 weeks** to transfer over the internet: Use **AWS Snowball Edge**.
> - For continuous, scheduled file synchronization between NFS/SMB on-premises and S3/EFS: Use **AWS DataSync**.

---

## 📌 Related Notes
- [[s3]] — Target S3 bucket storage
- [[efs-and-fsx]] — Target EFS / FSx file systems
