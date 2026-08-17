---
title: AWS Glue Schema Registry (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - streaming
  - burmese
date: 2026-08-15
---

# 🧬 AWS Glue Schema Registry (Streaming Data Schema ထိန်းချုပ်မှု)

- **Category**: Analytics / Streaming Data Governance
- **Language / ဘာသာစကား**: [English Version](/en/02-services/analytics-streaming/glue/glue-schema-registry) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Streaming applications များ (Kafka, Kinesis) တွင် ဖြတ်သန်းသွားသော ဒေတာများ၏ Schema ကို ဗဟိုမှ ထိန်းချုပ်ခြင်းနှင့် ပြောင်းလဲမှုများကို စီမံခန့်ခွဲခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[msk-kafka]]` | `[[kinesis]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Schema Registry** သည် Streaming ဒေတာများ၏ ဖွဲ့စည်းပုံ (Schema) ကို ဗဟိုမှ သတ်မှတ်ထိန်းချုပ်ပေးသော နေရာဖြစ်သည်။ Amazon MSK / Apache Kafka, Kinesis Data Streams တို့ကဲ့သို့သော Streaming စနစ်များတွင် ဒေတာပေးပို့သူ (Producers) နှင့် ဒေတာလက်ခံသူ (Consumers) အကြား ဒေတာဖော်မတ် တူညီရန် (Contract) လိုအပ်သည်။ Schema Registry သည် ယင်းလိုအပ်ချက်ကို တင်းကျပ်စွာ ထိန်းချုပ်ပေးပြီး ဒေတာဖွဲ့စည်းပုံ အပြောင်းအလဲများကြောင့် Consumer ဘက်တွင် Error တက်ခြင်းကို တားဆီးပေးသည်။

---

## ၂။ အဓိက စွမ်းဆောင်ရည်များ

### 1. Schema Validation (မှားယွင်းသော ဒေတာများကို တားဆီးခြင်း)
- Producer မှ ပေးပို့လိုက်သော Message တိုင်းကို Registry တွင် မှတ်ပုံတင်ထားသော Schema နှင့် ကိုက်ညီမှု ရှိ/မရှိ အလိုအလျောက် စစ်ဆေးသည်။
- Schema နှင့် မကိုက်ညီသော သို့မဟုတ် မှားယွင်းနေသော Message များကို Stream အတွင်းသို့ မရောက်မီ ကြိုတင် ပိတ်ပင်ပစ်လိုက်သည်။

### 2. Schema Evolution (ပြောင်းလဲမှုများကို လိုက်လျောညီထွေဖြစ်စေခြင်း)
ဒေတာဖွဲ့စည်းပုံများသည် အချိန်နှင့်အမျှ ပြောင်းလဲတတ်သည်။ ယင်းပြောင်းလဲမှုများအတွက် Compatibility modes (လိုက်လျောညီထွေမှု အဆင့်များ) ကို သတ်မှတ်နိုင်သည်။
- **Backward Compatibility**: Consumer က Schema အသစ်ကို သုံးနေသော်လည်း Producer မှ Schema အဟောင်းဖြင့် ပို့လိုက်သော ဒေတာများကို ဖတ်ရှုနားလည်နိုင်ခြင်း။
- **Forward Compatibility**: Consumer က Schema အဟောင်းကို သုံးနေသော်လည်း Producer မှ Schema အသစ်ဖြင့် ပို့လိုက်သော ဒေတာများကို ဖတ်ရှုနားလည်နိုင်ခြင်း။
- **Full Compatibility**: Backward နှင့် Forward နှစ်မျိုးစလုံးကို အထောက်အပံ့ ပေးခြင်း။

### 3. Data Compression နှင့် ကုန်ကျစရိတ် သက်သာစေခြင်း
- Schema များကို Registry တွင် ဗဟိုပြု သိမ်းဆည်းထားသောကြောင့် Producer များသည် Message အားလုံးတွင် Schema အပြည့်အစုံကို ထည့်သွင်းပေးပို့စရာ မလိုတော့ပါ။ (ပုံမှန် JSON များထက် ပိုမိုသက်သာသည်)
- Message Payload ထဲတွင် ဒေတာအစစ်နှင့် သေးငယ်သော Schema ID ကိုသာ ထည့်သွင်းပေးပို့သောကြောင့် Network Bandwidth နှင့် Storage ကုန်ကျစရိတ်ကို အလွန်သက်သာစေသည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Prevent bad records from entering a Kafka/Kinesis stream due to changing data formats"** $\rightarrow$ **AWS Glue Schema Registry ကို ရွေးချယ်ပါ**။
> - **"Ensure backward compatibility for an evolving Avro schema in Amazon MSK"** $\rightarrow$ **AWS Glue Schema Registry**။
> - **"Reduce network bandwidth and payload size for streaming messages"** $\rightarrow$ **Message တိုင်းတွင် Schema အပြည့်အစုံ ထည့်စရာမလိုအောင် AWS Glue Schema Registry ကို အသုံးပြုပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[msk-kafka]]` — Amazon Managed Streaming for Apache Kafka
- `[[kinesis]]` — Amazon Kinesis Data Streams
- `[[glue-data-catalog]]` — Glue Metadata Catalog
