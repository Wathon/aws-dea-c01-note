---
title: "Domain 3: Data Operations and Support (မြန်မာဘာသာ)"
type: domain
tags:
  - domain/operations
  - dea-c01
  - exam-prep
  - burmese
date: 2026-07-28
---

# ⚙️ Domain 3: Data Operations and Support (Weight: 22%)

- **Domain ID**: Domain 3
- **Language / ဘာသာစကား**: [English (Original)](/en/01-domains/domain-3-data-operations-and-support) | **မြန်မာဘာသာ (Burmese)**
- **Focus / အဓိက အာရုံစိုက်မှု**: Data pipelines များကို automate ပြုလုပ်ခြင်း၊ data quality ကို စောင့်ကြည့်စစ်ဆေးခြင်း (monitoring)၊ အမှားများကို ဖြေရှင်းခြင်း (troubleshooting errors)၊ စနစ် performance ထိန်းသိမ်းခြင်းနှင့် cost management ဆောင်ရွက်ခြင်း။
- **Hub Links**: [[mm/index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 3.1: Automate data processing workloads
- **Event-Driven Automation**: [[lambda]] သို့မဟုတ် [[glue]] jobs များကို trigger ပြုလုပ်ရန် [[cloudwatch-and-eventbridge]] (EventBridge rules, S3 Event Notifications) ကို အသုံးပြုခြင်း။
- **Infrastructure as Code (IaC)**: [[cdk-cloudformation]] (AWS CDK, CloudFormation, SAM) ကို အသုံးပြု၍ pipeline infrastructure များကို ထပ်ခါတလဲလဲ အလွယ်တကူ တည်ဆောက်နိုင်အောင် (reproducibly) deploy လုပ်ခြင်း။

### Task Statement 3.2: Monitor data pipelines and evaluate metrics
- **CloudWatch Monitoring**:
  - Metrics များကို စောင့်ကြည့်စစ်ဆေးခြင်း၊ Glue job failures သို့မဟုတ် SQS DLQ depth များအတွက် CloudWatch Alarms များ သတ်မှတ်ခြင်း။
  - CloudWatch Logs Insights ကို အသုံးပြု၍ log streams များကို ခွဲခြမ်းစိတ်ဖြာစစ်ဆေးခြင်း: [[cloudwatch-and-eventbridge]]။
- **Auditing & Event Tracking**: Pipeline components များတစ်လျှောက် API actions များကို log မှတ်တမ်းတင်ရန် AWS CloudTrail ကို အသုံးပြုခြင်း။

### Task Statement 3.3: Ensure data quality and handle pipeline errors
- **Data Quality Rule Enforcement**:
  - Dataset columns များပေါ်တွင် quality rules များကို အလိုအလျောက် audit ပြုလုပ်ရန်၊ monitor လုပ်ရန်နှင့် လိုက်နာစေရန် [[glue]] Data Quality (DQDL — Data Quality Definition Language) ကို အသုံးချခြင်း။
- **Error Handling & Dead Letter Queues (DLQ)**:
  - မအောင်မြင်သော event များကို ထိန်းသိမ်းထားရှိရန်နှင့် retry လုပ်ဆောင်မှုများကို ကိုင်တွယ်ရန် [[sqs-and-sns]] နှင့် [[lambda]] တို့တွင် DLQs များကို configure ပြုလုပ်ခြင်း။
  - [[step-functions]] တွင် retry logic နှင့် catch blocks များကို အသုံးပြုခြင်း။

### Task Statement 3.4: Optimize performance and manage costs
- **Resource Sizing & Provisioning**: EMR clusters၊ Glue DPUs (Data Processing Units) နှင့် Redshift Concurrency Scaling တို့ကို သင့်လျော်မှန်ကန်သော ပမာဏ သတ်မှတ်ခြင်း (Right-sizing)။
- **Cost Monitoring**: [[cost-management]] (AWS Cost Explorer, AWS Budgets, Savings Plans, Resource Tagging) ကို အသုံးပြုခြင်း။

---

## 🛠️ Essential AWS Services in Domain 3

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS EventBridge** | Event Router / Automation | S3 file ဖန်တီးမှု သို့မဟုတ် cron schedule အပေါ်မူတည်၍ Step Functions သို့မဟုတ် Glue workflows များကို trigger ပြုလုပ်ခြင်း | [[cloudwatch-and-eventbridge]] |
| **Amazon CloudWatch** | Logs, Metrics & Alarms | Pipeline performance alerting ပေးပို့ခြင်း၊ Insights မှတစ်ဆင့် log pattern matching ပြုလုပ်ခြင်း | [[cloudwatch-and-eventbridge]] |
| **AWS Glue Data Quality** | Data Validation | Bad data များ data warehouse များသို့ မရောက်ရှိစေရန် DQDL rules များ ရေးသားခြင်း | [[glue]] |
| **AWS SQS DLQ** | Failed Event Capture | Asynchronous debugging ပြုလုပ်ရန်အတွက် process မလုပ်နိုင်သော messages များကို သိမ်းဆည်းခြင်း | [[sqs-and-sns]] |
| **AWS Cost Explorer** | Cost Visibility | ကုန်ကျစရိတ် အများဆုံး data engineering resources များကို ဖော်ထုတ်ခြင်းနှင့် budgets များ သတ်မှတ်ခြင်း | [[cost-management]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 3

> [!IMPORTANT]
> **AWS Glue Data Quality (DQDL)**:
> - `Completeness "customer_id" > 0.99`၊ `ColumnValues "status" in ["PENDING", "COMPLETED"]` ကဲ့သို့သော rules များကို သတ်မှတ်ခွင့်ပြုသည်။
> - Rules များသည် သီးခြား validation code ရေးစရာမလိုဘဲ pipeline jobs များကို fail ဖြစ်စေနိုင်သလို bad records များကို quarantine S3 buckets များဆီသို့ လမ်းကြောင်းပြောင်း (route) ပေးပို့နိုင်သည်။

> [!TIP]
> **Handling Lambda Execution Failures**:
> - Asynchronous Lambda triggers များ (ဥပမာ - S3 event) သည် မအောင်မြင်ပါက အလိုအလျောက် ၂ ကြိမ် ထပ်မံကြိုးစားသည် (retry twice)။ Retries များ ကျရှုံးပြီးနောက် events များကို **SQS DLQ** သို့မဟုတ် **Lambda Destinations (On Failure)** သို့ ပေးပို့သင့်သည်။

---

## 📌 Checklist for Domain 3
- [ ] [[AWSCertifiedDataEngineerSlides.pdf]] ရှိ slide pages: 618-670 (Monitoring & Governance) နှင့် 756-768 (Cost Management) ကို ပြန်လည်လေ့လာသုံးသပ်ရန် (Review)
- [ ] Service notes များကို ပြီးစီးအောင် လေ့လာရန်: [[cloudwatch-and-eventbridge]], [[glue]], [[sqs-and-sns]], [[cost-management]]
- [ ] IaC ကို ပြန်လည်လေ့လာသုံးသပ်ရန်: [[cdk-cloudformation]]
