---
title: Data Validation and Profiling (မြန်မာဘာသာ)
type: concept-note
category: Data Quality & Governance
tags:
  - concept/data-engineering
  - dea-c01
  - data-quality
  - glue-dqdl
  - databrew
  - burmese
date: 2026-08-15
---

# 🔍 Data Validation and Profiling (ဒေတာအရည်အသွေး စစ်ဆေးခြင်းနှင့် ပုံစံလေ့လာဆန်းစစ်ခြင်း)

- **Category**: Data Quality & Governance (ဒေတာ အရည်အသွေး စီမံခန့်ခွဲမှု)
- **ဘာသာစကား လမ်းညွှန်**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/03-concepts/data-validation-and-profiling.md) | **မြန်မာဘာသာ (Burmese)**
- **Slide Reference**: Data Quality & Governance in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[service-catalog]]` | `[[glue]]` | `[[sagemaker-and-ai]]` | `[[lambda]]` | `[[s3]]`

---

## ၁။ အကျဉ်းချုပ် နှိုင်းယှဉ်ချက် (High-Level Summary)

ခေတ်မီ Data Pipeline များတွင် မသန့်ရှင်းသော ဒေတာများ (Garbage Data) Downstream Analytics သို့ မရောက်ရှိစေရန် **Data Profiling** နှင့် **Data Validation** ကို အဆင့်လိုက် အသုံးပြုပါသည်-

| သဘောတရား (Concept) | အဓိက ရည်ရွယ်ချက် (Primary Purpose) | မည်သည့်အဆင့်တွင် ပြုလုပ်သနည်း | အဓိက အသုံးပြုသော AWS Services |
| :--- | :--- | :--- | :--- |
| **Data Profiling** | ဒေတာ၏ ဖွဲ့စည်းပုံ၊ ကိန်းဂဏန်းပျံ့နှံ့မှု (Distributions)၊ Data Types၊ Null/Missing Values နှင့် ပုံမမှန်မှုများကို **လေ့လာဆန်းစစ်ခြင်း**။ | **Data Discovery & Ingestion အဆင့်** | **AWS Glue DataBrew**, SageMaker Data Wrangler, Glue Crawlers |
| **Data Validation** | စီးပွားရေးဆိုင်ရာ စည်းမျဉ်းများ (Business Rules)၊ ကန့်သတ်ချက်များ (Uniqueness, Range, Completeness, Regex) နှင့် ကိုက်ညီမှုရှိမရှိ **စစ်ဆေးအတည်ပြုခြင်း**။ | **ETL / Data Transformation အဆင့်** | **AWS Glue Data Quality (DQDL)**, PyDeequ (EMR/Spark), AWS Lambda |

---

## ၂။ Core Frameworks & စစ်ဆေးမှု စည်းမျဉ်းများ

```mermaid
flowchart LR
    Source["(1) Raw Ingestion (S3 Bronze)"] --> Validate{"(2) Data Validation Engine<br/>(Glue DQDL / Lambda)"}
    Validate -->|"Passed Quality Rules"| Lake[("(3) Processed Data Lake<br/>(S3 Silver / Redshift)")]
    Validate -->|"Failed / Corrupted Records"| DeadLetter[("(4) Quarantine S3 Bucket<br/>(Dead-Letter Store)")]
    Validate -->|"Threshold Breached Alert"| SNS["(5) Amazon SNS Alert<br/>(Notify Data Engineers)"]

    classDef src fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef val fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef pass fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef fail fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;

    class Source src;
    class Validate val;
    class Lake pass;
    class DeadLetter,SNS fail;
