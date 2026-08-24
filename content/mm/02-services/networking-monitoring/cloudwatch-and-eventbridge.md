---
title: Amazon CloudWatch & Amazon EventBridge (မြန်မာဘာသာ)
type: aws-service
category: Monitoring
tags:
  - aws/service
  - dea-c01
  - monitoring/cloudwatch
  - burmese
date: 2026-07-28
---

# 📈 Amazon CloudWatch & Amazon EventBridge

- **Category**: Management, Governance & Monitoring
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/networking-monitoring/cloudwatch-and-eventbridge) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Metrics များ၊ log aggregation၊ CloudWatch Logs Insights၊ event routing နှင့် pipeline automation rules များ။
- **Slide Reference**: `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)` မှ Pages 618–670
- **Hub Links**: `[[mm/index]]` | `[[service-catalog]]` | `[[domain-3-data-operations-and-support]]`

---

## 1. High-Level Summary
Amazon CloudWatch သည် AWS infrastructure အတွက် monitoring နှင့် telemetry data များကို ထောက်ပံ့ပေးပါသည်။ Amazon EventBridge (ယခင် CloudWatch Events) သည် data pipeline tasks များကို အလိုအလျောက် trigger ပြုလုပ်နိုင်ရန် AWS services များအကြား real-time data events များကို လမ်းကြောင်းပေးသည့် (routing) serverless event bus တစ်ခု ဖြစ်ပါသည်။

---

## 2. Technical Features

### 1. Amazon CloudWatch Features
- **CloudWatch Metrics**: AWS services များထံမှ အလိုအလျောက် စုဆောင်းရယူထားသော performance data များ (ဥပမာ - CPU utilization၊ SQS `ApproximateNumberOfMessagesVisible`)။
- **CloudWatch Alarms**: Metrics များသည် သတ်မှတ်ထားသော threshold ဘောင်ကျော်လွန်သွားသည့်အခါ notifications များ (SNS မှတစ်ဆင့်) သို့မဟုတ် auto-scaling actions များကို trigger ပြုလုပ်ပေးခြင်း။
- **CloudWatch Logs Insights**: CloudWatch Logs တွင် သိမ်းဆည်းထားသော log events များကို ရှာဖွေရန်၊ စစ်ထုတ် (filter) ရန်နှင့် ခွဲခြမ်းစိတ်ဖြာရန် အပြန်အလှန်အသုံးပြုနိုင်သော SQL-like query engine (ဥပမာ - Lambda error tracebacks များကို ရှာဖွေခြင်း)။

### 2. Amazon EventBridge Features
- **Event Rules**: ဝင်ရောက်လာသော JSON events များကို ကိုက်ညီမှုစစ်ဆေးပြီး (ဥပမာ - S3 object creation၊ Glue job state change) သက်ဆိုင်ရာ targets များ (Step Functions, Lambda, SNS) သို့ လမ်းကြောင်းပေးခြင်း။
- **Scheduled Rules (Cron)**: ထပ်ခါတလဲလဲ အချိန်သတ်မှတ်ထားသော cron schedules များအတိုင်း pipelines များကို execute ပြုလုပ်ခြင်း။
- **EventBridge Schema Registry**: Python, Java သို့မဟုတ် TypeScript တို့ဖြင့် code bindings များ generate ပြုလုပ်နိုင်ရန် event schemas များကို ရှာဖွေဖော်ထုတ်ပြီး သိမ်းဆည်းပေးခြင်း။

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **S3 ထဲသို့ file အသစ်တစ်ခု ရောက်ရှိလာချိန်တွင် Step Functions workflow တစ်ခုကို trigger ပြုလုပ်ခြင်း**: `s3:ObjectCreated` event နှင့် ကိုက်ညီသော **Amazon EventBridge rule** ကို အသုံးပြုပါ။
> - **Lambda log stream lines များစွာ (gigabytes ချီ၍) အတွင်း ရှာဖွေစစ်ဆေးခြင်း**: **CloudWatch Logs Insights** ကို အသုံးပြုပါ။

---

## 📌 Related Notes
- [[step-functions]] — EventBridge အတွက် Trigger target
- [[lambda]] — CloudWatch ထဲသို့ Lambda logging မှတ်တမ်းတင်ခြင်း
