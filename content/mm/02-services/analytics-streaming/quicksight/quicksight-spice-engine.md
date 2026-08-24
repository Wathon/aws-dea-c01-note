---
title: Amazon QuickSight SPICE In-Memory Engine, Refresh Strategies & Cost Optimization (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/quicksight
  - spice-engine
  - incremental-refresh
  - in-memory-analytics
  - cost-optimization
  - burmese
date: 2026-08-19
---

# ⚡ Amazon QuickSight SPICE In-Memory Engine, Refresh Strategies & Cost Optimization

- **Category**: Analytics / High-Performance In-Memory Analytics & Query Caching
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/analytics-streaming/quicksight/quicksight-spice-engine) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Dashboard queries များကို sub-second speed အထိ မြန်ဆန်စေခြင်း၊ Full နှင့် Incremental SPICE refresh များကို configure ပြုလုပ်ခြင်း၊ နှင့် Amazon Athena နှင့် database scan costs များကို သိသိသာသာ လျှော့ချခြင်း။
- **Slide Reference**: Pages 479–498 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[mm/index|index]]` | `[[mm/02-services/analytics-streaming/quicksight/quicksight|quicksight]]` | `[[mm/02-services/analytics-streaming/athena/athena|athena]]` | `[[mm/02-services/database/redshift|redshift]]` | `[[mm/02-services/database/rds-and-aurora|rds-and-aurora]]`

---

## 1. High-Level Summary

**SPICE (Superfast, Parallel, In-memory Calculation Engine)** သည် records သန်းရာနှင့်ချီရှိသော ဒေတာများပေါ်တွင် ရှုပ်ထွေးသည့် aggregations၊ filters များနှင့် pivot tables များကို sub-second response time ဖြင့် ဖြေကြားပေးနိုင်ရန် တည်ဆောက်ထားသည့် Amazon QuickSight ၏ columnar, in-memory data store ဖြစ်သည်။

**DEA-C01** စာမေးပွဲအတွက် **SPICE vs. Direct Query** ကို မည်သည့်အချိန်တွင် အသုံးပြုရမည်၊ **Lookback Window ဖြင့် Incremental Refresh** ကို မည်သို့ configure လုပ်ရမည်၊ နှင့် SPICE သည် **Athena data scanning costs** များကို မည်သို့ သိသိသာသာ လျှော့ချပေးနိုင်သည်ကို နားလည်ထားခြင်းသည် အရေးကြီးသော architectural skill တစ်ခုဖြစ်သည်။

```mermaid
graph TD
    subgraph StorageSources["Underlying Data Stores (အောက်ခြေ Data Store များ)"]
        S3Lake[("Amazon S3 Parquet Files")]
        AthenaQuery["Amazon Athena Engine"]
        AuroraDB[("Amazon Aurora MySQL (OLTP)")]
        RedshiftDW[("Amazon Redshift Warehouse")]
        S3Lake --> AthenaQuery
    end

    subgraph AccessModes["Amazon QuickSight Data Access Modes"]
        subgraph ModeSPICE["(1) SPICE In-Memory Engine (Recommended)"]
            SPICE_Cache[("SPICE In-Memory Cache<br/>• Up to 1 Billion Rows / 1 TB<br/>• Sub-Second Dashboard Latency<br/>• Downstream Query ဝန်ထုပ်ဝန်ပိုး သုညဖြစ်စေခြင်း")]
            RefreshEngine["Automated Refresh Scheduler<br/>• Incremental Refresh (ဥပမာ - ၁၅ မိနစ်တစ်ကြိမ်)<br/>• Full Refresh (ဥပမာ - နေ့စဉ်)"]
            RefreshEngine --> SPICE_Cache
        end

        subgraph ModeDirect["(2) Direct Query Mode"]
            LiveQuery["Direct Query Pushdown<br/>• Real-Time Live Data<br/>• Visual click တိုင်းအတွက် Athena $5/TB scan ကုန်ကျစရိတ်ဖြစ်ပေါ်စေခြင်း<br/>• Production DB များပေါ်သို့ query load သက်ရောက်စေခြင်း"]
        end
    end

    subgraph Users["End-User Consumption (သုံးစွဲသူများ)"]
        Analysts["Business User & Dashboard Reader ၁,၀၀၀ ကျော်"]
    end

    AthenaQuery -.->|Scheduled Extraction| RefreshEngine
    AuroraDB -.->|Scheduled Extraction| RefreshEngine
    RedshiftDW -.->|Scheduled Extraction| RefreshEngine

    AthenaQuery --- LiveQuery
    AuroraDB --- LiveQuery
    RedshiftDW --- LiveQuery

    SPICE_Cache --> Analysts
    LiveQuery --> Analysts

    classDef src fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;
    classDef spice fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#0f172a;
    classDef direct fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef user fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;

    class S3Lake,AthenaQuery,AuroraDB,RedshiftDW src;
    class SPICE_Cache,RefreshEngine spice;
    class LiveQuery direct;
    class Analysts user;
