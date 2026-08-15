---
title: AWS Glue Crawlers (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - crawler
  - burmese
date: 2026-08-15
---

# 🕷️ AWS Glue Crawlers (အလိုအလျောက် Schema ရှာဖွေသူများ)

- **Category**: Analytics / Automated Schema Discovery
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-crawlers.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: S3 နှင့် Database များရှိ ဒေတာ Format များကို ခွဲခြမ်းစိတ်ဖြာပြီး Schema နှင့် Partition များကို အလိုအလျောက် ရှာဖွေဖော်ထုတ်ခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[glue-data-catalog]]` | `[[athena]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Crawlers** သည် ဒေတာရင်းမြစ်များ (Amazon S3, Amazon RDS, DynamoDB, Redshift) ကို အလိုအလျောက် ဝင်ရောက်ဖတ်ရှုပြီး၊ ဒေတာဖော်မတ်များ (Parquet, JSON, CSV) နှင့် Schema (Column အမည်များ၊ အမျိုးအစားများ) ကို ခွဲခြမ်းစိတ်ဖြာကာ **[[glue-data-catalog]]** တွင် Metadata Table များ အလိုအလျောက် တည်ဆောက်ပေးသည်။ ထို့ကြောင့် Data Engineer များအနေဖြင့် DDL (CREATE TABLE) statements များကို ကိုယ်တိုင်ရေးသားစရာ မလိုတော့ပါ။

---

## ၂။ အဓိက စွမ်းဆောင်ရည်များ (Core Capabilities)

### 1. Built-in နှင့် Custom Classifiers
- Crawler သည် ဒေတာအမျိုးအစားကို ခွဲခြားသိရှိနိုင်ရန် **Classifiers** များကို အသုံးပြုသည်။ AWS Glue တွင် JSON, CSV, Parquet, ORC, Avro များအတွက် Built-in classifier များ အသင့်ပါရှိသည်။
- အကယ်၍ ကုမ္ပဏီသုံး သီးသန့် Log Format များဖြစ်နေပါက Grok patterns များကို အသုံးပြု၍ **Custom Classifier** ကို ကိုယ်တိုင် ဖန်တီးနိုင်သည်။

### 2. Automated Partition Detection
- Crawler သည် S3 တွင် ခွဲခြားသိမ်းဆည်းထားသော Hive-style Directory အမည်များ (ဥပမာ- `s3://bucket/data/year=2026/month=08/`) ကို အလိုအလျောက် ရှာဖွေသိရှိပြီး Data Catalog တွင် Partition အဖြစ် ထည့်သွင်းပေးသည်။
- ထို့ကြောင့် S3 သို့ ဒေတာအသစ် ဝင်လာတိုင်း Athena တွင် `MSCK REPAIR TABLE` command ကို ကိုယ်တိုင် ရိုက်ထည့်စရာ မလိုတော့ပါ။

### 3. Schema Evolution (Schema Drift) ကို ဖြေရှင်းခြင်း
အချိန်ကြာလာသည်နှင့်အမျှ ဒေတာရင်းမြစ်များတွင် Column အသစ်များ တိုးလာတတ်သည်။ Glue Crawler သည် ၎င်းအပြောင်းအလဲများကို အလိုအလျောက် သိရှိပြီး Data Catalog ကို Update လုပ်ပေးနိုင်သည်-
- Crawler ကို Setup လုပ်ရာတွင် `Update the table definition in the data catalog` ဆိုသော အချက်ကို ရွေးချယ်ပေးရမည်။ ထိုသို့လုပ်မှသာ Column အသစ်များကို Athena တွင် ချက်ချင်း Query လုပ်၍ ရမည်ဖြစ်သည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Automate the discovery of new partitions added to S3 daily"** $\rightarrow$ **AWS Glue Crawler ကို အချိန်ဇယားဆွဲ၍ Run ပါ**။
> - **"Source data occasionally adds new columns. How to ensure Athena can query them?"** $\rightarrow$ **Crawler configuration တွင် 'Update the table definition in the data catalog' ကို ဖွင့်ပါ**။
> - **"Data in S3 is in a proprietary log format that standard tools cannot parse"** $\rightarrow$ **Grok patterns ကိုသုံး၍ Custom Classifier ဖန်တီးပြီး Crawler နှင့် တွဲဖက်ပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Overview
- `[[glue-data-catalog]]` — Glue Data Catalog Metastore
- `[[data-modeling-and-partitioning]]` — S3 Partition Structures
- `[[athena]]` — Querying Discovered Data
