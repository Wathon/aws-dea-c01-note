---
title: Amazon EBS & EC2 Instance Store (မြန်မာဘာသာ)
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/block
  - ebs
  - instance-store
  - burmese
date: 2026-08-15
---

# 💾 Amazon EBS & EC2 Instance Store (Block Storage) (ဘလော့အဆင့် သိုလှောင်မှု စနစ်များ)

- **Category**: Storage (Block Storage)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/storage/ebs-and-instance-store.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: EC2 Compute Instances များအတွက် Block-level Storage၊ Big Data တွက်ချက်မှုများအတွက် မြန်ဆန်သော ယာယီ Scratch Storage၊ Databases များနှင့် Streaming Brokers များအတွက် Persistent Disk များ တပ်ဆင်ခြင်း။
- **Slide Reference**: Pages 139–154 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[s3]]` | `[[efs-and-fsx]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

Block Storage သည် EC2 Compute Instances များနှင့် တိုက်ရိုက်ချိတ်ဆက်အသုံးပြုနိုင်သော Low-latency Disk Volumes များကို ပေးဆောင်သည်။ Data Engineering စနစ်များတွင် Big Data Analytics Clusters၊ Distributed Streaming Brokers (Kafka) နှင့် Self-hosted Database များအတွက် အဓိက သိုလှောင်မှု အလွှာအဖြစ် အသုံးပြုသည်။

အင်ဂျင်နီယာများသည် **EC2 Instance Store** (Physical Server တွင် တိုက်ရိုက်တပ်ဆင်ထားသော Ephemeral၊ အမြင့်ဆုံး IOPS/Throughput) နှင့် **Amazon EBS** (Network ဖြင့် ချိတ်ဆက်ထားသော Persistent၊ Snapshot Backed Block Storage) တို့၏ ကွာခြားချက်များနှင့် သင့်လျော်သော EBS Volume Types (`gp3`, `io2`, `st1`, `sc1`) များကို ကျွမ်းကျင်စွာ ရွေးချယ်နိုင်ရမည်။

```mermaid
graph TB
    subgraph HostServer["Physical EC2 Host Server"]
        EC2Instance["EC2 Compute Instance (Worker / Broker / DB)"]
        InstStore[("EC2 Instance Store<br/>(Physical NVMe SSD / HDD)<br/>⚡ Ephemeral / Ultra-High IOPS")]
        EC2Instance <-->|"Direct PCIe / NVMe Bus (Sub-ms Latency)"| InstStore
    end

    subgraph AWSAZ["AWS Availability Zone (Network Attached)"]
        EBSVol[("Amazon EBS Volume<br/>(gp3 / io2 / st1 / sc1)<br/>💾 Persistent Block Storage")]
        EC2Instance <-->|"EBS Network Bus (Dedicated Bandwidth)"| EBSVol
    end

    subgraph AWSCloud["AWS Regional Storage"]
        S3Snap[("Amazon S3<br/>📦 Incremental EBS Snapshots<br/>11 9's Durability")]
        EBSVol -.->|"Point-in-time Backup / DLM"| S3Snap
    end

    classDef host fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef storage fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef s3 fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    class HostServer host;
    class EBSVol,InstStore storage;
    class S3Snap s3;
```

---

## ၂။ Amazon EBS vs. EC2 Instance Store နှိုင်းယှဉ်ချက်

| Feature | Amazon EBS (Elastic Block Store) | EC2 Instance Store (Ephemeral Storage) |
| :--- | :--- | :--- |
| **Physical Location** | **Network-attached Drive** (AZ အတွင်း Network ဖြင့် ချိတ်ဆက်ထားသည်) | **Direct-attached Drive** (EC2 Host Server ၏ Physical Motherboard တွင် တပ်ဆင်ထားသည်) |
| **Data Persistence** | ✅ **Persistent**: Instance ကို Stop/Start ပြုလုပ်သော်လည်း ဒေတာ မပျက်ပါ | ❌ **Ephemeral (ယာယီ)**: Instance ကို Stop သို့မဟုတ် Terminate လုပ်ပါက **ဒေတာ အားလုံး ပျက်စီးသည်** |
| **Max IOPS & Latency** | အများဆုံး 256,000 IOPS (io2 Block Express)၊ Single-digit ms Latency | **သန်းနှင့်ချီသော IOPS (Millions of IOPS)**၊ Sub-millisecond Latency (အမြန်ဆုံး) |
| **Backup & Snapshots** | **Amazon S3 Incremental Snapshots** ကို ထောက်ပံ့သည် | Built-in Snapshot မရှိပါ (Software အဆင့်မှ S3 သို့ Copy ကူးရသည်) |
| **Data Engineering အသုံးချမှု** | • Production Database Data Files (`[[rds-and-aurora]]`)<br/>• Kafka Broker Logs (`[[msk-kafka]]`) | • Spark Shuffle Storage / MapReduce Spillover<br/>• In-Memory Caches & Temporary Scratch Data |

---

## ၃။ Amazon EBS Volume Types နှိုင်းယှဉ်ချက်

```mermaid
graph TD
    WorkloadReq{What is the EBS Workload Type?}

    WorkloadReq -->|"General Purpose Boot & Balanced DB/ETL"| GP3["gp3 (SSD)<br/>• 3,000 IOPS & 125 MB/s baseline (FREE)<br/>• Scale IOPS/MBps independently of size"]

    WorkloadReq -->|"Mission-Critical Ultra-Low Latency OLTP / High IOPS"| IO2["io2 / io2 Block Express (SSD)<br/>• Up to 256,000 IOPS & sub-ms latency<br/>• 99.999% Durability (5 9's)"]

    WorkloadReq -->|"Sequential Throughput Big Data / EMR / Hadoop / Log Processing"| ST1["st1 (Throughput Optimized HDD)<br/>• 500 MB/s max throughput<br/>• Cost-effective for large sequential streams"]

    WorkloadReq -->|"Cold Infrequent Access Log Storage"| SC1["sc1 (Cold HDD)<br/>• Lowest cost block storage<br/>• Max 250 MB/s throughput"]

    classDef dec fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef ssd fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef hdd fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;

    class WorkloadReq dec;
    class GP3,IO2 ssd;
    class ST1,SC1 hdd;
```

---

## ၄။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Maximum IOPS and throughput for temporary Spark shuffle or intermediate scratch data"** $\rightarrow$ **EC2 Instance Store (NVMe SSD)**.
> - **"Cost-effective storage for high-throughput sequential big data logging and Hadoop HDFS"** $\rightarrow$ **EBS Throughput Optimized HDD (`st1`)**.
> - **"Predictable baseline performance where IOPS can scale without adding disk capacity"** $\rightarrow$ **EBS General Purpose SSD (`gp3`)**.
> - **"Attach block volume to multiple EC2 instances simultaneously"** $\rightarrow$ **EBS Multi-Attach with `io1` / `io2` (Clustered Applications / GFS2)**.

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[ebs-vs-efs-vs-instance-store]]` — Decision Matrix: EBS vs EFS vs Instance Store
- `[[efs-and-fsx]]` — Managed File Systems (EFS, FSx for Lustre)
- `[[s3]]` — Amazon S3 Object Storage
