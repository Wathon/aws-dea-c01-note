---
title: AWS Glue Data Catalog (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - metadata
  - burmese
date: 2026-08-15
---

# 📖 AWS Glue Data Catalog (ဗဟို Metadata သိုလှောင်မှု)

- **Category**: Analytics / Metadata Management
- **Language / ဘာသာစကား**: [English Version](/en/02-services/analytics-streaming/glue/glue-data-catalog) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: S3 Data Lakes, Athena, EMR နှင့် Redshift Spectrum တို့အတွက် ဗဟို Apache Hive-compatible Metastore အဖြစ် အသုံးပြုခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[athena]]` | `[[lake-formation]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Data Catalog** သည် AWS ပေါ်ရှိ ဒေတာများ၏ တည်နေရာ၊ Schema နှင့် ဖော်မတ်များကို စုစည်းမှတ်သားပေးသော ဗဟို Metadata Repository (Metastore) ဖြစ်သည်။ စနစ်အသီးသီးတွင် Metadata များကို ခွဲခြားသိမ်းဆည်းမည့်အစား **Amazon Athena**, **Amazon EMR** နှင့် **Amazon Redshift Spectrum** တို့သည် S3 ရှိ ဒေတာများကို Query ပြုလုပ်ရာတွင် ဤ Glue Data Catalog ကို တိုက်ရိုက် ချိတ်ဆက် အသုံးပြုကြသည်။

---

## ၂။ အဓိက အစိတ်အပိုင်းများ (Core Concepts)

### 1. Databases နှင့် Tables
- **Databases**: Catalog အတွင်းရှိ Table များကို စနစ်တကျ စုစည်းထားသော နေရာ။
- **Tables**: ဒေတာအမှန်တကယ် မဟုတ်ဘဲ ဒေတာ၏ ဖွဲ့စည်းပုံ (Metadata) ကိုသာ သိမ်းဆည်းသည်။ Table တွင် S3 တည်နေရာ၊ Columns အမည်များ၊ Data Types များနှင့် Parquet/JSON ကဲ့သို့ Format များကို မှတ်တမ်းတင်ထားသည်။

### 2. Partition Indexes
- Partition အရေအတွက် သန်းနှင့်ချီရှိသော S3 ဒေတာများကို Athena ဖြင့် Query ပြုလုပ်ရာတွင် ပိုမိုမြန်ဆန်စေရန် Glue Data Catalog table တွင် **Partition Indexes** များကို တည်ဆောက်နိုင်သည်။
- ဤသို့ပြုလုပ်ခြင်းဖြင့် Athena သည် Partition အားလုံးကို အချိန်ယူ၍ Scan ဖတ်နေစရာမလိုတော့ဘဲ မိမိအလိုရှိသော သက်ဆိုင်ရာ Partition များကိုသာ အမြန်ဆုံး ဆွဲထုတ်နိုင်သည်။

### 3. Lake Formation နှင့် ချိတ်ဆက်မှု
- Data Catalog သည် `[[lake-formation]]` နှင့် တိုက်ရိုက် ချိတ်ဆက်အလုပ်လုပ်ပြီး Table များ၏ Column-level နှင့် Row-level Access Control (ဝင်ရောက်ကြည့်ရှုခွင့်) များကို တင်းကျပ်စွာ ထိန်းချုပ်နိုင်သည်။

### 4. Cross-Account Access (အကောင့်များအကြား မျှဝေခြင်း)
- **AWS Resource Access Manager (RAM)** သို့မဟုတ် Lake Formation ကို အသုံးပြု၍ Data Catalog ကို အခြား AWS Accounts များနှင့် မျှဝေနိုင်ပြီး Data Mesh Architecture တည်ဆောက်ရာတွင် အဓိက အခန်းကဏ္ဍမှ ပါဝင်သည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Centralized metastore to store schema definitions for Athena, Redshift Spectrum, and EMR"** $\rightarrow$ **AWS Glue Data Catalog**.
> - **"Hive-compatible metastore on AWS"** $\rightarrow$ **AWS Glue Data Catalog**.
> - **"Speed up Athena queries on an S3 table with millions of partitions"** $\rightarrow$ **Glue Data Catalog တွင် Partition Index ဆောက်ပါ**။
> - **"Apply column-level security to a Data Catalog table"** $\rightarrow$ **AWS Lake Formation**.

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Overview
- `[[glue-crawlers]]` — Automating Data Catalog Population
- `[[athena]]` — Querying the Data Catalog
- `[[lake-formation]]` — Securing the Data Catalog
