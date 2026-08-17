---
title: Athena ACID Transactions (Apache Iceberg) (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - iceberg
  - burmese
date: 2026-08-17
---

# 🧊 Athena ACID Transactions (Apache Iceberg)

- **Category**: Analytics / Data Lake Formats
- **Language / ဘာသာစကား**: [English (Original)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/athena/athena-iceberg.md) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: S3 data lakes များပေါ်တွင် ACID အာမခံချက်များနှင့်အတူ row-level updates၊ deletes နှင့် time-travel queries များကို လုပ်ဆောင်နိုင်စေရန်။
- **Hub Links**: `[[mm/index]]` | `[[mm/athena]]` | `[[mm/domain-2-data-store-management]]`

---

## 1. High-Level Summary

ပုံမှန်အားဖြင့်၊ Amazon S3 နှင့် standard Athena table များသည် **append-only** သို့မဟုတ် **overwrite** သာ လုပ်ဆောင်နိုင်ပါသည်။ 10 GB ရှိသော Parquet file အတွင်းရှိ row တစ်ခုတည်းကို update သို့မဟုတ် delete လုပ်ရန်အတွက်ဆိုလျှင် ယခင်က file တစ်ခုလုံးကို ပြန်ရေးရန် (rewrite) လိုအပ်ပါသည်။

Amazon Athena သည် ကြီးမားသော analytic dataset များအတွက် ဖွင့်ထားသော (open) table format တစ်ခုဖြစ်သည့် **Apache Iceberg** ကို ပံ့ပိုးပေးပြီး ၎င်းသည် S3 data lakes များကို database ကဲ့သို့သော feature များ ရရှိစေပါသည်။ Iceberg ဖြင့် Athena သည် **ACID (Atomicity, Consistency, Isolation, Durability) transactions** များကို လုပ်ဆောင်နိုင်ပါသည်။

---

## 2. Core Capabilities

### 1. Row-Level Operations (UPDATE, DELETE, MERGE)
မှားယွင်းနေသော record တစ်ခုတည်းကို ပြင်ဆင်ရန် သို့မဟုတ် user ၏ data ကို ဖျက်ရန် (ဥပမာ- GDPR လိုက်နာမှုအတွက်) partition တစ်ခုလုံးကို ပြန်ရေးနေမည့်အစား၊ Iceberg သည် သင့်အား standard SQL `UPDATE`, `DELETE`, နှင့် `MERGE INTO` statement များကို Athena တွင် တိုက်ရိုက် run နိုင်စေပါသည်။

### 2. Time-Travel Queries
Iceberg သည် table တွင် ပြုလုပ်ခဲ့သော အပြောင်းအလဲတိုင်း၏ transaction log ကို သိမ်းဆည်းပေးပါသည်။ ၎င်းက သင့်အား အတိတ်ရှိ *သတ်မှတ်ထားသော အချိန်တစ်ခုတွင် ရှိခဲ့သည့်အတိုင်း* table ကို query လုပ်နိုင်စေပါသည်။
- **Exam Tip**: စစ်ဆေးခြင်း (auditing)၊ မတော်တဆ ဖျက်မိမှုများကို ပြန်လည်ယူဆောင်ခြင်း (rolling back)၊ သို့မဟုတ် သမိုင်းဝင် data များပေါ်တွင် machine learning model များကို ပြန်လည်ဖန်တီးခြင်း (reproducing) တို့အတွက် အသုံးဝင်ပါသည်။

```sql
-- မနေ့က ရှိခဲ့သည့်အတိုင်း data ကို query လုပ်ခြင်း
SELECT * FROM iceberg_table FOR SYSTEM_TIME AS OF (current_timestamp - interval '1' day);
```

### 3. Concurrent Writers (ACID Guarantees)
အကယ်၍ AWS Glue jobs၊ EMR clusters၊ နှင့် Athena user အများအပြားသည် တူညီသော S3 table သို့ တစ်ပြိုင်နက် ရေးရန် ကြိုးစားပါက၊ ဖတ်သူများ (readers) သည် တစ်စိတ်တစ်ပိုင်း သို့မဟုတ် ပျက်စီးနေသော (corrupted) data များကို ဘယ်သောအခါမှ မြင်ရမည်မဟုတ်ကြောင်း (Isolation) နှင့် တစ်ပြိုင်နက်တည်း ရေးသားမှုများသည် table ကို ပျက်စီးစေမည် မဟုတ်ကြောင်း (Consistency) Iceberg က အာမခံပါသည်။

### 4. Schema Evolution
သင်သည် column များကို ထည့်ခြင်း (add)၊ ဖျက်ခြင်း (drop)၊ အမည်ပြောင်းခြင်း (rename)၊ သို့မဟုတ် အစီအစဉ်ပြောင်းခြင်း (reorder) တို့ကို အခြေခံ data file များကို ပြန်လည်ရေးသားစရာမလိုဘဲ သို့မဟုတ် ဆက်စပ်နေသော downstream query များကို မပျက်စီးစေဘဲ လုံခြုံစွာ လုပ်ဆောင်နိုင်ပါသည်။

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Need to perform row-level UPDATEs and DELETEs on S3 data lake for GDPR compliance"** $\rightarrow$ **Athena နှင့်အတူ Apache Iceberg ကို အသုံးပြုပါ**.
> - **"Need to run 'time-travel' queries to see what the data looked like 3 days ago"** $\rightarrow$ **Apache Iceberg table format များကို အသုံးပြုပါ**.
> - **"Concurrent writers causing data corruption in S3"** $\rightarrow$ **ACID transactions များအတွက် table format ကို Apache Iceberg သို့ ပြောင်းပါ**.

---

## 📌 Related Notes
- `[[mm/athena]]` — Athena Overview
- `[[mm/athena-performance]]` — အထွေထွေ performance မြှင့်တင်ခြင်း
- `[[mm/glue-etl-jobs]]` — Iceberg နှင့်အတူ Glue ကိုလည်း အသုံးပြုနိုင်ပါသည်
