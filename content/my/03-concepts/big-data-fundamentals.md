---
title: Big Data Fundamentals & Data Lake Architecture (မြန်မာဘာသာ)
type: concept
tags:
  - concept/data-engineering
  - dea-c01
  - fundamentals
  - data-lake
  - medallion-architecture
  - burmese
date: 2026-08-15
---

# 🌐 Big Data Fundamentals & Data Lake Architecture (ဘစ်ဒေတာ အခြေခံနှင့် Data Lake တည်ဆောက်ပုံ)

- **Category**: Fundamentals (ဒေတာ အင်ဂျင်နီယာ အခြေခံသဘောတရားများ)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/03-concepts/big-data-fundamentals.md) | **မြန်မာဘာသာ (Burmese)**
- **Slide Reference**: Pages 12–37 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[service-catalog]]` | `[[domain-1-ingestion-and-processing]]` | `[[domain-2-data-store-management]]` | `[[s3]]` | `[[redshift]]` | `[[glue]]`

---

## ၁။ Big Data ၏ အခြေခံ ဝိသေသလက္ခဏာ ၅ ရပ် (The 5 V's of Big Data)

Big Data ဆိုသည်မှာ ရိုးရိုး Database များ (RDBMS) ဖြင့် သိုလှောင်ကိုင်တွယ်ရန် မဖြစ်နိုင်သော ပမာဏကြီးမားပြီး ရှုပ်ထွေးသည့် ဒေတာများကို ရည်ညွှန်းပြီး အောက်ပါ **5 V's** ဖြင့် သတ်မှတ်ပါသည်-

```mermaid
mindmap
  root((Big Data 5 V's))
    Volume (ပမာဏ)
      Terabytes မှ Petabytes အထိ
      Decoupled S3 Storage
    Velocity (အလျင်နှုန်း)
      Real-time Streams နှင့် Batch Ingestion
      Kinesis / MSK / Firehose
    Variety (အမျိုးအစားစုံလင်မှု)
      Structured SQL Tables
      Semi-Structured JSON / Parquet
      Unstructured Images / Audio / Video
    Veracity (တိကျမှန်ကန်မှု)
      Data Quality & Trustworthiness
      Glue Data Quality / Validation
    Value (တန်ဖိုးဖန်တီးမှု)
      Actionable BI & ML Predictions
      QuickSight / SageMaker
```

1. **Volume (ပမာဏ)**: Gigabytes မှ Terabytes နှင့် Petabytes အထိ များပြားလာသော ဒေတာပမာဏ။ AWS တွင် စျေးသက်သာပြီး အကန့်အသတ်မရှိ သိမ်းဆည်းနိုင်သော **Amazon S3** ကို Decoupled Storage အဖြစ် အသုံးပြုသည်။
2. **Velocity (စီးဆင်းမှု အလျင်နှုန်း)**: ဒေတာများ ဝင်ရောက်လာသည့် အမြန်နှုန်း။ ဥပမာ - IoT Sensors များနှင့် Clickstream ဒေတာများကို **Amazon Kinesis Data Streams** နှင့် **Amazon MSK (Apache Kafka)** ဖြင့် Real-time ရယူခြင်း။
3. **Variety (အမျိုးအစား စုံလင်မှု)**: 
   - **Structured (ပုံစံတကျ)**: RDBMS၊ CSV၊ SQL Tables။
   - **Semi-Structured (တစ်စိတ်တစ်ပိုင်း ပုံစံရှိ)**: JSON၊ XML၊ Apache Avro၊ Apache Parquet၊ ORC။
   - **Unstructured (ပုံစံမဲ့)**: ရုပ်ပုံများ၊ ဗီဒီယိုများ၊ အသံဖိုင်များနှင့် Raw Server Logs။
4. **Veracity (ဒေတာ တိကျမှန်ကန်မှုနှင့် ယုံကြည်စိတ်ချရမှု)**: ဒေတာများအတွင်း Null values များ၊ ပျက်စီးနေသော ဒေတာများကို **AWS Glue Data Quality (DQDL)** ဖြင့် စစ်ဆေးသန့်စင်ခြင်း။
5. **Value (စီးပွားရေးဆိုင်ရာ တန်ဖိုး)**: သန့်စင်ပြီး ဒေတာများမှ Business Intelligence (BI) နှင့် Machine Learning (ML) အသုံးချမှုများ ရယူဖန်တီးခြင်း (**Amazon QuickSight**, **Amazon SageMaker**).

---

## ၂။ Decoupled Storage and Compute Principle (သိုလှောင်မှုနှင့် တွက်ချက်မှုကို သီးခြားစီ ခွဲထုတ်ခြင်း)

Cloud Data Architecture ၏ အခြေခံအကျဆုံး ဒီဇိုင်းမှာ **Storage နှင့် Compute ကို သီးခြားစီ ခွဲထုတ်ထားခြင်း** ဖြစ်သည်-

```mermaid
graph LR
    subgraph StorageLayer["Decoupled Storage Layer (သိုလှောင်မှု အလွှာ)"]
        S3Bucket[("Amazon S3 Data Lake<br/>(ဗဟို ဒေတာ သိုလှောင်ကန်)")]
    end

    subgraph ComputeEngines["Independent Compute Engines (တွက်ချက်မှု အင်ဂျင်များ)"]
        Athena["Amazon Athena<br/>(Serverless Interactive SQL)"]
        EMR["Amazon EMR<br/>(Distributed Spark / Hadoop)"]
        Glue["AWS Glue ETL<br/>(Serverless PySpark)"]
        Redshift["Amazon Redshift<br/>(Data Warehouse / Spectrum)"]
        SageMaker["Amazon SageMaker<br/>(ML Feature Training)"]
    end

    S3Bucket <--> Athena
    S3Bucket <--> EMR
    S3Bucket <--> Glue
    S3Bucket <--> Redshift
    S3Bucket <--> SageMaker

    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef comp fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;

    class S3Bucket store;
    class Athena,EMR,Glue,Redshift,SageMaker comp;
```

- **ရိုးရာ On-Premise စနစ်**: Storage နှင့် Compute သည် Physical Server များတွင် တွဲလျက်ရှိသဖြင့် Storage တိုးချဲ့လိုပါက မလိုအပ်သော Compute Server များကိုပါ တွဲဖက်ဝယ်ယူရသည်။
- **AWS Cloud စနစ်**: ဒေတာများကို စျေးသက်သာပြီး Durability 99.999999999% (11 9's) ရှိသော **Amazon S3** ပေါ်တွင် သိမ်းဆည်းထားပြီး လိုအပ်သည့်အခါမှ Athena၊ Glue၊ EMR ကဲ့သို့သော Compute Engine များကို သီးခြားခေါ်ယူ အသုံးပြုကာ အလုပ်ပြီးပါက ကုန်ကျစရိတ် သုည ($0) အထိ ပိတ်ထားနိုင်သည်။

---

## ၃။ Data Warehouse vs. Data Lake vs. Data Swamp နှိုင်းယှဉ်ချက်

```mermaid
graph TD
    subgraph DWH["Data Warehouse (Amazon Redshift)"]
        DWH_Desc["• Schema-on-Write<br/>• Structured Relational / OLAP<br/>• Fast SQL & BI Reporting"]
    end

    subgraph DL["Data Lake (Amazon S3)"]
        DL_Desc["• Schema-on-Read<br/>• Multi-Format (Raw, Parquet, JSON)<br/>• Decoupled Storage & Compute"]
    end

    subgraph DS["Data Swamp (သတိထားရမည့် Anti-Pattern)"]
        DS_Desc["• Ungoverned Data Dump<br/>• Zero Metadata / No Catalog<br/>• Unsearchable & Incurring Idle Costs"]
    end

    classDef dwh fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef dl fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef ds fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;

    class DWH,DWH_Desc dwh;
    class DL,DL_Desc dl;
    class DS,DS_Desc ds;
```

| အချက်အလက် (Characteristic) | Data Warehouse (e.g. `[[redshift]]`) | Data Lake (e.g. `[[s3]]`) | Data Swamp (အမှိုက်ပုံသဖွယ် ဖြစ်နေသော Data) |
| :--- | :--- | :--- | :--- |
| **Data Structure** | **Schema-on-Write**: ဒေတာမထည့်မီ Table Schema ကို ကြိုတင်သတ်မှတ်ရသည်။ | **Schema-on-Read**: မူရင်းဒေတာကို သိမ်းဆည်းထားပြီး ဖတ်ယူသည့်အခါမှ Schema သတ်မှတ်သည်။ | Governance မရှိဘဲ စည်းမဲ့ကမ်းမဲ့ စုပုံထားသော ဒေတာများ။ |
| **Data Formats** | Structured (Relational / Tabular OLAP) ဒေတာများသာ။ | Structured၊ Semi-structured (JSON, Parquet)၊ Unstructured ဒေတာအားလုံး။ | မည်သည့်ဒေတာမဆို ဖော်မတ်မဲ့ ရောထွေးနေသည်။ |
| **Storage vs. Compute** | Managed Scaling (Redshift Serverless သို့မဟုတ် Provisioned Cluster)။ | **Fully Decoupled**: သိုလှောင်မှု (S3) နှင့် တွက်ချက်မှု (Athena/Spark) ကို သီးခြားစီ ခွဲထားသည်။ | Decoupled ဖြစ်သော်လည်း ရှာဖွေရယူရန် မဖြစ်နိုင်။ |
| **Governance & Catalog** | Strict ACID Transactions & Table Constraints | `[[lake-formation]]` နှင့် `[[glue]]` Data Catalog ဖြင့် စီမံခန့်ခွဲသည်။ | Metadata Catalog နှင့် လုံခြုံရေး မရှိပါ။ |
| **အဓိက အသုံးပြုသူများ** | Business Analysts, BI Developers, SQL Users | Data Engineers, Data Scientists, ML Engineers | မည်သူမျှ အသုံးမပြုနိုင် (Unusable)။ |

---

## ၄။ Medallion Data Lake Architecture (Tiering Strategy)

Data Lake တစ်ခုအတွင်း ဒေတာအရည်အသွေးကို အဆင့်ဆင့် မြှင့်တင်ရန်အတွက် **Bronze $\rightarrow$ Silver $\rightarrow$ Gold** အဆင့် ၃ ဆင့်ပါဝင်သော Medallion Architecture ကို အသုံးပြုပါသည်-

```mermaid
graph LR
    Raw["(1) Bronze Layer<br/>Raw Data Landing<br/>(CSV / JSON / API Dumps)"] -->|"Glue ETL / DQDL Cleansing"| Silver["(2) Silver Layer<br/>Cleaned & Filtered<br/>(Snappy Parquet / Partitioned)"]
    Silver -->|"Business Aggregations & Joins"| Gold["(3) Gold Layer<br/>Curated Data Marts<br/>(Aggregated Business Views)"]
    Gold --> BI["Amazon QuickSight Dashboards"]
    Gold --> ML["Amazon SageMaker ML Models"]

    classDef b fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef s fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef g fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef c fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;

    class Raw b;
    class Silver s;
    class Gold g;
    class BI,ML c;
```

1. **Bronze Layer (Raw Landing Zone)**:
   - ပြင်ပ System များမှ မူရင်းအတိုင်း ဝင်ရောက်လာသော မပြုပြင်ရသေးသည့် ဒေတာအကြမ်းများ (Raw CSV, JSON, Streaming Logs)။
   - မူရင်းဒေတာကို ပြင်ဆင်ဖျက်ဆီးခွင့်မရှိပါ (Immutable Source of Truth)။
2. **Silver Layer (Processed / Standardized Zone)**:
   - Data Cleansing ပြုလုပ်ထားပြီး၊ Duplicate များကို ဖယ်ရှားကာ Schema စစ်ဆေးပြီးသော ဒေတာများ။
   - ဖတ်ရှုမှု မြန်ဆန်စေရန်အတွက် **Apache Parquet (Snappy Compressed)** ဖော်မတ်သို့ ပြောင်းလဲပြီး Date/Region အလိုက် Partition ခွဲထားသည်။
3. **Gold Layer (Curated / Business Data Marts)**:
   - လုပ်ငန်းသုံး Report များ၊ Dashboard များနှင့် ML Feature Stores များအတွက် လိုအပ်သော Aggregations နှင့် Business Rules များကို ကြိုတင်တွက်ချက်ထားသည့် အဆင့်မြင့် ဒေတာအလွှာ။

---

## ၅။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Decoupled Storage and Compute for Big Data"** $\rightarrow$ **Amazon S3 (Storage) + Amazon Athena / Amazon EMR / AWS Glue (Compute)**။
> - **"Preventing Data Swamp"** $\rightarrow$ **AWS Glue Crawlers** ဖြင့် Catalog ပြုလုပ်ခြင်း နှင့် **AWS Lake Formation** ဖြင့် ဗဟိုမှ Access Control ထိန်းချုပ်ခြင်း။
> - **"Cost-effective analytical querying over S3 data lake"** $\rightarrow$ Raw ဒေတာများကို **Apache Parquet + Snappy Compression** သို့ ပြောင်းလဲသိမ်းဆည်းခြင်း။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[data-formats-and-compression]]` — Parquet, ORC, Avro နှင့် Compression စနစ်များ
- `[[data-modeling-and-partitioning]]` — S3 Partitioning နှင့် Star Schema ပုံစံများ
- `[[data-validation-and-profiling]]` — Glue Data Quality (DQDL) ဖြင့် ဒေတာအရည်အသွေး စစ်ဆေးခြင်း
- `[[s3]]` — Amazon S3 Data Lake ဗိသုကာ
- `[[redshift]]` — Amazon Redshift Data Warehouse
- `[[glue]]` — AWS Glue ETL နှင့် Data Catalog
