---
title: Amazon RDS & Amazon Aurora (မြန်မာဘာသာ)
type: aws-service
category: Database
tags:
  - aws/service
  - dea-c01
  - database/relational
  - rds
  - aurora
  - postgresql
  - mysql
  - burmese
date: 2026-08-15
---

# 🐘 Amazon RDS & Amazon Aurora (Managed Relational OLTP Databases) (စီမံခန့်ခွဲပေးထားသော Relational OLTP ဒေတာဘေ့စ်များ)

- **Category**: Database (Relational OLTP & Cloud-Native Storage)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/database/rds-and-aurora.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Transactional Operational Workloads များအတွက် စီမံခန့်ခွဲပေးထားသော Relational Databases၊ ACID Transactions၊ `[[dms-and-sct]]` ဖြင့် Change Data Capture (CDC) ရယူခြင်း၊ `[[redshift]]` သို့ Zero-ETL Integration နှင့် Amazon S3 သို့ Parquet တိုက်ရိုက် Export ပြုလုပ်ခြင်း။
- **Slide Reference**: Pages 196–213 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[redshift]]` | `[[dms-and-sct]]` | `[[s3]]` | `[[kms-and-secrets]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**Amazon Relational Database Service (Amazon RDS)** သည် Cloud ပေါ်တွင် Relational Database များကို လွယ်ကူစွာ တည်ဆောက်၊ စီမံခန့်ခွဲနိုင်စေသည့် Fully Managed Web Service ဖြစ်ပြီး Database Engine ၆ မျိုး (**Amazon Aurora**၊ **PostgreSQL**၊ **MySQL**၊ **MariaDB**၊ **Oracle** နှင့် **Microsoft SQL Server**) ကို ထောက်ပံ့ပေးသည်။

**Amazon Aurora** သည် AWS ၏ MySQL နှင့် PostgreSQL compatible ဖြစ်သော Cloud-Native Database Engine ဖြစ်သည်။ Aurora သည် Compute နှင့် Storage ကို Decoupled ခွဲထုတ်ထားပြီး Availability Zones (AZs) ၃ ခုအတွင်း Distributed Storage Subsystem ကို အသုံးပြုထားသဖြင့် သမားရိုးကျ **MySQL ထက် ၅ ဆ**၊ **PostgreSQL ထက် ၃ ဆ ပိုမိုမြန်ဆန်သော Throughput** ကို ပေးစွမ်းသည်။

```mermaid
graph TB
    subgraph ComputeLayer["Compute & Transaction Layer"]
        AppWrites["Application Writes / OLTP"]
        AppReads["Read-Heavy Web Traffic"]
        AnalyticsQueries["Data Engineering / BI Reports"]
    end

    subgraph AuroraCluster["Amazon Aurora Multi-AZ Cluster"]
        WriterNode["Aurora Primary Instance (Writer)<br/>⚡ Cluster Endpoint"]
        
        subgraph ReaderNodes["Aurora Read Replicas (Up to 15)"]
            Reader1["Read Replica 1<br/>⚡ Reader Endpoint"]
            Reader2["Read Replica 2<br/>⚡ Custom Endpoint (BI)"]
        end
        
        subgraph StorageLayer["Aurora Distributed Storage Fleet (3 AZs)"]
            AZ1[("AZ-a<br/>Copy 1 & Copy 2")]
            AZ2[("AZ-b<br/>Copy 3 & Copy 4")]
            AZ3[("AZ-c<br/>Copy 5 & Copy 6")]
        end
    end

    subgraph AnalyticsExport["Analytics & Data Lake Integrations"]
        S3Snapshot["S3 Snapshot Export (Parquet)"]
        ZeroETL["Amazon Redshift Zero-ETL Ingestion"]
        DMSCapture["AWS DMS (CDC via Binlog/WAL)"]
    end

    AppWrites --> WriterNode
    AppReads --> Reader1
    AnalyticsQueries --> Reader2

    WriterNode <--> StorageLayer
    Reader1 <--> StorageLayer
    Reader2 <--> StorageLayer

    StorageLayer --> S3Snapshot
    StorageLayer --> ZeroETL
    WriterNode --> DMSCapture

    classDef client fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef aurora fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef ana fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;

    class AppWrites,AppReads,AnalyticsQueries client;
    class WriterNode,ReaderNodes,Reader1,Reader2 aurora;
    class StorageLayer,AZ1,AZ2,AZ3 store;
    class AnalyticsExport,S3Snapshot,ZeroETL,DMSCapture ana;
```

---

## ၂။ Multi-AZ Deployments vs. Read Replicas (Core Exam Focus)

```mermaid
graph TD
    subgraph MultiAZ["Multi-AZ Deployments (Disaster Recovery & High Availability)"]
        PrimaryDB["Primary DB Instance (AZ-a)<br/>(Active Read/Write)"]
        StandbyDB["Standby DB Instance (AZ-b)<br/>(Passive Synchronous Replica)"]
        PrimaryDB <-->|"Synchronous Replication"| StandbyDB
        MultiAZDesc["• ရည်ရွယ်ချက်- High Availability & Automatic Failover<br/>• Standby Instance ကို Read လုပ်ရန် အသုံးမပြုနိုင်ပါ (No Read Offload)<br/>• DNS Failover ဖြင့် ၆၀ စက္ကန့်အတွင်း အလိုအလျောက် ပြောင်းလဲပေးသည်"]
    end

    subgraph ReadReplicas["Read Replicas (Read Scalability & Analytics Offload)"]
        MasterDB["Primary DB Instance"]
        RR1["Read Replica 1 (AZ-a)"]
        RR2["Read Replica 2 (AZ-b)"]
        RR3["Cross-Region Replica (eu-west-1)"]
        MasterDB -->|"Asynchronous Replication"| RR1
        MasterDB -->|"Asynchronous Replication"| RR2
        MasterDB -->|"Asynchronous Replication"| RR3
        RRDesc["• ရည်ရွယ်ချက်- Read Performance တိုးမြှင့်ခြင်း & Analytics Queries Offloading<br/>• Read Replicas အသီးသီးတွင် သီးခြား Connection Endpoint ရှိသည်<br/>• RDS တွင် အများဆုံး ၅ ခု၊ Aurora တွင် အများဆုံး ၁၅ ခု ထားရှိနိုင်သည်"]
    end

    classDef maz fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef rr fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class MultiAZ,PrimaryDB,StandbyDB,MultiAZDesc maz;
    class ReadReplicas,MasterDB,RR1,RR2,RR3,RRDesc rr;
```

---

## ၃။ Aurora Distributed Storage Architecture

- **6-Way Replication Across 3 AZs**: Aurora သည် ဒေတာ Block တစ်ခုချင်းစီကို Availability Zones ၃ ခုအတွင်း ကော်ပီ ၆ စောင် (AZ တစ်ခုစီတွင် ၂ စောင်စီ) အလိုအလျောက် သိမ်းဆည်းသည်။
- **Write Quorum (4 of 6)**: AZ တစ်ခုလုံး ပျက်စီးသွားပြီး အပို Node တစ်ခု ထပ်မံပျက်စီးသည့်တိုင် (2 of 6 down) Write Availability မပျက်စီးဘဲ ဆက်လက် အလုပ်လုပ်နိုင်သည်။
- **Read Quorum (3 of 6)**: AZ တစ်ခုလုံး ပျက်စီးသည့်တိုင် (3 of 6 down) Read Availability မပျက်စီးပါ။
- **Auto-Expanding Storage**: Storage ကို 10 GB မှစတင်၍ **128 TB အထိ** အလိုအလျောက် တိုးချဲ့ပေးသည်။

---

## ၄။ Data Lake & Analytics Integration Patterns

```mermaid
graph LR
    subgraph OperationalDB["Amazon Aurora / RDS Engine"]
        AuroraEngine["Aurora PostgreSQL / MySQL"]
    end

    subgraph S3Integration["Amazon S3 Data Lake (Parquet Export)"]
        DirectSQL["aws_s3 Extension (SELECT aws_s3.query_export_to_s3)"]
        SnapshotExport["RDS Snapshot Export to Amazon S3<br/>(Automated Parquet conversion via Glue/Athena)"]
    end

    subgraph RedshiftIntegration["Amazon Redshift Zero-ETL"]
        ZeroETLChannel["Near-Real-Time CDC Ingestion (Zero-ETL)"]
    end

    AuroraEngine --> DirectSQL
    AuroraEngine --> SnapshotExport
    AuroraEngine --> ZeroETLChannel

    classDef db fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef s3 fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef rs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;

    class OperationalDB,AuroraEngine db;
    class S3Integration,DirectSQL,SnapshotExport s3;
    class RedshiftIntegration,ZeroETLChannel rs;
```

1. **Amazon Redshift Zero-ETL Integration**: Aurora MySQL/PostgreSQL မှ Transactional Data များကို Redshift သို့ Complex Data Pipeline ရေးစရာမလိုဘဲ စက္ကန့်ပိုင်းအတွင်း Replicate လုပ်ပေးသည်။
2. **RDS Snapshot Export to Amazon S3**: RDS Backup Snapshots များကို **Apache Parquet** ဖော်မတ်ဖြင့် S3 ပေါ်သို့ တိုက်ရိုက် Export လုပ်ပေးသည်။ AWS Glue Data Catalog နှင့် ချိတ်ဆက်၍ Athena ဖြင့် ချက်ချင်း Query လုပ်နိုင်သည်။

---

## ၅။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Offload heavy reporting and BI queries from production transactional database"** $\rightarrow$ **Create Read Replicas (RDS) / Aurora Read Replicas with Custom Endpoint**.
> - **"High availability and automatic synchronous failover across AZs"** $\rightarrow$ **RDS Multi-AZ Deployment**.
> - **"Transactional replication to Redshift without writing ETL pipelines"** $\rightarrow$ **Amazon Aurora Zero-ETL integration with Amazon Redshift**.
> - **"Export RDS historical snapshot data to S3 in columnar format for Athena querying"** $\rightarrow$ **RDS Snapshot Export to S3 (converts to Apache Parquet automatically)**.
> - **"Capture incremental changes from relational database in real-time"** $\rightarrow$ **AWS DMS with Change Data Capture (CDC) reading from WAL / Binlogs**.

> [!WARNING]
> **Exam Traps (သတိထားရမည့် အချက်များ)**:
> 1. **Multi-AZ vs. Read Replica Trap**: စာမေးပွဲတွင် "Reporting queries are slowing down production DB" ဟု မေးပါက Multi-AZ ကို မရွေးပါနှင့် (Multi-AZ Standby သည် Query ဖတ်မရပါ); **Read Replica** ကိုသာ ရွေးချယ်ပါ။
> 2. **IAM Database Auth Token Expiration**: IAM DB Auth ဖြင့် ရရှိသော Authentication Token များသည် **၁၅ မိနစ်သာ** သက်တမ်းရှိသည်။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[redshift]]` — Amazon Redshift & Zero-ETL Ingestion
- `[[dms-and-sct]]` — AWS DMS Database Migration & CDC
- `[[s3]]` — RDS Snapshot Parquet Exports to S3
- `[[dynamodb]]` — NoSQL DynamoDB vs. Relational RDS
