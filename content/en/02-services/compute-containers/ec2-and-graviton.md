---
title: Amazon EC2 & AWS Graviton in Big Data
type: aws-service
category: Compute
tags:
  - aws/service
  - dea-c01
  - compute/ec2
  - compute/graviton
  - spot-instances
  - emr
date: 2026-08-14
---

# 🖥️ Amazon EC2 & AWS Graviton in Big Data (Purchasing Models & Arm Architecture)

- **Category**: Compute (Virtual Machine Infrastructure, Spot Pricing & Arm Processors)
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/compute-containers/ec2-and-graviton)
- **Primary Use Case**: Compute backbone for self-hosted data platforms, underlying instance topology for [[emr]] clusters (Master, Core, Task nodes), and maximizing price-performance using custom **AWS Graviton** silicon across [[msk-kafka]], [[rds-and-aurora]], [[opensearch]], and [[lambda]].
- **Slide Reference**: Pages 286–288 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]] | [[domain-2-data-store-management]] | [[emr]] | [[batch]] | [[ecr-ecs-eks]] | [[lambda]]

---

## 1. High-Level Summary

**Amazon Elastic Compute Cloud (Amazon EC2)** provides scalable on-demand compute capacity in the AWS Cloud. In data engineering architectures, EC2 instances form the core compute substrate powering distributed big data clusters (**Amazon EMR**), managed databases (**Amazon RDS/Aurora**), streaming brokers (**Amazon MSK**), and custom containerized ETL fleets.

**AWS Graviton Processors** are custom 64-bit Arm Neoverse-based microprocessors engineered by AWS to deliver up to **40% better price-performance** over comparable x86 processors across databases, analytics, memory caches, and containerized microservices.

For the **AWS Certified Data Engineer – Associate (DEA-C01)** exam, you must master:
1. **EC2 Purchasing Models**: On-Demand vs. Spot Instances vs. Reserved Instances (RI) / Savings Plans.
2. **Spot Instances for Analytics**: Leveraging Spot for stateless, fault-tolerant workloads (e.g. EMR Task nodes, AWS Batch) with **S3 state checkpointing** to survive 2-minute interruption notices.
3. **EMR Cluster Node Architecture**: Mapping EC2 purchasing models across **Master Nodes** (On-Demand), **Core Nodes** (On-Demand/Reserved), and **Task Nodes** (Spot).
4. **AWS Graviton Instance Families**: Identifying Graviton-powered instance types (`c7g`, `m7g`, `r7g`, `is4gen`) across AWS analytics and data services.

```mermaid
graph TB
    subgraph PurchasingModels["EC2 Purchasing Models"]
        OnDemand["(1) On-Demand Instances<br/>• Full flexibility, no commitment<br/>• Pay per second / hour<br/>🎯 Short-term, spiky, unpredictable jobs"]
        SpotInst["(2) Spot Instances<br/>• Up to 90% discount over On-Demand<br/>• Reclaimable with 2-min warning<br/>🎯 Fault-tolerant, stateless ETL & ML"]
        SavingsPlans["(3) Reserved Instances / Savings Plans<br/>• 1 or 3-Year commitment<br/>• Up to 72% discount<br/>🎯 24/7 Steady-state baseline clusters"]
    end

    subgraph EMRClusterMapping["Amazon EMR Cluster Topology"]
        MasterNode["Master Node (YARN ResourceManager / NameNode)<br/>🔒 MUST use On-Demand / Reserved Instances!"]
        CoreNode["Core Nodes (HDFS DataNodes + Compute)<br/>🛡️ On-Demand / Reserved (Prevents HDFS Data Loss)"]
        TaskNode["Task Nodes (Pure Compute / No HDFS)<br/>💰 100% Spot Instances (Safe to scale & terminate)"]
    end

    subgraph GravitonSilicon["AWS Graviton Silicon (Arm Architecture)"]
        GravitonChip["AWS Graviton3 / Graviton4<br/>⚡ 40% Better Price-Performance<br/>🌱 60% Lower Energy Consumption"]
        
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

## 2. EC2 Purchasing Options for Data Engineering Workloads

| Purchasing Option | Cost Discount | Interruption Risk | Best Data Engineering Workload |
| :--- | :--- | :--- | :--- |
| **On-Demand** | Baseline price ($0\%$) | **None** (Guaranteed availability until stopped) | • Dev/Test environments<br/>• Short, non-interruptible one-off data processing<br/>• EMR Master nodes |
| **Spot Instances** | **Up to 90% discount** | ⚠️ **Can be reclaimed by AWS with a 2-minute warning** | • **EMR Task Nodes** (Pure compute, no HDFS storage)<br/>• **AWS Batch jobs with S3 checkpointing**<br/>• Distributed ML model training & hyperparameter tuning |
| **Compute Savings Plans / EC2 Instance Savings Plans** | **Up to 72% discount** | **None** (1-year or 3-year hourly spend commitment) | • 24/7 Production databases ([[rds-and-aurora]])<br/>• Long-running continuous **EMR Master & Core nodes**<br/>• 24/7 **Amazon MSK** Kafka broker fleets |

---

## 3. Spot Instances & Fault-Tolerant Big Data Topologies

Spot Instances represent unused EC2 compute capacity available at steep discounts. However, when AWS needs capacity back, the instance receives a **2-minute rebalance recommendation / interruption notice**.

```mermaid
sequenceDiagram
    autonumber
    actor Task as EMR Task Node / Batch Spot Worker
    participant Event as Amazon EventBridge / Instance Metadata
    participant S3 as Amazon S3 Data Lake (Checkpoint Store)
    participant AWS as AWS EC2 Capacity Pool

    AWS->>Event: 1. Emits EC2 Spot Interruption Warning (2-minute timer starts)
    Event->>Task: 2. Notifies worker process / Spark Executor
    Task->>S3: 3. Flushes in-flight memory partition state & writes checkpoint.parquet
    Task->>AWS: 4. Gracefully exits before instance termination
    AWS->>Task: 5. Terminates Spot instance
    AWS->>Task: 6. New Spot/On-Demand instance launched from deeper capacity pool
    Task->>S3: 7. Reads latest checkpoint and resumes processing seamlessly!
