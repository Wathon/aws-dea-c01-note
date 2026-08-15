---
title: AWS Glue Studio (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - visual-etl
  - burmese
date: 2026-08-15
---

# 🎨 AWS Glue Studio (Visual ETL တည်ဆောက်ခြင်း)

- **Category**: Analytics / Visual ETL & Monitoring
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-studio.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: AWS Glue ETL jobs များကို Drag-and-drop ပြုလုပ်နိုင်သော Visual Interface ဖြင့် ရေးဆွဲခြင်း၊ Run ခြင်းနှင့် စောင့်ကြည့်စစ်ဆေးခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[glue-etl-jobs]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue Studio** သည် Data Engineer များနှင့် ETL Developer များအတွက် PySpark သို့မဟုတ် Scala Code များကို အစကနေ ကိုယ်တိုင်ရေးစရာမလိုဘဲ မျက်စိဖြင့်မြင်သာသော (Graphical, Drag-and-drop) Interface မှတစ်ဆင့် Data Integration Pipeline များကို အလွယ်တကူ တည်ဆောက်ခွင့်ပေးသော ဝန်ဆောင်မှုဖြစ်သည်။ သင် Visual အနေဖြင့် ဆွဲလိုက်သော Pipeline ပုံစံများကို S3 နောက်ကွယ်တွင် PySpark Code အဖြစ် အလိုအလျောက် ပြောင်းလဲ ရေးသားပေးသည်။

---

## ၂။ အဓိက စွမ်းဆောင်ရည်များ

### 1. Visual Job Authoring
- **Drag-and-Drop Nodes**: Source (ဒေတာရင်းမြစ်)၊ Transform (ဒေတာပြောင်းလဲမှု) နှင့် Target (ဒေတာသိမ်းဆည်းမည့်နေရာ) များကို Nodes လေးများအဖြစ် ဆက်သွယ်ပေးရုံဖြင့် Pipeline တစ်ခု တည်ဆောက်နိုင်သည်။
- **Built-in Transformations**: မလိုအပ်သော Null values များ ဖယ်ရှားခြင်း၊ ကော်လံအမည်များ ပြောင်းခြင်း၊ Join လုပ်ခြင်းနှင့် အထပ်ထပ်ဖြစ်နေသော JSON များကို ဖြန့်ထုတ်ခြင်း (Relationalize) စသည်တို့ကို အလွယ်တကူ ထည့်သွင်းနိုင်သည်။
- **Code Generation**: သင်တည်ဆောက်လိုက်သော ပုံ (Visual DAG) ကို အလိုအလျောက် Apache Spark code သို့ ပြောင်းပေးပြီး၊ လိုအပ်ပါက ၎င်း Code ကို ကိုယ်တိုင် ဝင်ရောက် ပြင်ဆင်နိုင်သည်။

### 2. Job Monitoring Dashboard
- Glue Studio တွင် AWS အကောင့်တစ်ခုလုံးရှိ Glue ETL jobs အားလုံး၏ အခြေအနေနှင့် စွမ်းဆောင်ရည်ကို စောင့်ကြည့်နိုင်သော ဗဟို Dashboard ပါဝင်သည်။
- Job များ အောင်မြင်မှု/ကျရှုံးမှုနှုန်း၊ ကြာချိန်နှင့် Resource အသုံးပြုမှု (Resource utilization) များကို တစ်နေရာတည်းတွင် ကြည့်ရှုနိုင်သည်။

### 3. Notebook Integration
- အကယ်၍ Visual UI တွင် မပါဝင်သော သီးသန့် Transform များ လိုအပ်ပါက Glue Studio ထဲတွင် Built-in Jupyter Notebooks များကို တိုက်ရိုက် ဖွင့်၍ Code ရေးသားနိုင်သည်။

---

## ၃။ Glue Studio နှင့် Glue DataBrew နှိုင်းယှဉ်ချက်

| Feature | AWS Glue Studio | AWS Glue DataBrew |
| :--- | :--- | :--- |
| **အဓိက အသုံးပြုသူ** | **ETL Developers / Data Engineers** | **Data Analysts / Data Scientists** |
| **ရရှိလာသော ရလဒ်** | PySpark / Scala **ETL Code** ကို ထုတ်ပေးသည် | Data Preparation **Recipes** ကို ထုတ်ပေးသည် |
| **ရှုပ်ထွေးမှု** | ရှုပ်ထွေးသော Joins၊ Partitions နှင့် Large-scale ETL များကို ကိုင်တွယ်နိုင်သည် | ဒေတာများ သန့်စင်ခြင်း (Cleaning, Normalization, Profiling) ကိုသာ အဓိကထားသည် |
| **နောက်ကွယ်ရှိ အင်ဂျင်** | Apache Spark | Pre-built transformations engine |

---

## ၄။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Author and monitor Apache Spark ETL jobs using a visual, drag-and-drop interface that automatically generates PySpark code"** $\rightarrow$ **AWS Glue Studio ကို ရွေးချယ်ပါ**။
> - **"Need a central dashboard to monitor the status, execution times, and resource usage of all Glue jobs across the account"** $\rightarrow$ **AWS Glue Studio Job Monitoring**။
> - **"Business analysts need to clean data without writing code"** $\rightarrow$ *သတိပြုရန်! ၎င်းသည် Glue Studio မဟုတ်ဘဲ **Glue DataBrew** ဖြစ်သည်*။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue-etl-jobs]]` — Code-based AWS Glue ETL Jobs
- `[[glue-databrew]]` — Visual Data Preparation for Analysts
