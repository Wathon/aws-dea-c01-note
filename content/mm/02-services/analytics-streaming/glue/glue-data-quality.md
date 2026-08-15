---
title: AWS Glue Data Quality (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - data-quality
  - burmese
date: 2026-08-15
---

# ✅ AWS Glue Data Quality (ဒေတာ အရည်အသွေး စစ်ဆေးခြင်း)

- **Category**: Analytics / Data Governance
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-data-quality.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: ဒေတာမှန်ကန်မှုကို အလိုအလျောက် စစ်ဆေးခြင်း၊ မှားယွင်းသော ဒေတာများပါလာပါက Pipeline ကို ရပ်တန့်ပစ်ခြင်း သို့မဟုတ် သီးခြားဖယ်ထုတ်ခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[data-validation-and-profiling]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Data Quality** သည် Data Engineer များအနေဖြင့် ၎င်းတို့၏ Data Lake နှင့် Pipeline များအတွင်းရှိ ဒေတာများ၏ အရည်အသွေးကို အလွယ်တကူ တိုင်းတာစစ်ဆေးနိုင်ရန် ပြုလုပ်ပေးသော ဝန်ဆောင်မှုဖြစ်သည်။ ဒေတာမှန်ကန်မှု (Data correctness) ကို စစ်ဆေးရန် ရှုပ်ထွေးသော PySpark Code များကို ကိုယ်တိုင်ရေးသားမည့်အစား **DQDL (Data Quality Definition Language)** ဟုခေါ်သော ရိုးရှင်းသည့် စည်းမျဉ်းများကိုသာ အသုံးပြုရသည်။

---

## ၂။ အဓိက စွမ်းဆောင်ရည်များ

### 1. Data Quality Definition Language (DQDL)
DQDL သည် စည်းမျဉ်းများကို ရိုးရှင်းစွာ ရေးသားနိုင်သော ဘာသာစကားဖြစ်သည်။ ဥပမာ-
- `Completeness "email" > 0.98` (Email column တွင် ဒေတာပါဝင်မှု ၉၈% ရှိရမည်)။
- `IsUnique "user_id"` (User ID များ ထပ်နေခြင်း မရှိစေရ)။
- `ColumnValues "status" in ["ACTIVE", "INACTIVE", "PENDING"]` (Status သည် သတ်မှတ်ထားသော တန်ဖိုး ၃ မျိုးသာ ဖြစ်ရမည်)။

### 2. Glue ETL Jobs နှင့် တွဲဖက်အသုံးပြုခြင်း
Glue ETL Pipeline ထဲတွင် Data Quality ကို ထည့်သွင်းထားပါက ၎င်းသည် Gatekeeper အဖြစ် အလုပ်လုပ်ပေးသည်-
- **CloudWatch သို့ Metrics များပို့ပေးခြင်း**။
- အကယ်၍ အရေးကြီးသော စည်းမျဉ်းများ ကျရှုံးပါက **Job ကို ချက်ချင်း ရပ်တန့်ပစ်ခြင်း (Fail the job)** (မှားယွင်းသော ဒေတာများ Data Warehouse သို့ မရောက်စေရန်)။
- အမှားပါသော row များကို လူကိုယ်တိုင် စစ်ဆေးရန် သီးသန့် Quarantine S3 Bucket (Dead-letter) သို့ ပို့ဆောင်ပေးပြီး အမှန်ပါသော row များကို ဆက်လက် အလုပ်လုပ်စေခြင်း။

### 3. Data Catalog တွင် တိုက်ရိုက် စစ်ဆေးခြင်း
Glue ETL တွင်သာမကဘဲ **[[glue-data-catalog]]** ထဲတွင် ရှိနှင့်ပြီးသား Table များကိုပါ အချိန်ဇယားဆွဲ၍ (Schedule) Data Quality စစ်ဆေးမှုများ အလိုအလျောက် ပြုလုပ်နိုင်သည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Need to validate that data in a pipeline does not contain null values without writing custom code"** $\rightarrow$ **AWS Glue Data Quality တွင် DQDL rules များကို သုံးပါ**။
> - **"Halt the ETL pipeline if the completeness of a critical column drops below 95%"** $\rightarrow$ **Rule ကျရှုံးပါက Job ကိုပါ ရပ်တန့်ပစ်ရန် AWS Glue Data Quality တွင် Configure လုပ်ပါ**။
> - **"Route rows failing validation to a quarantine S3 bucket while letting valid rows proceed"** $\rightarrow$ **AWS Glue Data Quality ကိုသုံး၍ စစ်ဆေးမှု အောင်မြင်သော ဒေတာနှင့် ကျရှုံးသော ဒေတာကို ခွဲထုတ်ပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Overview
- `[[glue-etl-jobs]]` — Integration with Glue ETL Jobs
- `[[data-validation-and-profiling]]` — Concept: Data Validation vs Profiling
