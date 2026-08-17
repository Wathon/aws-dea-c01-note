---
title: Athena CTAS (Create Table As Select) (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - etl
  - burmese
date: 2026-08-17
---

# 🔄 Athena CTAS (Create Table As Select)

- **Category**: Analytics / Lightweight ETL
- **Language / ဘာသာစကား**: [English (Original)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/athena/athena-ctas.md) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: S3 တွင်ရှိသော data များကို convert, partition နှင့် compress လုပ်ရန် SQL ကို အသုံးပြု၍ lightweight data transformations (ETL) ကို ဆောင်ရွက်ခြင်း။
- **Hub Links**: `[[mm/index]]` | `[[mm/athena]]` | `[[mm/glue-etl-jobs]]`

---

## 1. High-Level Summary

**CTAS (Create Table As Select)** သည် Amazon Athena မှ ထောက်ပံ့ပေးထားသော standard SQL statement တစ်ခုဖြစ်ပါသည်။ ၎င်းသည် လက်ရှိရှိနေသော table တစ်ခုပေါ်တွင် query တစ်ခု run ပြီး ထို query ၏ output ကို **လုံးဝအသစ်ဖြစ်သော table တစ်ခု** အနေဖြင့် Amazon S3 တွင် သိမ်းဆည်းနိုင်စေကာ AWS Glue Data Catalog သို့ အဆိုပါ table အသစ်ကို အလိုအလျောက် ထည့်သွင်းပေးပါသည်။

ဤအချက်က Athena ကို Spark clusters များ provision လုပ်စရာမလိုဘဲ သို့မဟုတ် ရှုပ်ထွေးသော Python/Scala code များ ရေးစရာမလိုဘဲ **Lightweight ETL** (Extract, Transform, Load) operations များအတွက် စွမ်းအားကြီးမားသော tool တစ်ခု ဖြစ်စေပါသည်။

---

## 2. Core Capabilities & Use Cases

### 1. Data Format Conversion (CSV $\rightarrow$ Parquet)
အကယ်၍ သင်သည် raw CSV data ကို ရရှိထားပါက၊ ၎င်းကို ထပ်ခါတလဲလဲ query လုပ်ခြင်းသည် နှေးကွေးပြီး စရိတ်ကြီးမားပါသည်။ သင်သည် CTAS query ကို အသုံးပြု၍ CSV data ကို select လုပ်ကာ compressed ဖြစ်သော Parquet အနေဖြင့် write လုပ်နိုင်ပါသည်။

```sql
CREATE TABLE new_parquet_table
WITH (
  format = 'PARQUET',
  parquet_compression = 'SNAPPY',
  external_location = 's3://my-bucket/optimized-data/'
) AS
SELECT * FROM raw_csv_table;
```

### 2. Partitioning Data
သင်သည် unpartitioned data များကို နောက်ပိုင်း query များ ပိုမိုကောင်းမွန်စေရန် S3 တွင် partitioned directory structure တစ်ခုသို့ ပြောင်းလဲဖွဲ့စည်းနိုင်ပါသည်။

```sql
CREATE TABLE partitioned_sales
WITH (
  format = 'PARQUET',
  partitioned_by = ARRAY['year', 'month']
) AS
SELECT order_id, total, year, month FROM raw_sales;
```

### 3. Data Cleansing & Aggregation
null records များကို filter ထုတ်ခြင်း၊ table များကို join ခြင်း သို့မဟုတ် နေ့စဉ် aggregations များကို ကြိုတင်တွက်ချက်ထားခြင်း စသည်တို့ကို ပြုလုပ်နိုင်ပြီး သန့်စင်ထားသော/ပေါင်းစပ်ထားသော dataset ကို table အသစ်တစ်ခုအနေဖြင့် သိမ်းဆည်းကာ business analysts များမှ လျင်မြန်စွာ query လုပ်နိုင်ရန် အသုံးပြုနိုင်ပါသည်။

---

## 3. CTAS vs. AWS Glue ETL

Athena CTAS နှင့် AWS Glue ကို မည်သည့်အချိန်တွင် သုံးသင့်သနည်း။

| Feature | Athena CTAS | AWS Glue ETL (Spark) |
| :--- | :--- | :--- |
| **Skill Required** | Standard SQL | Python (PySpark) / Scala |
| **Complexity Limit** | Simple joins, filters, format conversion | Complex, multi-step transformations, ML transforms |
| **Execution Limit** | Fails if query takes > 30 minutes | Can run for hours (supports massive datasets) |
| **Cost** | Charged per TB scanned | Charged per DPU-hour (Compute time) |

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Convert CSV data to Parquet using only SQL without managing servers"** $\rightarrow$ **Use Athena CTAS**.
> - **"Create a subset of a massive table for analysts to query faster and cheaper"** $\rightarrow$ **Use an Athena CTAS query with aggregation**.
> - **"Transform data in S3 but the team only knows SQL"** $\rightarrow$ **Use Athena CTAS**.

> [!WARNING]
> **Exam Trap**:
> - ထောင်ပေါင်းများစွာသော transformations များ လိုအပ်သည့် သို့မဟုတ် process လုပ်ရန် နာရီပေါင်းများစွာ ကြာမြင့်သည့် ရှုပ်ထွေးသော ETL logic အတွက် Athena CTAS ကို အသုံးမပြုပါနှင့်။ Heavy ETL အတွက်ဆိုလျှင် စာမေးပွဲ၏ အဖြေမှာ **AWS Glue ETL** သို့မဟုတ် **Amazon EMR** ဖြစ်ပါလိမ့်မည်။

---

## 📌 Related Notes
- `[[mm/athena]]` — Athena Overview
- `[[mm/glue-etl-jobs]]` — Heavyweight Spark ETL
- `[[mm/athena-performance]]` — Why Parquet and partitioning matter