```

---

## 2. SPICE vs. Direct Query Mode Comparison Matrix

| အကဲဖြတ်မှု အတိုင်းအတာ (Evaluation Dimension) | SPICE (In-Memory Mode) | Direct Query Mode |
| :--- | :--- | :--- |
| **Query Latency** | တစ်သမတ်တည်း **Sub-second** ($< 500\text{ ms}$) ရရှိသည်။ | စက္ကန့်ပိုင်းမှ မိနစ်ပိုင်းအထိ (အောက်ခြေ database/Athena engine ၏ စွမ်းဆောင်ရည်အပေါ် မူတည်သည်)။ |
| **Data Freshness (ဒေတာ လတ်ဆတ်မှု)** | နောက်ဆုံး scheduled သို့မဟုတ် API refresh ပြုလုပ်ထားသည့် အချိန်အတိုင်း လတ်ဆတ်သည် (ဥပမာ - ၁၅ မိနစ် / ၁ နာရီတစ်ကြိမ်)။ | Source database မှ **၁၀၀% real-time live** ဒေတာ ဖြစ်သည်။ |
| **Downstream Impact (မူရင်းစနစ်အပေါ် သက်ရောက်မှု)** | အသုံးပြုသူများ ဝင်ရောက်ကြည့်ရှုနေစဉ် source database ပေါ်တွင် **လုံးဝ သက်ရောက်မှုမရှိပါ (Zero impact)**။ | Visual click သို့မဟုတ် filter တစ်ခုစီတိုင်းသည် source database ပေါ်တွင် live query တစ်ခုစီ run စေသည်။ |
| **Athena Cost Impact (Athena ကုန်ကျစရိတ် သက်ရောက်မှု)** | **ပုံသေ၊ သက်သာသော ကုန်ကျစရိတ် (Fixed, low cost)** ဖြစ်သည်။ သတ်မှတ်ထားသော scheduled ingestion အချိန်များတွင်သာ ဒေတာ scan ဖတ်သည်။ | **ကုန်ကျစရိတ် အလွန်များပြားသည် (Extremely expensive)**။ Dashboard reload သို့မဟုတ် filter ပြောင်းလဲမှုတိုင်းသည် **၁ TB လျှင် \$5 နှုန်း** ဖြင့် ဒေတာ scan ဖတ်သည်။ |
| **Maximum Dataset Size (အများဆုံး Dataset အရွယ်အစား)** | Dataset တစ်ခုလျှင် **Rows ၁ ဘီလီယံ (သို့မဟုတ် 1 TB)** အထိ (Enterprise Edition)။ | အကန့်အသတ်မရှိ (Source database ၏ capacity အပေါ်တွင်သာ မူတည်သည်)။ |
| **Best Used For (အသုံးပြုရန် အသင့်တော်ဆုံး အခြေအနေများ)** | လျင်မြန်သော interactive dashboards များ၊ executive KPI reports များ၊ OLTP databases များကို ဝန်မပိစေရန် ကာကွယ်ခြင်းနှင့် S3 data lakes များအတွက်။ | တိကျသော real-time operational monitoring၊ 1 TB ထက် ကျော်လွန်သော datasets များ၊ သို့မဟုတ် pre-optimized Redshift clusters များအတွက်။ |

---

## 3. SPICE Refresh Strategies (SPICE Refresh ပြုလုပ်နည်း ဗျူဟာများ)

```mermaid
graph TD
    subgraph IngestionStrategies["SPICE Ingestion & Refresh Models"]
        subgraph FullRef["(1) Full Refresh"]
            F1["Dataset တစ်ခုလုံးကို ဖျက်ထုတ်ပြီး အစအဆုံး ပြန်လည် load လုပ်ခြင်း"] --> F2["နေ့စဉ်/အပတ်စဉ် schedule သတ်မှတ်ခြင်း သို့မဟုတ် API မှတစ်ဆင့် trigger လုပ်ခြင်း"]
            F2 --> F3["သေးငယ်သော datasets များ သို့မဟုတ် မကြာခဏ update ဖြစ်တတ်သော historical ဒေတာများအတွက် အကောင်းဆုံးဖြစ်သည်"]
        end

        subgraph IncRef["(2) Incremental Refresh"]
            I1["အသစ်ဝင်လာသော သို့မဟုတ် ပြင်ဆင်ထားသော records များကိုသာ ထုတ်ယူခြင်း"] --> I2["Date/Timestamp column လိုအပ်သည် (ဥပမာ - 'updated_at')"]
            I2 --> I3["Lookback Window ဖြင့် configure ပြုလုပ်ထားသည် (ဥပမာ - ၂၄ နာရီ)"]
            I3 --> I4["မကြာခဏ run နိုင်သည် (အမြန်ဆုံး ၁၅ မိနစ်တစ်ကြိမ်အထိ)"]
        end
    end

    classDef full fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef inc fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class F1,F2,F3 full;
    class I1,I2,I3,I4 inc;
