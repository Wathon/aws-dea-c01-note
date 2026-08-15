---
title: AWS Glue Flex Execution Class (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - cost-optimization
  - burmese
date: 2026-08-15
---

# 💰 AWS Glue Flex Execution Class (ကုန်ကျစရိတ် သက်သာသော Glue အသုံးပြုမှု)

- **Category**: Analytics / Cost Optimization
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-flex.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: အချိန်အတိအကျ မလိုအပ်သော (Non-urgent) Data Integration လုပ်ငန်းစဉ်များအတွက် ကုန်ကျစရိတ် ချွေတာရန်။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[glue-etl-jobs]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Flex** သည် AWS ၏ အသုံးမပြုဘဲ ကျန်ရှိနေသော Compute Capacity များကို အသုံးချခြင်းဖြင့် Glue Jobs များ၏ ကုန်ကျစရိတ်ကို ၃၅% အထိ လျှော့ချပေးနိုင်သော Job Execution Class တစ်ခုဖြစ်သည်။ (Amazon EC2 Spot Instances များနှင့် သဘောတရား တူညီပါသည်)။ 

Spare Capacity ကို အသုံးပြုသည့်အတွက် Job စတင်မည့်အချိန်နှင့် ပြီးစီးမည့် အချိန်များမှာ အပြောင်းအလဲ ရှိနိုင်ပြီး AWS မှ Compute Resources များကို အခြားနေရာအတွက် ပြန်လည်ရယူပါက Job အလုပ်လုပ်နေစဉ် ရပ်တန့်သွားနိုင်သည်။ ထို့ကြောင့် **အချိန်အတိအကျ အာမခံရန် မလိုအပ်သော (Non-time-sensitive)** Workloads များအတွက်သာ သီးသန့် ရည်ရွယ်သည်။

---

## ၂။ Standard vs. Flex Execution Class နှိုင်းယှဉ်ချက်

| Feature | Standard Execution Class | Flex Execution Class |
| :--- | :--- | :--- |
| **Cost (ကုန်ကျစရိတ်)** | Baseline cost ပုံမှန်အတိုင်း | **၃၅% အထိ ပိုမို သက်သာသည်** |
| **Start Time (စတင်ချိန်)** | မြန်ဆန်ပြီး ခန့်မှန်းရ လွယ်ကူသည် | AWS Capacity ပေါ်မူတည်၍ နှောင့်နှေးနိုင်သည် |
| **Job Interruption (ရပ်တန့်နိုင်မှု)** | အလွန်နည်းပါးသည် | **ရှိနိုင်ပါသည်** (Resources များကို AWS မှ ပြန်လည်ရယူနိုင်သည်) |
| **အကောင်းဆုံး အသုံးချမှု** | အချိန်အတိအကျ ပြီးရန်လိုသော ပုံမှန် Reports များ၊ Streaming များ | ညဘက်အေးဆေးမှ Run သော Batch Jobs များ၊ Development/Testing များ၊ ဒေတာဟောင်းများ Backfill ပြုလုပ်ခြင်း |
| **Supported Worker Types** | `G.1X`, `G.2X`, `G.4X`, `G.8X`, `G.025X` | `G.1X`, `G.2X` |

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Cost-optimize non-urgent, nightly batch ETL jobs where predictable start times are not required"** $\rightarrow$ **AWS Glue Flex execution class ကို ရွေးချယ်ပါ**။
> - **"Save up to 35% on Glue PySpark jobs running historical backfills"** $\rightarrow$ **AWS Glue Flex**။
> - **"A job is mission-critical and must finish exactly at 8:00 AM every day"** $\rightarrow$ **Glue Flex ကို လုံးဝ မသုံးရပါ၊ Standard execution class ကိုသာ သုံးပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue-etl-jobs]]` — AWS Glue ETL Jobs & Worker Types
- `[[cost-management]]` — General AWS Cost Optimization
