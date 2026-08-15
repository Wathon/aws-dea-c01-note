---
title: AWS Glue DataBrew (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - databrew
  - burmese
date: 2026-08-15
---

# ☕ AWS Glue DataBrew (Code မလိုသော Visual Data Preparation)

- **Category**: Analytics / Visual Data Preparation
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-databrew.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Data Analysts နှင့် Data Scientists များအနေဖြင့် PySpark / SQL Code ရေးစရာမလိုဘဲ UI မှတစ်ဆင့် ဒေတာများကို သန့်စင်ခြင်း၊ ပြင်ဆင်ခြင်း (Visual ETL)။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue DataBrew** သည် Analytics နှင့် Machine Learning ပြုလုပ်မည့် ဒေတာများကို Code လုံးဝရေးစရာမလိုဘဲ (No-code) အလွယ်တကူ သန့်စင်ခြင်း (Cleaning) နှင့် ပုံမှန်ဖြစ်အောင် ပြင်ဆင်ခြင်း (Normalization) တို့ ပြုလုပ်ပေးနိုင်သော Visual Data Preparation Tool တစ်ခုဖြစ်သည်။ DEA-C01 စာမေးပွဲတွင် Data Analyst များအတွက် **No-code Data Preparation** ဟုမေးလာပါက DataBrew သည် အဓိက အဖြေဖြစ်သည်။

---

## ၂။ အဓိက စွမ်းဆောင်ရည်များ

- **Visual Interface**: ဒေတာများကို မျက်စိဖြင့် မြင်သာအောင် Spreadsheet (Excel ကဲ့သို့) ပုံစံဖြင့် ဖော်ပြပေးသည်။
- **Pre-built Transformations**: မှားယွင်းနေသော ဒေတာများကို ဖယ်ရှားခြင်း၊ Format ပြောင်းခြင်း၊ ကွက်လပ် (Missing values) များကို ဖြည့်တင်းခြင်း စသည့် Data Preparation အဆင့်များအတွက် **Code ရေးစရာမလိုသော Built-in Transformations ၂၅၀ ကျော်** အသင့်ပါဝင်သည်။
- **Data Profiling**: ဒေတာများ၏ အရည်အသွေးကို စစ်ဆေးပေးသည့် Statistics များ၊ Correlations များနှင့် Distribution များကို Visual Graphs များဖြင့် အလိုအလျောက် ပြသပေးသည်။
- **Data Lineage**: ဒေတာစတင်ထွက်ရှိလာရာ နေရာနှင့် ၎င်းကို မည်ကဲ့သို့ အဆင့်ဆင့် ပြောင်းလဲ (Transform) ခဲ့သည်ကို မြေပုံကဲ့သို့ ရှင်းလင်းစွာ ပြသပေးသည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Empower business analysts to clean, normalize, and prepare datasets without writing PySpark or SQL code"** $\rightarrow$ **AWS Glue DataBrew ဖြင့် Visual ETL ပြုလုပ်ပါ**။
> - **"Need over 200 pre-built transformations for visual data cleaning"** $\rightarrow$ **AWS Glue DataBrew ကို သုံးပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Overview
- `[[glue-etl-jobs]]` — Code-based ETL alternatives
