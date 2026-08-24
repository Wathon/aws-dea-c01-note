---
title: AWS Cost Management & Optimization (မြန်မာဘာသာ)
type: aws-service
category: Cost Management
tags:
  - aws/service
  - dea-c01
  - cost
  - burmese
date: 2026-07-28
---

# 💰 AWS Cost Management & Optimization

- **Category**: Management & Governance
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/ml-dev-cost/cost-management) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Cost monitoring, budget enforcement, resource tagging, Savings Plans, Cost & Usage Reports (CUR) များ စီမံခန့်ခွဲခြင်း။
- **Slide Reference**: `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)` မှ Pages 756–768
- **Hub Links**: [[mm/index]] | [[service-catalog]] | [[domain-3-data-operations-and-support]]

---

## 1. High-Level Summary
Data engineering pipelines များသည် ကြီးမားသော data ပမာဏ (massive scale) များကို လုပ်ဆောင်ရပြီး စနစ်တကျ monitor နှင့် optimize မလုပ်ပါက ကုန်ကျစရိတ်များ အလွန်များပြားလာနိုင်ပါသည်။ AWS သည် cost allocation၊ budgeting၊ forecasting နှင့် savings commitments များအတွက် သီးသန့် tool များကို ထောက်ပံ့ပေးထားပါသည်။

---

## 2. Key Tools & Concepts

1. **AWS Cost Explorer**: ယခင် သုံးစွဲခဲ့သော ကုန်ကျစရိတ် trends များကို visualize လုပ်ပြီး ခွဲခြမ်းစိတ်ဖြာခြင်း (analyze)၊ နောင် ၁၂ လအထိ အနာဂတ်ကုန်ကျစရိတ်များကို ခန့်မှန်းတွက်ချက်ခြင်း (forecast) နှင့် Savings Plans အကြံပြုချက်များကို လေ့လာသုံးသပ်ခြင်း။
2. **AWS Budgets**: ကုန်ကျစရိတ် သို့မဟုတ် အသုံးပြုမှုသည် သတ်မှတ်ထားသော threshold ထက် ကျော်လွန်သည့်အခါ (သို့မဟုတ် ကျော်လွန်မည်ဟု ခန့်မှန်းရသည့်အခါ) email သို့မဟုတ် SNS မှတစ်ဆင့် alert ပေးပို့သည့် custom budgets များကို သတ်မှတ်ခြင်း။ Automated actions များ (ဥပမာ EC2 instances များကို Stop လုပ်ခြင်း) ကိုလည်း trigger လုပ်ဆောင်ပေးနိုင်သည်။
3. **AWS Cost & Usage Report (CUR)**: ရရှိနိုင်သမျှတွင် အပြည့်စုံဆုံးဖြစ်သော cost dataset ဖြစ်သည်။ [[athena]] ဖြင့် ခွဲခြမ်းစိတ်ဖြာနိုင်ရန် နာရီအလိုက် သို့မဟုတ် နေ့အလိုက် အသေးစိတ် granular cost files များကို CSV/Parquet format ဖြင့် S3 bucket ထဲသို့ တိုက်ရိုက် deliver လုပ်ပေးပါသည်။
4. **AWS Savings Plans & Reserved Instances**: ၁ နှစ် သို့မဟုတ် ၃ နှစ် commitment ပြုလုပ်ခြင်းဖြင့် On-Demand စျေးနှုန်းထက် ၇၂% အထိ သက်သာစေသော ပြောင်းလွယ်ပြင်လွယ်ရှိသည့် pricing model ဖြစ်သည်။
5. **Cost Allocation Tags**: အဖွဲ့ (team) သို့မဟုတ် ဌာန (department) အလိုက် ကုန်ကျစရိတ်များကို ခွဲခြမ်းစိတ်ဖြာရန် resource များသို့ သတ်မှတ်ပေးထားသော metadata tags များ (`Environment=Production`, `Project=DataLake`) ဖြစ်သည်။

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Granular Cost Querying with SQL**: S3 တွင် သိမ်းဆည်းထားသော **AWS Cost & Usage Report (CUR)** ကို **Amazon Athena** အသုံးပြု၍ query ပြုလုပ်ခြင်း။
> - **Automated Pipeline Halt on Budget Breach**: Budget သတ်မှတ်ချက် ကျော်လွန်ပါက Lambda function သို့မဟုတ် Step Functions workflow ကို invoke လုပ်ရန် SNS notification ဖြင့် **AWS Budgets** ကို configure ပြုလုပ်ခြင်း။

---

## 📌 Related Notes
- [[athena]] — SQL ဖြင့် CUR reports များကို query လုပ်ခြင်း
- [[s3]] — CUR S3 delivery target ဖြစ်ခြင်း
