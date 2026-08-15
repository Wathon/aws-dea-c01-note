---
title: Amazon EFS & AWS FSx (မြန်မာဘာသာ)
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/file
  - efs
  - fsx
  - lustre
  - burmese
date: 2026-08-15
---

# 📁 Amazon EFS & AWS FSx (Lustre, ONTAP, Windows, OpenZFS) (မျှဝေသုံး ဖိုင်စနစ်များ)

- **Category**: Storage (Shared Managed File Systems)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/storage/efs-and-fsx.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Linux Compute Clusters များအတွက် မျှဝေသုံး POSIX File Storage၊ Container Persistent Volumes (`[[ecr-ecs-eks]]`)၊ Serverless Functions (`[[lambda]]`)၊ နှင့် `[[s3]]` မှ HPC/Machine Learning Datasets များကို အလွန်မြန်ဆန်သော **AWS FSx for Lustre** ဖြင့် Parallel Staging ပြုလုပ်ခြင်း။
- **Slide Reference**: Pages 139–154 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[s3]]` | `[[ebs-and-instance-store]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

Shared File Storage သည် Compute Instances ရာထောင်ချီ (EC2, ECS Tasks, EKS Pods, Lambda Functions များနှင့် On-premise Servers) အား Single POSIX File System တစ်ခုတည်းကို Network မှတစ်ဆင့် တစ်ပြိုင်နက် ရယူအသုံးပြုခွင့် (Read/Write) ပေးသည်။

```mermaid
graph TB
    subgraph ComputeLayer["Compute Layer (Multi-AZ & Hybrid)"]
        EC2Node["EC2 Linux Instances<br/>(Cluster Compute / Spark)"]
        EKSContainers["Amazon ECR / ECS / EKS<br/>(Container Stateful Volumes)"]
        Serverless["AWS Lambda Functions<br/>(Serverless ML / ETL)"]
        OnPrem["On-Premises Servers<br/>(via Direct Connect / VPN)"]
    end

    subgraph EFSArch["Amazon EFS (Multi-AZ Elastic File System)"]
        AP["EFS Access Points<br/>(POSIX UID/GID Enforcement + Root Directory Jailing)"]
        MT1["Mount Target (AZ-a)"]
        MT2["Mount Target (AZ-b)"]
        MT3["Mount Target (AZ-c)"]
        
        subgraph EFSTiers["EFS Tiering (Intelligent-Tiering / Lifecycle)"]
            StandardTier[("EFS Standard<br/>⚡ Low Latency SSD")]
            IATier[("EFS Infrequent Access (IA)<br/>💰 92% Lower Storage Cost")]
            ArchiveTier[("EFS Archive<br/>📦 Cold Compliance Data")]
        end
    end

    subgraph FSxArch["AWS FSx for Lustre (HPC & ML Staging)"]
        LustreCluster[("FSx for Lustre Parallel FS<br/>⚡ Hundreds of GB/s Throughput<br/>⚡ Sub-millisecond Latency")]
        S3Bucket[("Amazon S3 Data Lake<br/>📦 Automated Hydration & Export<br/>(Data Repository Association)")]
    end

    EC2Node -->|"NFSv4 (Port 2049) + TLS"| AP
    EKSContainers --> AP
    Serverless --> AP
    OnPrem --> AP

    AP --> MT1
    AP --> MT2
    AP --> MT3

    MT1 --- StandardTier
    MT2 --- StandardTier
    MT3 --- StandardTier
    StandardTier <--> IATier
    IATier <--> ArchiveTier

    EC2Node <-->|"Lustre Driver (Parallel POSIX)"| LustreCluster
    LustreCluster <-->|"Bi-directional Sync"| S3Bucket

    classDef comp fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef fsx fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;

    class ComputeLayer,EC2Node,EKSContainers,Serverless,OnPrem comp;
    class EFSArch,AP,MT1,MT2,MT3,EFSTiers,StandardTier,IATier,ArchiveTier efs;
    class FSxArch,LustreCluster,S3Bucket fsx;
```

---

## ၂။ Amazon EFS vs. AWS FSx for Lustre (Core Exam Focus)

```mermaid
graph TD
    DecisionRoot{Shared File System Requirement?}

    DecisionRoot -->|"Linux Standard Workloads, Containers, Lambda, Multi-AZ Shared Directory"| EFSBranch["Amazon EFS<br/>• Standard POSIX NFSv4.1<br/>• Serverless & Multi-AZ replication<br/>• Elastic Auto-scaling capacity"]

    DecisionRoot -->|"HPC, Distributed ML, Video Rendering, Big Data Compute Layer"| FSxLBranch["AWS FSx for Lustre<br/>• Parallel File System (Hundreds of GB/s)<br/>• Sub-millisecond latency<br/>• Native Bi-directional Sync with Amazon S3"]

    DecisionRoot -->|"Windows Active Directory / SMB"| FSxWBranch["AWS FSx for Windows File Server"]

    DecisionRoot -->|"Enterprise NetApp ONTAP Features (SnapMirror/Deduplication)"| FSxOBranch["AWS FSx for NetApp ONTAP"]

    classDef dec fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef fsx fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;

    class DecisionRoot dec;
    class EFSBranch efs;
    class FSxLBranch,FSxWBranch,FSxOBranch fsx;
```

| Dimension | Amazon EFS | AWS FSx for Lustre |
| :--- | :--- | :--- |
| **Protocol** | **NFSv4.1 / NFSv4.0** | **Lustre Parallel Client** |
| **Architecture** | **Multi-AZ by default** (Regional Resilience) | **Single-AZ** (Scratch/Persistent) သို့မဟုတ် Multi-AZ |
| **S3 Integration** | DataSync ဖြင့် သီးခြား ကူးယူရသည် | **Native Direct S3 Link (Data Repository Association)** — S3 ရှိ Object များကို ဖိုင်အဖြစ် တိုက်ရိုက်ဖတ်/ရေးသည် |
| **Performance Profile** | အများဆုံး 10+ GB/s Throughput, Low-ms Latency | **Hundreds of GB/s Throughput, Millions of IOPS, Sub-ms Latency** |
| **Data Engineering အသုံးချမှု** | • Container Persistent Volumes (`[[ecr-ecs-eks]]`)<br/>• Lambda Functions (`[[lambda]]`) ကြီးမားသော ML Model မျှဝေရန် | • **Distributed Machine Learning (SageMaker / PyTorch)**<br/>• **High-Performance Big Data Simulations on S3 data** |

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Shared POSIX file system across multiple Availability Zones for Linux EC2, ECS, and Lambda"** $\rightarrow$ **Amazon EFS**.
> - **"Ultra-high-throughput parallel file system for machine learning / HPC with seamless bi-directional S3 data lake sync"** $\rightarrow$ **AWS FSx for Lustre**.
> - **"Restrict Lambda function file access to a specific POSIX directory with UID/GID enforcement"** $\rightarrow$ **EFS Access Points**.

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[ebs-vs-efs-vs-instance-store]]` — Decision Matrix: EBS vs. EFS vs. Instance Store
- `[[s3]]` — Amazon S3 Data Lake Object Storage
- `[[lambda]]` — AWS Lambda with Mounted Amazon EFS
- `[[ecr-ecs-eks]]` — Containers Persistent Storage
