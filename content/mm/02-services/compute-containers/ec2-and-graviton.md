---
title: Amazon EC2 & AWS Graviton in Big Data (မြန်မာဘာသာ)
type: aws-service
category: Compute
tags:
  - aws/service
  - dea-c01
  - compute/ec2
  - compute/graviton
  - spot-instances
  - emr
  - burmese
date: 2026-08-15
---

# 🖥️ Amazon EC2 & AWS Graviton in Big Data (Purchasing Models & Arm Architecture) (EC2 ဝယ်ယူမှုပုံစံများနှင့် Graviton ပရိုဆက်ဆာများ)

- **Category**: Compute (Virtual Machine Infrastructure, Spot Pricing & Arm Processors)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/compute-containers/ec2-and-graviton.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Self-hosted Data Platform များအတွက် အခြေခံ Compute အဖြစ် သုံးခြင်း၊ `[[emr]]` Cluster များ၏ Node Topology (Master, Core, Task nodes) ကို ဖွဲ့စည်းခြင်း၊ နှင့် `[[msk-kafka]]`၊ `[[rds-and-aurora]]`၊ `[[opensearch]]`၊ `[[lambda]]` တို့တွင် **AWS Graviton** Arm Processors ဖြင့် Price-Performance အမြင့်ဆုံး ရယူခြင်း။
- **Slide Reference**: Pages 286–288 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[emr]]` | `[[batch]]` | `[[ecr-ecs-eks]]` | `[[lambda]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**Amazon Elastic Compute Cloud (Amazon EC2)** သည် AWS Cloud တွင် စိတ်ကြိုက်ပြောင်းလဲနိုင်သော Compute Capacity ကို ပေးဆောင်သည်။ Data Engineering စနစ်များတွင် EC2 သည် Distributed Big Data Cluster များ (**Amazon EMR**), Managed Database များ (**Amazon RDS/Aurora**), Streaming Brokers များ (**Amazon MSK**) နှင့် Custom Container Fleets များကို မောင်းနှင်ပေးသည့် အဓိက အခြေခံအဆောက်အအုံ ဖြစ်သည်။

**AWS Graviton Processors** သည် AWS မှ သီးသန့် ဒီဇိုင်းထုတ်ထားသော 64-bit Arm Neoverse-based Microprocessors ဖြစ်ပြီး သမားရိုးကျ x86 Processors များနှင့် နှိုင်းယှဉ်ပါက Databases၊ Analytics၊ In-Memory Caching နှင့် Container များတွင် **၄၀% အထိ ပိုမိုကောင်းမွန်သော Price-Performance** ကို ပေးစွမ်းသည်။

```mermaid
graph TB
    subgraph PurchasingModels["EC2 Purchasing Models (ဝယ်ယူမှု ပုံစံများ)"]
        OnDemand["(1) On-Demand Instances<br/>• ကတိကဝတ်မလို၊ လိုသလောက်သုံး<br/>• Pay per second / hour<br/>🎯 ခန့်မှန်းရခက်သော၊ တိုတောင်းသော Jobs"]
        SpotInst["(2) Spot Instances<br/>• ၉၀% အထိ စျေးသက်သာသည်<br/>• ၂ မိနစ် သတိပေးချက်ဖြင့် ပြန်သိမ်းနိုင်သည်<br/>🎯 Fault-tolerant, stateless ETL & ML"]
        SavingsPlans["(3) Reserved Instances / Savings Plans<br/>• ၁ နှစ် သို့မဟုတ် ၃ နှစ် ကတိကဝတ်<br/>• ၇၂% အထိ စျေးသက်သာသည်<br/>🎯 ၂၄/၇ မပြတ်လည်ပတ်နေသော Baseline Clusters"]
    end

    subgraph EMRClusterMapping["Amazon EMR Cluster Topology (Node ဖွဲ့စည်းပုံ)"]
        MasterNode["Master Node (YARN ResourceManager / NameNode)<br/>🔒 MUST use On-Demand / Reserved Instances!"]
        CoreNode["Core Nodes (HDFS DataNodes + Compute)<br/>🛡️ On-Demand / Reserved (Prevents HDFS Data Loss)"]
        TaskNode["Task Nodes (Pure Compute / No HDFS)<br/>💰 100% Spot Instances (Safe to scale & terminate)"]
    end

    subgraph GravitonSilicon["AWS Graviton Silicon (Arm Architecture)"]
        GravitonChip["AWS Graviton3 / Graviton4<br/>⚡ ၄၀% Price-Performance သာလွန်သည်<br/>🌱 ၆၀% စွမ်းအင် သုံးစွဲမှု သက်သာသည်"]
        
        subgraph ManagedServices["Graviton-Optimized AWS Data Services"]
            MSK["Amazon MSK (Kafka)"]
            RDS["Amazon RDS / Aurora"]
            OpenSearch["Amazon OpenSearch"]
            EMRGrav["Amazon EMR"]
            LambdaGrav["AWS Lambda (Arm64)"]
        end
    end

    OnDemand --> MasterNode
    SavingsPlans --> CoreNode
    SpotInst --> TaskNode

    GravitonChip --> MSK
    GravitonChip --> RDS
    GravitonChip --> OpenSearch
    GravitonChip --> EMRGrav
    GravitonChip --> LambdaGrav

    classDef buy fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef emr fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef chip fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef svc fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class OnDemand,SpotInst,SavingsPlans buy;
    class MasterNode,CoreNode,TaskNode emr;
    class GravitonChip chip;
    class MSK,RDS,OpenSearch,EMRGrav,LambdaGrav svc;
```

---

## ၂။ EC2 Purchasing Options နှိုင်းယှဉ်ချက် (ဝယ်ယူမှု ရွေးချယ်စရာများ)

| Purchasing Option | စျေးသက်သာမှု | Interruption Risk (ရပ်တန့်ခံရနိုင်ခြေ) | အကောင်းဆုံး Data Engineering အသုံးချမှု |
| :--- | :--- | :--- | :--- |
| **On-Demand** | ပုံမှန်စျေးနှုန်း ($0\%$) | **လုံးဝမရှိပါ** (အသုံးပြုသူ မရပ်မချင်း အာမခံသည်) | • Dev/Test စမ်းသပ်မှုများ<br/>• အရေးကြီးပြီး မပြတ်တောက်နိုင်သော One-off Jobs<br/>• **EMR Master Nodes** |
| **Spot Instances** | **၉၀% အထိ လျှော့စျေး** | ⚠️ **AWS မှ ၂ မိနစ် သတိပေးချက်ဖြင့် ပြန်သိမ်းနိုင်သည်** | • **EMR Task Nodes** (HDFS ဒေတာ မသိမ်းသော Compute Node များ)<br/>• **AWS Batch jobs with S3 checkpointing**<br/>• Distributed ML Model Training |
| **Compute Savings Plans / EC2 Savings Plans** | **၇၂% အထိ လျှော့စျေး** | **လုံးဝမရှိပါ** (၁ နှစ် သို့မဟုတ် ၃ နှစ် ကတိကဝတ်) | • ၂၄/၇ Production Databases (`[[rds-and-aurora]]`)<br/>• အမြဲလည်ပတ်နေသော **EMR Master & Core Nodes**<br/>• **Amazon MSK** Kafka Broker Fleets |

---

## ၃။ Spot Instances & Fault-Tolerant Big Data Topologies

```mermaid
sequenceDiagram
    autonumber
    actor Task as EMR Task Node / Batch Spot Worker
    participant Event as Amazon EventBridge / Instance Metadata
    participant S3 as Amazon S3 Data Lake (Checkpoint Store)
    participant AWS as AWS EC2 Capacity Pool

    AWS->>Event: (1) Emits EC2 Spot Interruption Warning (2-minute timer starts)
    Event->>Task: (2) Notifies worker process / Spark Executor
    Task->>S3: (3) Flushes in-flight memory partition state & writes checkpoint.parquet
    Task->>AWS: (4) Gracefully exits before instance termination
    AWS->>Task: (5) Terminates Spot instance
    AWS->>Task: (6) New Spot/On-Demand instance launched from deeper capacity pool
    Task->>S3: (7) Reads latest checkpoint and resumes processing seamlessly!
```

### EMR Cluster Node Mapping Strategy (စာမေးပွဲ အဓိက မေးခွန်းပုံစံ)

```mermaid
graph TD
    subgraph EMRClusterTopology["Amazon EMR Cluster Node Mapping"]
        subgraph MasterLayer["(1) Master Node"]
            M1["Master Node<br/>• YARN ResourceManager & HDFS NameNode<br/>• တစ်ခုတည်းသော ဦးစီးဆာဗာ<br/>🛑 NEVER use Spot Instances! (Master သေပါက Cluster တစ်ခုလုံး ပျက်သည်)<br/>✅ Use On-Demand or Savings Plans"]
        end

        subgraph CoreLayer["(2) Core Nodes"]
            C1["Core Nodes<br/>• DataNode (HDFS ဒေတာ သိမ်းသည်) & NodeManager<br/>⚠️ Core Node ရပ်တန့်ခံရပါက HDFS Data Loss ဖြစ်နိုင်သည်<br/>✅ Use On-Demand or Savings Plans"]
        end

        subgraph TaskLayer["(3) Task Nodes"]
            T1["Task Nodes<br/>• Pure compute workers (Spark Executors / NodeManager)<br/>• STORES ZERO HDFS DATA!<br/>✅ 100% Spot Instances (အချိန်မရွေး ထပ်တိုး/လျှော့/ရပ်တန့် နိုင်သည်)"]
        end
    end

    classDef master fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef core fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef task fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class M1 master;
    class C1 core;
    class T1 task;
```

---

## ၄။ AWS Graviton Processors in Data Engineering (Arm Architecture)

```mermaid
graph LR
    subgraph GravitonFamilies["AWS Graviton Instance Families"]
        GenPurpose["General Purpose: M7g, T4g<br/>(Kafka, Web, Microservices)"]
        ComputeOpt["Compute Optimized: C7g, C6g<br/>(Batch compute, Spark worker nodes)"]
        MemOpt["Memory Optimized: R7g, X2gd<br/>(Redis, OpenSearch, In-Memory Spark)"]
        StorageOpt["Storage Optimized: Im4gn, Is4gen<br/>(High-throughput NVMe SSD data stores)"]
        AccelOpt["Accelerated / ML: G5g<br/>(Arm-based ML inference)"]
    end

    classDef grav fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    class GenPurpose,ComputeOpt,MemOpt,StorageOpt,AccelOpt grav;
```

### Graviton Adoption Across AWS Data Services

| Managed Service | Graviton Instance Option | Data Engineering အကျိုးကျေးဇူး |
| :--- | :--- | :--- |
| **Amazon EMR** | `c7g`, `m7g`, `r7g` | Apache Spark၊ Hive နှင့် Presto များတွင် **၃၀% စျေးသက်သာပြီး ၁၅% ပိုမိုမြန်ဆန်သည်**။ |
| **Amazon MSK (Kafka)** | `kafka.m7g.*` | Streaming Ingest တွင် Throughput ပိုမိုမြင့်မားပြီး Latency နည်းပါးသည်။ |
| **Amazon RDS & Aurora** | `db.r7g.*`, `db.m7g.*` | PostgreSQL နှင့် MySQL များတွင် **၂၀% ပိုမိုကောင်းမွန်သော Transaction Throughput** ကို ရရှိသည်။ |
| **Amazon OpenSearch** | `r7g.search.*`, `m7g.search.*`| Indexing Throughput **၃၈% ပိုမိုမြန်ဆန်သည်**။ |
| **AWS Lambda** | **`arm64` Architecture** | x86_64 နှင့် နှိုင်းယှဉ်ပါက Duration ကုန်ကျစရိတ် **၂၀% ပိုမိုသက်သာသည်**။ |

---

## ၅။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Cost-optimized compute for fault-tolerant, stateless ETL and ML with checkpointing"** $\rightarrow$ **EC2 Spot Instances**.
> - **"EMR Task nodes compute selection"** $\rightarrow$ **Spot Instances** (Task node များသည် HDFS ဒေတာ မသိမ်းဆည်းပါ).
> - **"EMR Master node compute selection"** $\rightarrow$ **On-Demand သို့မဟုတ် Reserved Instances** (Spot လုံးဝ မသုံးရပါ!).
> - **"Best price-performance for managed data services (EMR, MSK, RDS, OpenSearch, Lambda)"** $\rightarrow$ **AWS Graviton (Arm-based instances with 'g' suffix, e.g. `m7g`, `r7g`, `c7g`)**.

> [!WARNING]
> **Exam Traps (သတိထားရမည့် အချက်များ)**:
> 1. **Spot Instances for EMR Master Nodes Trap**: EMR Master Node တွင် Spot Instances ကို လုံးဝ မရွေးချယ်ရပါ။ Master ပြုတ်ကျပါက Cluster တစ်ခုလုံး ပျက်စီးပြီး လုပ်လက်စ အားလုံး ဆုံးရှုံးသည်။
> 2. **Graviton Binary Compatibility**: Graviton သည် Arm64 ဖြစ်သဖြင့် Python၊ PySpark၊ Java များသည် အဆင်ပြေစွာ Run နိုင်သော်လည်း Custom C/C++ Binaries များကို Docker Container သွင်းမည်ဆိုပါက `linux/arm64` ဖြင့် Compile လုပ်ထားရမည်။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[emr]]` — Amazon EMR Master/Core/Task Node ဖွဲ့စည်းပုံ
- `[[batch]]` — AWS Batch Spot-driven Batch Compute
- `[[lambda]]` — AWS Lambda Arm64 Graviton Architecture
- `[[ecr-ecs-eks]]` — Containers on EC2, Fargate, and EKS
- `[[msk-kafka]]` — Amazon MSK Graviton Broker Deployment
