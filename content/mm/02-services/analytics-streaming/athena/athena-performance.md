---
title: Athena Performance & Optimization (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - performance
  - burmese
date: 2026-08-17
---

# 🚀 Athena Performance & Optimization

- **Category**: Analytics / Optimization
- **Language / ဘာသာစကား**: [English (Original)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/athena/athena-performance.md) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: S3 မှ ဖတ်ယူရမည့် ဒေတာပမာဏကို ကန့်သတ်ခြင်းဖြင့် query ကုန်ကျစရိတ်ကို လျှော့ချရန်နှင့် query latency ကို တိုးတက်ကောင်းမွန်စေရန်။
- **Hub Links**: `[[mm/index]]` | `[[mm/athena]]` | `[[mm/s3]]`

---

## 1. High-Level Summary

Amazon Athena သည် **ဖတ်ယူစစ်ဆေးသော (scanned) ဒေတာ တစ် Terabyte (TB) လျှင် $5 ကုန်ကျ** သည်။ ထို့ကြောင့် Athena တွင် performance optimization သည် **cost optimization** နှင့် တိုက်ရိုက်ဆက်စပ်နေသည်။ Data Engineer များသည် Athena အနေဖြင့် query အတွက် *လိုအပ်သော* ဒေတာကိုသာ ဖတ်ယူပြီး၊ မသက်ဆိုင်သော ဒေတာများကို လျစ်လျူရှုနိုင်ရန် (ignore လုပ်နိုင်ရန်) S3 တွင် ဒေတာများကို ဖွဲ့စည်းတည်ဆောက်ထားရမည်။

Athena optimization ၏ အဓိက အချက်သုံးချက်မှာ - **Columnar Formats**၊ **Compression** နှင့် **Partitioning** တို့ဖြစ်သည်။

---

## 2. The Core Optimization Techniques

### 1. Columnar Data Formats (Parquet & ORC)
- CSV နှင့် JSON ကဲ့သို့သော ပုံမှန် format များသည် **row-based** (အတန်းလိုက်) ဖြစ်သည်။ အကယ်၍ query တစ်ခုသည် ကော်လံ (column) ၁၀၀ ရှိသော CSV ဖိုင်တစ်ခုမှ ကော်လံ ၂ ခုကိုသာ လိုအပ်ပါက၊ Athena သည် ထိုအတန်း (row) တစ်ခုလုံးကို (ဒေတာ ၁၀၀% ကို) ဖတ်ယူစစ်ဆေးရဆဲဖြစ်သည်။
- **Apache Parquet** နှင့် **Apache ORC** တို့သည် **columnar** (ကော်လံလိုက်) ဖြစ်သည်။ Athena သည် `SELECT` statement တွင် တောင်းဆိုထားသော သီးခြား ကော်လံများကို*သာ* ဖတ်ယူနိုင်ပြီး ကျန်ရှိသော ကော်လံများကို ကျော်သွားနိုင်သည်။
- **Exam Tip**: Athena scan ကုန်ကျစရိတ်များကို သိသိသာသာ လျှော့ချရန် AWS Glue ကို အသုံးပြု၍ CSV/JSON မှ Parquet သို့မဟုတ် ORC သို့ အမြဲတမ်း ပြောင်းလဲပါ။

### 2. Compression (Snappy / Zstd)
- ဒေတာများကို compress လုပ်ခြင်းသည် S3 ရှိ ဖိုင်အရွယ်အစားကို သေးငယ်စေသည်။ ၎င်းသည် Athena အနေဖြင့် megabytes ပိုမိုနည်းပါးစွာ scan ဖတ်ရစေသောကြောင့် ကုန်ကျစရိတ်ကို တိုက်ရိုက်ကျဆင်းစေပြီး network I/O ကို ပိုမိုမြန်ဆန်စေသည်။
- **Snappy** သည် Parquet အတွက် default အနေဖြင့် အကြံပြုထားသော compression format ဖြစ်သည်။ အဘယ်ကြောင့်ဆိုသော် ၎င်းသည် အလွယ်တကူ ခွဲခြမ်းနိုင်သော (highly splittable) ကြောင့်ဖြစ်သည်။ (Athena သည် ဖိုင်၏ အစိတ်အပိုင်းများကို တစ်ပြိုင်နက် (in parallel) ဖတ်ယူနိုင်သည်။)
- **Gzip** သည် သီးခြား configuration များဖြင့် အသုံးပြုခြင်းမှလွဲ၍ အလွယ်တကူ ခွဲခြမ်းနိုင်ခြင်း (splittable) မရှိသောကြောင့် big data အတွက် အသုံးပြုရန် သိပ်မသင့်တော်ပါ။

### 3. Data Partitioning
- Partitioning သည် ကော်လံတစ်ခု၏ တန်ဖိုး (value) ကို အခြေခံ၍ ဒေတာများကို သီးခြား S3 folder များထဲသို့ အုပ်စုခွဲခြင်းဖြစ်သည်။ (ဥပမာ- `s3://bucket/sales/year=2026/month=08/`)
- Query တစ်ခုတွင် `WHERE year = '2026'` clause ပါဝင်သောအခါ၊ Athena သည် အခြားနှစ်များအတွက် folder များကို scan ဖတ်ခြင်းမှ ကျော်သွားမည်ဖြစ်သည်။
- **Glue Crawler Integration**: S3 သို့ partition အသစ်များ ထည့်သွင်းပါက၊ catalog ကို update လုပ်ရန် Glue Crawler ကို run ရမည်၊ သို့မဟုတ် Athena တွင် `MSCK REPAIR TABLE` ကို manual အနေဖြင့် run ရမည်။

---

## 3. Advanced: Partition Projection

Data lake တစ်ခုသည် ကြီးထွားလာပြီး ရာထောင်ချီသော partition များ (ဥပမာ- နှစ်များစွာအတွက် နာရီအလိုက် partition များ) ပါဝင်လာသောအခါ၊ `MSCK REPAIR TABLE` ကို run ခြင်း သို့မဟုတ် partition metadata အတွက် Glue Data Catalog ကို query လုပ်ခြင်းသည် အလွန်နှေးကွေးပြီး ကုန်ကျစရိတ်များလာသည်။

**Partition Projection** သည် Glue Data Catalog metadata ရှာဖွေခြင်းကို လုံးဝကျော်လွန်ပြီး၊ table properties တွင် သတ်မှတ်ထားသော စည်းမျဉ်းများ (rules) အပေါ် အခြေခံ၍ memory အတွင်းရှိ (in-memory) partition တည်နေရာများကို *တက်ကြွစွာ (dynamically)* တွက်ချက်ပေးသော Athena ၏ လုပ်ဆောင်ချက်တစ်ခုဖြစ်သည်။

### Benefits of Partition Projection:
- Partition အသစ်များ ထည့်သွင်းသည့်အခါ **`MSCK REPAIR TABLE` ကို run ရန် မလိုအပ်ပါ**။
- နေ့စဉ်/နာရီအလိုက် partition အသစ်များကို ရှာဖွေရန် **Glue Crawlers များကို run ရန် မလိုအပ်ပါ**။
- Partition အများအပြားပါဝင်သော table များပေါ်တွင် **query များကို သိသိသာသာ မြန်ဆန်စေသည်**။

```sql
-- Example of configuring Partition Projection in table properties
TBLPROPERTIES (
  'projection.enabled' = 'true',
  'projection.date.type' = 'date',
  'projection.date.range' = '2020-01-01,NOW',
  'projection.date.format' = 'yyyy-MM-dd',
  'storage.location.template' = 's3://my-bucket/data/${date}/'
)
```

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Reduce Athena cost and improve query performance"** $\rightarrow$ **Convert data to Parquet/ORC and compress with Snappy**.
> - **"Queries are failing due to a high number of partitions"** သို့မဟုတ် **"MSCK REPAIR TABLE is taking too long"** $\rightarrow$ **Enable Partition Projection**.
> - **"Highly partitioned table with predictable patterns (like hourly/daily dates)"** $\rightarrow$ **Use Partition Projection**.

---

## 📌 Related Notes
- `[[mm/athena]]` — Athena Overview
- `[[mm/glue-crawlers]]` — Automating partition discovery
- `[[mm/s3-performance]]` — S3 Prefix limits and optimization