```

### 1. Incremental Refresh Mechanics (Incremental Refresh ၏ လုပ်ဆောင်ပုံ ယန္တရား):
- **Timestamp Field Requirement (Timestamp Field လိုအပ်ချက်)**: Source dataset တွင် `date` သို့မဟုတ် `timestamp` column (ဥပမာ `order_timestamp` သို့မဟုတ် `last_modified_date`) ပါဝင်ရမည်။
- **Lookback Window**: QuickSight သည် `current_time - lookback_window` အတိုင်းအတာအတွင်းရှိ records များကို ဆွဲယူသည်။
  - *ဥပမာ*: **၂၄ နာရီ** Lookback window သတ်မှတ်ထားခြင်းဖြင့် လွန်ခဲ့သော ၂၄ နာရီအတွင်း နောက်ကျမှ ဝင်ရောက်လာသော order status updates များ (သို့မဟုတ် late-arriving CDC records များ) ကို multi-gigabyte table scan အပြည့်အစုံ ဖတ်စရာမလိုဘဲ SPICE ထဲတွင် update ဖြစ်စေရန် သေချာစေသည်။

### 2. Event-Driven Programmatic Refresh:
Static clock schedules များကို အသုံးပြုမည့်အစား ခေတ်မီ data engineering pipelines များတွင် AWS SDK / boto3 API ကို အသုံးပြု၍ ETL job ပြီးဆုံးသည်နှင့် တပြိုင်နက် SPICE refresh များကို programmatic နည်းလမ်းဖြင့် trigger လုပ်ကြသည်:
```python
import boto3

quicksight = boto3.client('quicksight')

response = quicksight.create_ingestion(
    DataSetId='orders-dataset-id',
    IngestionId='ingest-job-2026-08-19-01',
    AwsAccountId='123456789012',
    IngestionType='INCREMENTAL_REFRESH'  # or 'FULL_REFRESH'
)
```

---

## 4. Cost Optimization: Slashing Athena & Database Query Bills (Athena နှင့် Database Query ကုန်ကျစရိတ်များကို လျှော့ချခြင်း)

```mermaid
graph LR
    subgraph DirectQueryCost["Scenario A: Athena ပေါ်တွင် Direct Query အသုံးပြုခြင်း"]
        A_User["နေ့စဉ် Dashboards ကြည့်ရှုနေသော အသုံးပြုသူ ၅၀၀"] -->|"တစ်နေ့လျှင် Visual Queries ၅,၀၀၀"| A_Athena["Query တစ်ခုလျှင် Athena မှ 200 GB scan ဖတ်ခြင်း"]
        A_Athena -->|"Total Cost"| A_Bill["Athena Scan Fees တစ်လလျှင် $5,000 ကျော် 💸"]
    end

    subgraph SPICECost["Scenario B: SPICE In-Memory Cache အသုံးပြုခြင်း"]
        B_User["နေ့စဉ် Dashboards ကြည့်ရှုနေသော အသုံးပြုသူ ၅၀၀"] -->|"Sub-Second Visual Interaction"| B_SPICE["SPICE In-Memory Cache"]
        B_Source["နေ့စဉ် Scheduled Extraction (Athena)"] -->|"တစ်နေ့လျှင် ၁ ကြိမ် Scan (200 GB)"| B_SPICE
        B_SPICE -->|"Total Cost"| B_Bill["တစ်လလျှင် $35 အောက် (SPICE Capacity + Scan ၁ ကြိမ်) 💰"]
    end

    classDef bad fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;
    classDef good fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class A_User,A_Athena,A_Bill bad;
    class B_User,B_SPICE,B_Source,B_Bill good;
