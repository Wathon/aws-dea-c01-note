---
title: Amazon EFS vs. EBS vs. EC2 Instance Store (မြန်မာဘာသာ)
type: comparison
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/comparison
  - efs
  - ebs
  - instance-store
  - burmese
date: 2026-08-15
---

# ⚖️ Amazon EFS vs. Amazon EBS vs. EC2 Instance Store (သိုလှောင်မှု စနစ် ၃ မျိုး နှိုင်းယှဉ်ချက်)

- **Category**: Storage Architecture & Service Selection
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/storage/ebs-vs-efs-vs-instance-store.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: **Amazon EFS** (Shared Multi-AZ File)၊ **Amazon EBS** (Persistent Network Block) နှင့် **EC2 Instance Store** (Ultra-High IOPS Ephemeral Block) တို့အကြား သင့်လျော်သော Storage အလွှာကို ရွေးချယ်နိုင်ရန် ဆုံးဖြတ်ချက် လမ်းညွှန်။
- **Slide Reference**: Pages 139–154 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[ebs-and-instance-store]]` | `[[efs-and-fsx]]` | `[[s3]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Architectural Summary)

DEA-C01 စာမေးပွဲ Domain 2 တွင် အမေးအများဆုံး အကြောင်းအရာတစ်ခုမှာ Workload အလိုက် သင့်လျော်သော Compute-attached Storage ကို ရွေးချယ်ခြင်း ဖြစ်သည်-

```mermaid
graph TB
    subgraph HostServer["Physical EC2 Host Hardware"]
        EC2Instance["EC2 Instance (Compute Worker / Broker / DB)"]
        InstStore[("EC2 Instance Store<br/>⚡ Physical NVMe PCIe Bus<br/>⚡ Sub-ms Latency / Millions IOPS<br/>❌ Ephemeral (Wiped on STOP)")]
        EC2Instance <-->|"Direct PCIe / NVMe Bus"| InstStore
    end

    subgraph AWSAZ["Single Availability Zone (Network Attached)"]
        EBSVol[("Amazon EBS Volume<br/>(gp3 / io2 / st1 / sc1)<br/>💾 Dedicated Network SAN<br/>✅ Persistent across Stops<br/>🔒 Confined to Single AZ")]
        EC2Instance <-->|"Dedicated EBS Network Bus"| EBSVol
    end

    subgraph AWSCloud["Regional AWS Cloud (Multi-AZ Shared)"]
        EFSVol[("Amazon EFS File System<br/>(Standard / IA / Archive)<br/>📁 NFSv4.1 POSIX Shared Storage<br/>✅ Multi-AZ (11 9's Durability)<br/>👥 Thousands of Concurrent Nodes")]
        EC2Instance <-->|"NFSv4 (Port 2049) + TLS"| EFSVol
        LambdaFunc["AWS Lambda / ECS / EKS"] <-->|"EFS Access Point"| EFSVol
        OnPrem["On-Premises Servers"] <-->|"Direct Connect / VPN"| EFSVol
    end

    classDef host fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef ebs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class HostServer,EC2Instance,InstStore host;
    class AWSAZ,EBSVol ebs;
    class AWSCloud,EFSVol,LambdaFunc,OnPrem efs;
```

---

## ၂။ Master Comparative Matrix

| Feature | EC2 Instance Store | Amazon EBS | Amazon EFS |
| :--- | :--- | :--- | :--- |
| **Storage Type** | **Block Storage** | **Block Storage** | **File Storage (POSIX / NFSv4.1)** |
| **Physical Attachment** | Direct-attached NVMe PCIe | Network-attached virtual disk | Network-attached shared file system |
| **Persistence** | ❌ **Ephemeral** (Stop/Terminate လုပ်ပါက ဒေတာ ပျက်သည်) | ✅ **Persistent** (Independent of instance lifecycle) | ✅ **Persistent & Serverless Elastic** |
| **Scope / Boundary** | Single Host Server | **Single Availability Zone (AZ)** | **Regional (Multi-AZ by default)** |
| **Concurrency** | Single EC2 Instance သာ သုံးနိုင်သည် | Single Instance (io1/io2 Multi-Attach in same AZ) | **EC2, ECS, EKS, Lambda ထောင်သောင်းချီ တစ်ပြိုင်နက် သုံးနိုင်သည်** |
| **Max Performance** | **Millions of IOPS, Sub-ms latency** | Up to 256,000 IOPS (io2), Low-ms | Up to 10+ GB/s throughput, Low-ms |
| **အကောင်းဆုံး အသုံးချမှု** | Spark Shuffling, Temporary caches, Ingest buffers | Databases (`[[rds-and-aurora]]`), Kafka logs | Shared models, Container volumes, Web assets |

---

## ၃။ စာမေးပွဲ ဆုံးဖြတ်ချက် လမ်းညွှန် (Exam Decision Tree)

```mermaid
graph TD
    DecisionRoot{Storage Selection Question}

    DecisionRoot -->|"ယာယီ (Temporary) Spark Shuffle, Caches, အမြင့်ဆုံး IOPS လိုအပ်ပါက"| UseInstStore["EC2 Instance Store (NVMe SSD)<br/>• Sub-millisecond latency, zero network cost"]

    DecisionRoot -->|"Database Data Disk, Single AZ Persistent Block လိုအပ်ပါက"| UseEBS["Amazon EBS (gp3 / io2 / st1)<br/>• Independent lifecycle, S3 snapshots"]

    DecisionRoot -->|"EC2, ECS, Lambda များစွာမှ Multi-AZ မျှဝေသုံးစွဲရန် လိုအပ်ပါက"| UseEFS["Amazon EFS<br/>• Multi-AZ durability, Serverless scaling, NFSv4"]

    classDef dec fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef inst fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef ebs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class DecisionRoot dec;
    class UseInstStore inst;
    class UseEBS ebs;
    class UseEFS efs;
```

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[ebs-and-instance-store]]` — Amazon EBS & Instance Store Deep Dive
- `[[efs-and-fsx]]` — Amazon EFS & FSx Deep Dive
- `[[s3]]` — Amazon S3 Object Storage