```

### EMR Cluster Node Mapping Strategy (Top Exam Focus):

```mermaid
graph TD
    subgraph EMRClusterTopology["Amazon EMR Cluster Node Mapping"]
        subgraph MasterLayer["(1) Master Node"]
            M1["Master Node<br/>• Runs YARN ResourceManager & HDFS NameNode<br/>• Single point of coordination<br/>🛑 NEVER use Spot Instances! (Cluster dies if master terminates)<br/>✅ Use On-Demand or Savings Plans"]
        end

        subgraph CoreLayer["(2) Core Nodes"]
            C1["Core Nodes<br/>• Runs DataNode (stores HDFS data) & NodeManager<br/>⚠️ Terminating a Core node risks HDFS data loss / under-replication<br/>✅ Use On-Demand or Savings Plans (or conservative Spot with high minimums)"]
        end

        subgraph TaskLayer["(3) Task Nodes"]
            T1["Task Nodes<br/>• Pure compute workers (Runs Spark Executors / NodeManager)<br/>• STORES ZERO HDFS DATA!<br/>✅ 100% Spot Instances (Safe to add, drop, or interrupt dynamically)"]
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

## 4. AWS Graviton Processors in Data Engineering

AWS Graviton processors are custom-built 64-bit Arm processors designed by AWS using 7nm/5nm silicon technology:

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

### Graviton Adoption Across AWS Managed Data Services

| Managed Service | Graviton Instance Option | Benefits for Data Engineering |
| :--- | :--- | :--- |
| **Amazon EMR** | `c7g`, `m7g`, `r7g` | Up to **30% lower cost** and **15% higher performance** for Apache Spark, Hive, and Presto jobs compared to equivalent x86 instances. |
| **Amazon MSK (Kafka)** | `kafka.m7g.*` | Higher network throughput per dollar and reduced tail latency for high-volume streaming ingest. |
| **Amazon RDS & Aurora** | `db.r7g.*`, `db.m7g.*` | Delivers up to **20% better transaction throughput** for PostgreSQL and MySQL workloads at lower cost. |
| **Amazon OpenSearch** | `r7g.search.*`, `m7g.search.*`| Up to **38% indexing throughput improvement** and 20% query latency reduction for search clusters. |
| **AWS Lambda** | **`arm64` Architecture** | **20% lower price** per millisecond of compute duration compared to `x86_64` for identical Python/Node/Java functions. |

---

## 5. High-Yield DEA-C01 Exam Tips & Traps

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Cost-optimized compute for fault-tolerant, stateless ETL and machine learning with checkpointing"** $\rightarrow$ **EC2 Spot Instances**.
> - **"EMR Task nodes compute selection"** $\rightarrow$ **Spot Instances** (Task nodes store no HDFS data and can be terminated safely).
> - **"EMR Master node compute selection"** $\rightarrow$ **On-Demand or Reserved Instances** (Never Spot!).
> - **"Best price-performance for managed data services (EMR, MSK, RDS, OpenSearch, Lambda)"** $\rightarrow$ **AWS Graviton (Arm-based instance types with 'g' suffix, e.g. `m7g`, `r7g`, `c7g`)**.

> [!WARNING]
> **Exam Traps & Failure Modes**:
> 1. **Spot Instances for EMR Master Nodes Trap**:
>    - Never select Spot Instances for the **Master Node** of an Amazon EMR cluster. If the master node is reclaimed, the entire cluster fails and all job progress is lost!
> 2. **Spot Interruption Mitigation**:
>    - When using Spot instances for data processing, always implement **state checkpointing to Amazon S3** so that when an instance is reclaimed, the retry job resumes from the latest checkpoint rather than restarting from scratch.
> 3. **Graviton Binary Compatibility**:
>    - Graviton runs on the **Arm64** instruction set. While Python, PySpark, Java, and Node.js code run with zero modifications, custom compiled C/C++ or Go binaries packaged into Docker containers must be compiled specifically for `linux/arm64`.

---

## 📌 Related Notes

- [[emr]] — Amazon EMR cluster architecture, Master/Core/Task node mapping
- [[batch]] — AWS Batch for spot-driven containerized batch computing
- [[lambda]] — AWS Lambda Arm64 Graviton execution architecture
- [[ecr-ecs-eks]] — Running containers on EC2, Fargate, and EKS
- [[msk-kafka]] — Amazon MSK Graviton broker deployment
- [[domain-1-ingestion-and-processing]] — DEA-C01 Domain 1 Study Guide
- [[service-comparisons]] — Master DEA-C01 Service Decision Matrix
