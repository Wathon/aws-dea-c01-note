---
title: Athena Workgroups & Cost Management (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - governance
  - burmese
date: 2026-08-17
---

# 🛡️ Athena Workgroups & Cost Management

- **Category**: Analytics / Governance & Security
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/analytics-streaming/athena/athena-workgroups) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: အဖွဲ့အစည်းအသီးသီးအတွက် query run သည့် environment များကို ခွဲခြားထားရန်၊ ကုန်ကျစရိတ် ကန့်သတ်ချက်များ သတ်မှတ်ရန်နှင့် query history များကို သီးခြားစီထားရှိရန်။
- **Hub Links**: `[[mm/index]]` | `[[mm/athena]]` | `[[mm/domain-5-security-and-governance]]`

---

## 1. High-Level Summary

Amazon Athena သည် scan လုပ်လိုက်သော data ပမာဏအပေါ် အခြေခံပြီး (TB လျှင် $5 နှုန်းဖြင့်) ကျသင့်ငွေကို ကောက်ခံသောကြောင့်၊ ညံ့ဖျင်းစွာရေးသားထားသော query တစ်ခု (ဥပမာ - partition မခွဲထားသော Petabyte အဆင့်ရှိ table တစ်ခုပေါ်တွင် `SELECT *` အသုံးပြုခြင်း) သည် တစ်ကြိမ် run ရုံဖြင့် ဒေါ်လာထောင်ချီပြီး မတော်တဆ ကုန်ကျသွားစေနိုင်ပါသည်။

**Athena Workgroups** များကို အသုံးပြုသူများ (users)၊ အဖွဲ့များ (teams)၊ သို့မဟုတ် application များကို သီးခြားစီခွဲထားရန် အသုံးပြုပြီး၊ administrator များအနေဖြင့် တင်းကျပ်သော စီမံခန့်ခွဲမှု (governance) များကို ပြုလုပ်နိုင်ခြင်း၊ အဖွဲ့အလိုက် ကုန်ကျစရိတ်များကို ခြေရာခံနိုင်ခြင်းနှင့် ထိန်းချုပ်မရသော query များကို တားဆီးနိုင်ခြင်းတို့ကို လုပ်ဆောင်နိုင်စေပါသည်။

---

## 2. Core Capabilities of Workgroups

### 1. Cost Control & Data Usage Limits
- workgroup တစ်ခုစီအတွက် **Data Usage Control Limit** (ဥပမာ - query တစ်ခုလျှင် အများဆုံး scan လုပ်နိုင်မည့် data ပမာဏ 100 GB) ကို သတ်မှတ်နိုင်ပါသည်။
- အကယ်၍ အသုံးပြုသူတစ်ဦးသည် သတ်မှတ်ထားသော limit ထက်ပို၍ data များကို scan လုပ်ရန်ကြိုးစားသော query တစ်ခုကို run ပါက၊ အဆမတန် ကုန်ကျစရိတ်များ မဖြစ်ပေါ်စေရန် Athena က ထို query ကို **အလိုအလျောက် cancel လုပ်ပေးမည်** ဖြစ်ပါသည်။
- Limit များကို **per-query** (query တစ်ခုချင်းစီအတွက်) သို့မဟုတ် **workgroup-wide daily/hourly limit** (workgroup တစ်ခုလုံးအတွက် နေ့စဉ်/နာရီအလိုက် ကန့်သတ်ချက်) အနေဖြင့် သတ်မှတ်နိုင်ပါသည်။

### 2. Separation of Environments
- Query တိုင်းသည် သတ်မှတ်ထားသော Workgroup တစ်ခုအတွင်း၌သာ run ပါသည်။
- **Query History Isolation**: "Marketing" workgroup ရှိ အသုံးပြုသူများသည် "Finance" workgroup ၏ query history၊ သိမ်းဆည်းထားသော query များနှင့် query ရလဒ်များကို မြင်တွေ့နိုင်မည် မဟုတ်ပါ။
- **IAM Integration**: အသုံးပြုသူတစ်ဦးအား သီးခြား Workgroup တစ်ခုတည်းကိုသာ ဝင်ရောက်အသုံးပြုခွင့်ပေးရန် IAM policy များကို အသုံးပြုနိုင်ပါသည်။

### 3. Overriding Client Settings
- Workgroup တစ်ခုကို **client-side settings များကို override လုပ်ရန် (ကျော်လွန်၍ အစားထိုးသတ်မှတ်ရန်)** configure လုပ်နိုင်ပါသည်။
- ဥပမာ - အသုံးပြုသူဘက်မှ မည်သို့ပင် တောင်းဆိုထားစေကာမူ၊ သီးခြား workgroup တစ်ခုတွင် run သည့် query အားလုံး၏ ရလဒ်များကို S3 တွင် သီးခြား AWS KMS key တစ်ခုအသုံးပြု၍ အတင်းအကျပ် encrypt လုပ်ခိုင်းနိုင်ပါသည်။
- Workgroup တစ်ခုအတွက် query ရလဒ်များအားလုံးကို S3 bucket ရှိ သီးခြား path တစ်ခုသို့ မဖြစ်မနေ သိမ်းဆည်းစေရန် အတင်းအကျပ် သတ်မှတ်နိုင်ပါသည်။

### 4. CloudWatch Metrics Integration
- Workgroup များသည် query metric များ (scan လုပ်ခဲ့သော data ပမာဏ၊ query ကြာချိန်) ကို **Amazon CloudWatch** သို့ အလိုအလျောက် ပေးပို့ (publish) ပါသည်။
- ၎င်းသည် အဖွဲ့တစ်ဖွဲ့ချင်းစီအတွက် ဘေလ်ကောက်ခံမှုဆိုင်ရာ သတိပေးချက်များ (billing alerts) နှင့် dashboard များကို ပြုလုပ်နိုင်စေပါသည်။

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Prevent users from running expensive queries that scan too much data"** $\rightarrow$ **Set per-query data usage limits on Athena Workgroups** (Athena Workgroups တွင် per-query data usage limit များကို သတ်မှတ်ပါ).
> - **"Separate query history and saved queries between the Data Science and Marketing teams"** $\rightarrow$ **Create separate Athena Workgroups and assign IAM permissions** (သီးခြား Athena Workgroup များဖန်တီးပြီး IAM permission များသတ်မှတ်ပေးပါ).
> - **"Force all query results to be encrypted with a specific KMS key"** $\rightarrow$ **Configure the Workgroup to override client-side settings for output encryption** (Output encryption အတွက် client-side setting များကို ကျော်လွန်သတ်မှတ်ရန် Workgroup ကို configure လုပ်ပါ).

---

## 📌 Related Notes
- `[[mm/athena]]` — Athena Overview
- `[[mm/macie]]` — S3 data discovery and protection
- `[[mm/kms]]` — AWS Key Management Service