```

### ၁. Data Profiling တွင် ပါဝင်သော အချက်များ
- **Statistical Insights**: အနည်းဆုံး (Min)၊ အများဆုံး (Max)၊ ပျမ်းမျှ (Mean/Median)၊ Standard Deviation နှင့် စုစုပေါင်း Row အရေအတွက် တွက်ချက်ခြင်း။
- **Structural Inspection**: Nested JSON များ၊ Data types ပြောင်းလဲမှု (Schema Drift) ကို စောင့်ကြည့်ခြင်း။
- **Missingness & Cardinality**: Null တန်ဖိုး ရာခိုင်နှုန်း၊ တန်ဖိုးထပ်နေမှု (Duplicates) များကို ဖော်ထုတ်ခြင်း။

### ၂. Data Validation Rules (DQDL ဥပမာများ)
- **Completeness (ပြည့်စုံမှု)**: `Completeness "customer_id" >= 0.98` (Null value ၂% ထက် မကျော်ရ)။
- **Uniqueness (သီးသန့်ဖြစ်မှု)**: `IsUnique "transaction_id"` (Primary key ထပ်မနေရ)။
- **Range & Correlation (ကိန်းဂဏန်း အပိုင်းအခြား)**: `ColumnValues "age" between 18 and 120`။
- **Format Assertions**: အီးမေးလ်ပုံစံ Regex စစ်ဆေးခြင်း၊ ISO Timestamps ကိုက်ညီမှု ရှိမရှိ စစ်ဆေးခြင်း။

---

## ၃။ AWS Services အလိုက် လုပ်ဆောင်ချက်များ (DEA-C01 Focus)

### ၁. AWS Glue Data Quality (DQDL)
- Serverless Glue ETL Pipeline များအတွင်း **Data Quality Definition Language (DQDL)** ဖြင့် Declarative Rules များ ရေးသားနိုင်ခြင်း။
- Data Quality Score သတ်မှတ်ချက် မပြည့်မီပါက **Glue ETL Job ကို အလိုအလျောက် ရပ်တန့် (Fail) စေနိုင်သည်**။
- **AWS Glue Data Catalog** နှင့် ချိတ်ဆက်၍ Table တစ်ခုချင်းစီ၏ Quality Score ကို မှတ်တမ်းတင်ပေးသည်။

### ၂. AWS Glue DataBrew
- Code ရေးစရာမလိုသော **No-code Visual Data Profiling & Preparation Tool** ဖြစ်သည်။
- စာရင်းဇယား မက်ထရစ် ၈၀ ကျော်ပါဝင်သည့် **Data Quality Reports** များကို Visual Charts များဖြင့် ဖော်ပြပေးသည်။
- Data Analysts များနှင့် Non-programmers များ အသုံးပြုရန် သင့်လျော်သည်။

### ၃. PyDeequ / Deequ (Amazon EMR & Apache Spark)
- AWS မှ Apache Spark ပေါ်တွင် Unit Test ပြုလုပ်ရန် ဖန်တီးထားသော Open-Source Library ဖြစ်သည်။
- Petabyte-scale Big Data PySpark ETL များတွင် Anomaly Detection နှင့် Quality Metrics များကို စစ်ဆေးရန် အသုံးပြုသည်။

---

## ၄။ ပျက်စီးနေသော ဒေတာများကို ကိုင်တွယ်သည့် ပုံစံများ (Quarantine Patterns)

| Architecture Pattern | အလုပ်လုပ်ပုံ (Mechanism) | အသုံးပြုသည့် အခြေအနေ (Use Case) |
| :--- | :--- | :--- |
| **Quarantine Bucket / DLQ** | စည်းမျဉ်းမကိုက်ညီသော Record များကို **S3 Quarantine Bucket** သို့မဟုတ် **SQS DLQ** သို့ ခွဲထုတ်ပို့ပြီး မှန်ကန်သော Record များကိုသာ ဆက်လက် Process လုပ်စေခြင်း။ | High-throughput Streaming (Kinesis) သို့မဟုတ် Batch ETL စနစ်များ။ |
| **Fail-Fast (ချက်ချင်း ရပ်တန့်ခြင်း)** | Data Quality မပြည့်မီပါက Glue Job သို့မဟုတ် Step Function ကို ချက်ချင်း ရပ်တန့်စေခြင်း။ | ဘဏ္ဍာရေးစာရင်းများ (Financial Ledger)၊ တိကျမှု အရေးကြီးသော နေရာများ။ |
| **Remediation & Masking** | Null တန်ဖိုးများကို Default တန်ဖိုးဖြင့် အစားထိုးခြင်း သို့မဟုတ် PII Data များကို Mask ပြုလုပ်ခြင်း။ | စာရင်းအင်း သုတေသန ပြုလုပ်မည့် Data Lake များ။ |

---

## ၅။ DEA-C01 စာမေးပွဲ အဓိက မေးခွန်းပုံစံများ (Exam Scenarios)

> [!IMPORTANT]
> **Key Exam Decision Matrix**:
> - **Scenario 1: "Visual, no-code data profiling reports with 80+ statistical metrics"** $\rightarrow$ **AWS Glue DataBrew** ကို ရွေးပါ။
> - **Scenario 2: "Declarative data quality rules inside serverless Glue ETL jobs with auto-fail threshold"** $\rightarrow$ **AWS Glue Data Quality (DQDL)** ကို ရွေးပါ။
> - **Scenario 3: "Unit testing and anomaly detection on distributed Amazon EMR PySpark jobs"** $\rightarrow$ **PyDeequ / Deequ** ကို ရွေးပါ။
> - **Scenario 4: "Alert team when null values exceed threshold in S3 table"** $\rightarrow$ **Glue Data Quality + CloudWatch Alarm + Amazon SNS**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Data Catalog, Crawlers နှင့် Glue Data Quality
- `[[sagemaker-and-ai]]` — SageMaker Data Wrangler profiling စနစ်များ
- `[[data-formats-and-compression]]` — Parquet နှင့် Schema Validation
- `[[service-comparisons]]` — Glue Data Quality vs. Glue DataBrew နှိုင်းယှဉ်ချက်
