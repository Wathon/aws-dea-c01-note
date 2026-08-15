---
title: AWS Glue ETL Jobs & DynamicFrames (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - etl
  - spark
  - burmese
date: 2026-08-15
---

# ⚙️ AWS Glue ETL Jobs & DynamicFrames (Serverless Spark ETL နှင့် DynamicFrames)

- **Category**: Analytics / Distributed Processing
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/analytics-streaming/glue/glue-etl-jobs.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Apache Spark ဖြင့် Serverless ဒေတာပြောင်းလဲခြင်း (Transformations)၊ အသစ်ဝင်လာသော ဒေတာများကိုသာ ရွေးချယ်လုပ်ဆောင်ခြင်း (Incremental Processing)၊ ဖော်မတ်မကျသော Semi-structured ဒေတာများကို ကိုင်တွယ်ခြင်း။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[emr]]` | `[[domain-3-data-processing]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Glue ETL Jobs** သည် Apache Spark (PySpark သို့မဟုတ် Scala) နှင့် Python Shell များကို အသုံးပြု၍ Serverless အနေဖြင့် ဒေတာပြောင်းလဲမှု (Data Transformation) များကို လုပ်ဆောင်ပေးသည်။ **[[emr]]** တွင်ကဲ့သို့ Cluster များကို ကိုယ်တိုင်တည်ဆောက်၊ ချိန်ညှိ၊ ဖျက်သိမ်းရန် မလိုဘဲ AWS မှ Worker Nodes များကို အလိုအလျောက် စီမံပေးသဖြင့် Data Engineer များသည် Transformation Logic ရေးသားခြင်းကိုသာ အာရုံစိုက်နိုင်သည်။

---

## ၂။ DEA-C01 အတွက် အဓိက အချက်အလက်များ

### 1. Glue DynamicFrames vs. Spark DataFrames
ပုံမှန် Apache Spark တွင် တိကျသော Schema ရှိရန် လိုအပ်သည့် DataFrames များကို သုံးသော်လည်း AWS Glue တွင် **DynamicFrames** ကို မိတ်ဆက်ထားသည်။
- **DynamicFrames** သည် ကြိုတင်သတ်မှတ်ထားသော Schema မလိုအပ်ဘဲ Row တစ်ကြောင်းချင်းစီအလိုက် Schema ကို အလိုအလျောက် သတ်မှတ်ပေးသည်။
- ဥပမာ- JSON ဖိုင်များတွင် Data Field အချို့ ပျောက်နေခြင်း၊ Column တစ်ခုတည်းတွင် Row 1 ၌ `Integer` ဖြစ်နေပြီး Row 2 ၌ `String` ဖြစ်နေခြင်း စသည့် ဖော်မတ်မကျသော ပြဿနာများကို Error မတက်စေဘဲ ဖြေရှင်းပေးနိုင်သည်။
- Data Types နှစ်မျိုးဖြစ်နေပါက "Choice" အမျိုးအစားအဖြစ် မှတ်သားထားပြီး နောက်ပိုင်းမှ `ResolveChoice` transform ဖြင့် ဖြေရှင်းနိုင်သည်။

### 2. Job Bookmarks (အသစ်ဝင်လာသော ဒေတာများကိုသာ လုပ်ဆောင်ခြင်း)
- **Glue Job Bookmarks** သည် ယခင်အကြိမ် Job Run ခဲ့စဉ်က မည်သည့်ဒေတာများကို လုပ်ဆောင်ပြီးသွားပြီလဲ ဆိုသည်ကို အလိုအလျောက် မှတ်သားထားသည်။
- ထို့ကြောင့် Job ကို ထပ်မံ Run သည့်အခါ S3 သို့ **အသစ်ရောက်ရှိလာသော ဖိုင်များကိုသာ (Incremental Processing)** ရွေးချယ်လုပ်ဆောင်ပေးသည်။
- **စာမေးပွဲ အကြံပြုချက်**: ကိုယ်ပိုင် ခြေရာခံစနစ်များကို DynamoDB ဖြင့် တည်ဆောက်စရာမလိုဘဲ Incremental Processing ရရှိစေသော Built-in နည်းလမ်းဖြစ်သည်။

### 3. Pushdown Predicates (S3 Partition များကို ကြိုတင် စစ်ထုတ်ခြင်း)
- S3 မှ Partitioned Data များကို ဖတ်ရာတွင် Glue script ထဲ၌ **Pushdown Predicates** ကို ထည့်သွင်း အသုံးပြုနိုင်သည်။
- ဒေတာအားလုံးကို Spark memory ထဲသို့ ဆွဲတင်ပြီးမှ Filter လုပ်မည့်အစား၊ Pushdown Predicates သည် S3 directory level တွင်သာ **ဖတ်မည့်ဒေတာများကို ကြိုတင်ရွေးချယ် စစ်ထုတ်** ပေးသည်။
- **စာမေးပွဲ အကြံပြုချက်**: ဤနည်းလမ်းသည် မလိုအပ်သော ဒေတာများကို ဖတ်ရှုခြင်းမှ သက်သာစေသဖြင့် I/O ကုန်ကျစရိတ်ကို လျှော့ချပေးပြီး Query အမြန်နှုန်းကို များစွာ တိုးတက်စေသည်။

### 4. Built-in Machine Learning Transforms (`FindMatches`)
- **FindMatches** သည် AWS Glue တွင် အသင့်ပါဝင်သော ML Transform တစ်ခုဖြစ်ပြီး **ဒေတာများ ထပ်နေခြင်းကို ရှာဖွေဖယ်ရှားရာတွင် (Data deduplication)** အဓိက အသုံးပြုသည်။
- ဥပမာ - Customer list တွင် Unique ID မပါဘဲ "John Doe" နှင့် "J. Doe" ဟု ကွဲလွဲနေပါက၊ ရှုပ်ထွေးသော String matching code များ ရေးစရာမလိုဘဲ `FindMatches` က ၎င်းတို့သည် လူတစ်ဦးတည်းဖြစ်ကြောင်း Machine Learning ဖြင့် ခွဲခြားပေးနိုင်သည်။

### 5. Worker Types (Capacity ရွေးချယ်ခြင်း)
Workload အပေါ်မူတည်၍ အောက်ပါ Worker အမျိုးအစားများကို ရွေးချယ်နိုင်သည်-
- **`G.1X`**: 1 DPU, 4 vCPU, 16 GB memory. ပုံမှန် Spark ETL များအတွက်။
- **`G.2X`**: 2 DPU, 8 vCPU, 32 GB memory. Memory အများအပြားလိုအပ်သော ကြီးမားသည့် Joins များ၊ Machine Learning Transforms များအတွက်။
- **`G.025X`**: 0.25 DPU. သေးငယ်သော Python shell jobs များနှင့် ပေါ့ပါးသော Streaming များအတွက်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များ (Exam Tips)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Process nested, semi-structured JSON with changing data types without failing"** $\rightarrow$ **AWS Glue DynamicFrames နှင့် `ResolveChoice` ကိုသုံးပါ**။
> - **"Process only the newly arrived S3 files without maintaining custom tracking logic"** $\rightarrow$ **AWS Glue Job Bookmarks ကို ဖွင့်ပါ**။
> - **"Need to run a serverless Spark job to aggregate 10 TB of data with heavy joins"** $\rightarrow$ **Memory လိုအပ်ချက်များသောကြောင့် AWS Glue ETL Jobs တွင် `G.2X` workers များကို သုံးပါ**။
> - **"Optimize S3 reads by filtering out irrelevant partitions before loading data into memory"** $\rightarrow$ **Pushdown Predicates ကို သုံးပါ**။
> - **"Deduplicate records across two tables without a unique identifier using Machine Learning"** $\rightarrow$ **`FindMatches` transform ကို သုံးပါ**။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[glue]]` — AWS Glue Overview
- `[[glue-databrew]]` — Visual ETL alternatives
- `[[emr]]` — Amazon EMR (Cluster-based Spark alternative)
