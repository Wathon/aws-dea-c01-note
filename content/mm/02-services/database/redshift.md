---
title: Amazon Redshift (မြန်မာဘာသာ)
type: aws-service
category: Database
tags:
  - aws/service
  - dea-c01
  - database/redshift
  - data-warehouse
  - olap
  - redshift-spectrum
  - redshift-serverless
  - zero-etl
  - data-sharing
  - data-api
  - burmese
date: 2026-08-15
---

# 🔴 Amazon Redshift (Petabyte-Scale Cloud Data Warehouse & Lakehouse) (Petabyte အဆင့် Cloud Data Warehouse)

- **Category**: Database (Petabyte-Scale Columnar OLAP Data Warehouse)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/database/redshift.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Enterprise Data Warehousing၊ မြန်ဆန်သော Complex SQL Analytics၊ BI Reporting၊ Redshift Spectrum ဖြင့် Data Lakehouse Query များ ပြုလုပ်ခြင်း၊ Serverless Data Processing၊ Zero-ETL Replication နှင့် Real-time Streaming Ingestion။
- **Slide Reference**: Pages 220–265 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[athena]]` | `[[glue]]` | `[[s3]]` | `[[rds-and-aurora]]` | `[[kinesis]]` | `[[kms-and-secrets]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**Amazon Redshift** သည် Petabyte အဆင့်အထိ Scale လုပ်နိုင်သော Fully Managed Columnar Massively Parallel Processing (MPP) Data Warehouse ဝန်ဆောင်မှု ဖြစ်သည်။ Analytical (OLAP) Query များကို Compute Node များစွာနှင့် Slices များပေါ်တွင် Parallelize တွက်ချက်ပေးခြင်း၊ Columnar Storage Layout နှင့် Hardware-Accelerated Local Cache များကို S3 Decoupled Storage ဖြင့် တွဲဖက် အသုံးပြုထားသဖြင့် သမားရိုးကျ Relational Databases များထက် **၁၀ ဆ ပိုမိုမြန်ဆန်သည်**။

```mermaid
graph TB
    subgraph ClientLayer["Client & BI Interface"]
        SQLClient["SQL Client / JDBC / ODBC / QuickSight"]
        ETLPipelines["Data Pipelines (Glue / Airflow / Step Functions)"]
    end

    subgraph Cluster["Amazon Redshift MPP Cluster Architecture"]
        LeaderNode["Leader Node<br/>⚡ Query Parsing & Execution Planning<br/>⚙️ C++ Code Compilation & Coordination<br/>🚫 User Table Data လုံးဝ မသိမ်းပါ (အခမဲ့ ဖြစ်သည်)"]

        subgraph ComputeNodes["Compute Node Fleet (RA3 Nodes)"]
            subgraph CN1["Compute Node 1"]
                Slice1["Slice 1 (Worker)"]
                Slice2["Slice 2 (Worker)"]
            end
            subgraph CN2["Compute Node 2"]
                Slice3["Slice 3 (Worker)"]
                Slice4["Slice 4 (Worker)"]
            end
        end

        RMS[("Redshift Managed Storage (RMS)<br/>📦 Decoupled S3-Backed Persistent Storage<br/>⚡ Local SSD Cache + Automatic Data Tiering")]
    end

    subgraph ExternalSources["External Data & Federation"]
        S3Lake[("Amazon S3 Data Lake (Parquet/ORC)")]
        AuroraDB[("Amazon Aurora (Zero-ETL / Federated)")]
    end

    SQLClient --> LeaderNode
    ETLPipelines --> LeaderNode

    LeaderNode --> ComputeNodes
    ComputeNodes <--> RMS
    ComputeNodes <-->|"Redshift Spectrum"| S3Lake
    ComputeNodes <-->|"Federated Query / Zero-ETL"| AuroraDB

    classDef client fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef leader fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef comp fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class SQLClient,ETLPipelines client;
    class LeaderNode leader;
    class ComputeNodes,CN1,CN2,Slice1,Slice2,Slice3,Slice4 comp;
    class RMS,S3Lake,AuroraDB store;
```

---

## ၂။ Distribution Styles (DISTSTYLE) မဟာဗျူဟာများ

Table များအတွင်း ဒေတာများကို Node Slices များဆီသို့ ခွဲဝေဖြန့်ကြက်ရန်အတွက် Distribution Styles ၄ မျိုး ရှိပါသည်-

```mermaid
graph TD
    DistChoice{Table အလိုက် DISTSTYLE ရွေးချယ်ခြင်း}
    
    DistChoice -->|"အသေးစား Dimension Tables (< သန်းဂဏန်း Rows)"| DistAll["DISTSTYLE ALL<br/>• Table တစ်ခုလုံးကို Node တိုင်းရှိ Slice တိုင်းပေါ်တွင် ကူးယူသိမ်းသည်<br/>• ကြီးမားသော Fact Table နှင့် Join သည့်အခါ Network Data Shuffling မရှိစေပါ"]
    
    DistChoice -->|"အလွန်ကြီးမားသော Fact Table & Join Key တူညီသည့် နေရာများ"| DistKey["DISTSTYLE KEY (col_name)<br/>• တူညီသော Key တန်ဖိုးရှိသည့် Row များကို Slice တူတူတွင် အတူတကွ သိမ်းသည်<br/>• Colocated Joins ကြောင့် အမြန်ဆုံး Performance ရရှိသည်"]
    
    DistChoice -->|"Uniform Distribution လိုအပ်ပြီး Join Key မသေချာသော အခါ"| DistEven["DISTSTYLE EVEN<br/>• Round-robin နည်းဖြင့် Slice အားလုံးသို့ အညီအမျှ ဖြန့်ဝေသည်<br/>• Data Skew မဖြစ်စေရန် အကာအကွယ်ပေးသည်"]
    
    DistChoice -->|"Default Option (Redshift မှ စီမံခန့်ခွဲသည်)"| DistAuto["DISTSTYLE AUTO<br/>• သေးငယ်ချိန်တွင် ALL ဖြင့် စတင်ပြီး ကြီးမားလာပါက EVEN သို့ ပြောင်းပေးသည်"]

    classDef dec fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef c fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class DistChoice dec;
    class DistAll,DistKey,DistEven,DistAuto c;
```

---

## ၃။ Sort Keys (SORTKEY) နှင့် Zone Maps

Redshift သည် 1 MB အရွယ်အစားရှိသော Disk Blocks များတွင် ဒေတာများကို သိမ်းဆည်းပြီး Block တစ်ခုစီအတွက် Min/Max တန်ဖိုးများပါဝင်သည့် **Zone Maps** များကို Memory တွင် ထိန်းသိမ်းထားသည်-

```mermaid
graph LR
    subgraph DiskBlocks["1 MB Redshift Data Blocks (Sorted on 'order_date')"]
        B1["Block 1: [2026-01-01 to 2026-03-31]<br/>Zone Map: Min=2026-01-01, Max=2026-03-31"]
        B2["Block 2: [2026-04-01 to 2026-06-30]<br/>Zone Map: Min=2026-04-01, Max=2026-06-30"]
        B3["Block 3: [2026-07-01 to 2026-09-30]<br/>Zone Map: Min=2026-07-01, Max=2026-09-30"]
    end

    Query["SELECT * FROM orders WHERE order_date = '2026-08-15'"]

    Query -.->|"Zone Map Check: Skip Block 1"| B1
    Query -.->|"Zone Map Check: Skip Block 2"| B2
    Query -->|"Zone Map Match: Read ONLY Block 3"| B3

    classDef b fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef q fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef match fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class B1,B2 b;
    class B3 match;
    class Query q;
```

1. **Compound Sort Keys (Default & Most Common)**: Prefix Order ဖြင့် Sort လုပ်ထားသည်။ `WHERE col1 = '...' AND col2 = '...'` စသည့် အစီအစဉ်လိုက် Filter ပြုလုပ်သည့်အခါ အလွန်မြန်ဆန်သည်။
2. **Interleaved Sort Keys**: Column အသီးသီးကို အလေးချိန်တူညီစွာ Sort လုပ်ပေးသည်။ မတူညီသော Column များဖြင့် မကြာခဏ အမျိုးမျိုး Filter လုပ်ရသည့် Query များအတွက် သင့်လျော်သည်။

---

## ၄။ Redshift Bulk Ingestion: The `COPY` Command (Exam Critical)

Redshift ထဲသို့ ဒေတာသွင်းရာတွင် `INSERT` command များကို လုံးဝ (လုံးဝ) မသုံးရပါ။ **`COPY` command** တစ်ခုတည်းကိုသာ သုံးရမည်-

```sql
COPY sales_fact
FROM 's3://my-data-lake-bucket/curated/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftS3ReadRole'
FORMAT AS PARQUET;
```

```mermaid
graph TD
    S3Folder["S3 Prefix: s3://my-data-lake-bucket/curated/sales/<br/>(Divided into N files = Multiples of Cluster Slices)"]
    
    subgraph RedshiftSlices["Redshift MPP Slices (Parallel Load)"]
        S1["Slice 1: Reads file_part01.parquet"]
        S2["Slice 2: Reads file_part02.parquet"]
        S3["Slice 3: Reads file_part03.parquet"]
        S4["Slice 4: Reads file_part04.parquet"]
    end

    S3Folder --> S1
    S3Folder --> S2
    S3Folder --> S3
    S3Folder --> S4

    classDef s3 fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef slice fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class S3Folder s3;
    class S1,S2,S3,S4 slice;
```

### Ingestion Best Practices:
- **File Splitting**: S3 ဖိုင်အရေအတွက်သည် Cluster တစ်ခုလုံးရှိ **Slice အရေအတွက်၏ အဆ (Multiples of Slices)** ဖြစ်စေရမည်။
- **Manifest Files**: တိကျသော ဖိုင်များကိုသာ ရွေးချယ်သွင်းရန်နှင့် မလိုလားအပ်သော ဖိုင်များ မပါဝင်စေရန် `manifest` file ကို အသုံးပြုပါ။
- **Compression Encodings**: `AZ64` (ဂဏန်းများနှင့် ရက်စွဲများအတွက် အကောင်းဆုံး) သို့မဟုတ် `ZSTD` ကို အသုံးပြုပါ။

---

## ၅။ Redshift Spectrum vs. Serverless vs. Zero-ETL

| Feature | Redshift Spectrum | Redshift Serverless | Aurora Zero-ETL Ingestion |
| :--- | :--- | :--- | :--- |
| **Architectural Model** | Exabyte S3 Data Lake ကို Redshift မှ External Tables အဖြစ် တိုက်ရိုက် Query လုပ်ခြင်း | Serverless Data Warehouse (RPUs - Redshift Processing Units ဖြင့် Auto-scale လုပ်သည်) | Amazon Aurora မှ Transactional Data များကို Redshift သို့ စက္ကန့်ပိုင်းအတွင်း အလိုအလျောက် Replicate လုပ်ပေးခြင်း |
| **ETL Requirements** | **Zero ETL** (S3 Parquet/ORC ကို In-place ဖတ်သည်) | ပုံမှန် SQL/ETL Pipelines | **Zero ETL / Zero Pipeline Maintenance** |
| **Cost Model** | Scan လုပ်သည့် Data ပမာဏအလိုက် ($5 per TB scanned) | Run သည့် RPU-hours အလိုက် ပေးချေရသည် | Aurora I/O + Redshift Serverless RPUs |

---

## ၆။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"High-performance petabyte-scale columnar OLAP data warehousing"** $\rightarrow$ **Amazon Redshift**.
> - **"Fastest parallel bulk load into Redshift"** $\rightarrow$ **`COPY` command from Amazon S3 with files split into multiples of node slices + Parquet / AZ64 encoding**.
> - **"Query S3 data lake files directly without loading them into Redshift"** $\rightarrow$ **Redshift Spectrum** (External schema & external tables via Glue Data Catalog).
> - **"Near-real-time analytics on transactional data without building custom ETL"** $\rightarrow$ **Amazon Aurora Zero-ETL integration with Amazon Redshift**.
> - **"Eliminate join overhead for small dimension tables"** $\rightarrow$ **`DISTSTYLE ALL`**.
> - **"Eliminate join overhead for massive fact table joining on customer_id"** $\rightarrow$ **`DISTSTYLE KEY(customer_id)` on both tables (Colocated join)**.

> [!WARNING]
> **Exam Traps (သတိထားရမည့် အချက်များ)**:
> 1. **Single-row INSERT Trap**: Redshift သို့ Data ထည့်သွင်းရာတွင် `INSERT` command များကို Loop ပတ်သုံးခြင်းသည် Cluster တစ်ခုလုံးကို အလွန်နှေးကွေးစေသည်။ အမြဲတမ်း S3 ပေါ်သို့ File အဖြစ် ချပြီး `COPY` command ကို သုံးပါ။
> 2. **Interleaved Sort Key Vacuuming Trap**: Interleaved Sort Keys များကို Data အများအပြား အသစ်ထည့်ပြီးပါက `VACUUM REINDEX` မဖြစ်မနေ run ပေးရမည်။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[athena]]` — Amazon Athena Serverless S3 Querying
- `[[glue]]` — AWS Glue ETL & Data Catalog
- `[[s3]]` — Amazon S3 Data Lake
- `[[rds-and-aurora]]` — Amazon Aurora Zero-ETL & RDS
- `[[service-comparisons]]` — Redshift vs Athena vs EMR