```

### Cost Optimization Rules (ကုန်ကျစရိတ် သက်သာစေမည့် စည်းမျဉ်းများ):
1. **Athena Scan Reduction (Athena Scan လျှော့ချခြင်း)**: QuickSight မှ S3 data lakes များကို Athena ဖြင့် တိုက်ရိုက် query လုပ်ခြင်းသည် visual filter အပြောင်းအလဲ သို့မဟုတ် page refresh ပြုလုပ်တိုင်း raw files များကို scan ဖတ်သည့် SQL query အသစ်တစ်ခု ဖြစ်ပေါ်စေသောကြောင့် cloud ကုန်ကျစရိတ်များ အဆမတန် မြင့်တက်လာနိုင်သည်။ Athena table ကို **SPICE** ထဲသို့ import လုပ်ခြင်းဖြင့် Athena scanning ကို သတ်မှတ်ထားသော scheduled ingestion intervals များတွင်သာ အလုပ်လုပ်စေရန် သီးသန့် ကန့်သတ်ပေးသည်။
2. **Protecting Production Databases (Production Database များကို ကာကွယ်ခြင်း)**: Direct Query သည် လုပ်ငန်းသုံး operational databases (Aurora/RDS) များဆီသို့ ကြိုတင်ခန့်မှန်းမရနိုင်သော ပြိုင်တူ (concurrent) SQL queries များကို ပေးပို့စေသည်။ SPICE သည် OLTP application workloads များပေါ်တွင် analytical queries များကြောင့် ဖြစ်ပေါ်လာမည့် ဝန်ပိမှု (query contention) ကို ကာကွယ်ပေးသည်။

---

## 5. DEA-C01 Exam Essentials (စာမေးပွဲအတွက် မဖြစ်မနေ သိထားရမည့်အချက်များ)

> [!IMPORTANT]
> **SPICE အတွက် အဓိက စာမေးပွဲ Decision Triggers များ**:
>
> - **"Business analysts များက Athena မှတစ်ဆင့် S3 data lake ကို query လုပ်ထားသော dashboards များသည် နှေးကွေးပြီး scanning cost များစွာ ကုန်ကျနေသည်ဟု တိုင်ကြားလာခြင်း"** $\rightarrow$ Dataset access mode ကို **Direct Query** မှ **SPICE** သို့ ပြောင်းလဲပါ။
> - **"နှေးကွေးသော full reload ကို run စရာမလိုဘဲ rows သန်းပေါင်းများစွာရှိသော SPICE dataset ကို အသစ်ရောက်ရှိလာသော records များဖြင့် မကြာခဏ update ပြုလုပ်လိုခြင်း"** $\rightarrow$ Timestamp column ပေါ်တွင် **Lookback Window** ဖြင့် **Incremental Refresh** ကို configure ပြုလုပ်ပါ။
> - **"AWS Glue ETL job က S3 သို့ ဒေတာရေးသားပြီးစီးသည်နှင့် တပြိုင်နက် SPICE ကို refresh လုပ်လိုခြင်း"** $\rightarrow$ AWS Step Functions state machine သို့မဟုတ် Lambda function အတွင်းမှ **QuickSight `CreateIngestion` API** ကို ခေါ်ယူပါ။
> - **"Enterprise Capacity Limit"** $\rightarrow$ SPICE သည် Enterprise Edition တွင် dataset တစ်ခုလျှင် **Rows ၁ ဘီလီယံ (သို့မဟုတ် 1 TB)** အထိ ထောက်ပံ့ပေးသည်။

---

## 📌 Related Notes
- `[[mm/02-services/analytics-streaming/quicksight/quicksight|quicksight]]` — QuickSight Master Hub
- `[[mm/02-services/analytics-streaming/quicksight/quicksight-data-preparation-and-modeling|quicksight-data-preparation-and-modeling]]` — Dataset Joins & Calculated Fields
- `[[mm/02-services/analytics-streaming/athena/athena|athena]]` — Amazon Athena Query Engine
- `[[mm/02-services/database/redshift|redshift]]` — Amazon Redshift Data Warehousing
- `[[mm/02-services/analytics-streaming/glue/glue-etl-jobs|glue-etl-jobs]]` — Orchestrating ETL Pipelines before SPICE Ingestion
