---
title: Amazon SageMaker & AWS AI Services (မြန်မာဘာသာ)
type: aws-service
category: Machine Learning
tags:
  - aws/service
  - dea-c01
  - ml/sagemaker
  - burmese
date: 2026-07-28
---

# 🤖 Amazon SageMaker & AWS AI Services for Data Engineers

- **Category**: Machine Learning
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/ml-dev-cost/sagemaker-and-ai) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Data preparation (Data Wrangler)၊ feature management (Feature Store)၊ dataset labeling (Ground Truth)၊ generative AI (Amazon Bedrock, Amazon Q Business)။
- **Slide Reference**: `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)` မှ Pages 671–741
- **Hub Links**: [[mm/index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
Data engineer များသည် machine learning model များအတွက် သန့်စင်ပြီး စနစ်တကျ ဖွဲ့စည်းထားသော feature set များကို ထောက်ပံ့ပေးရပါသည်။ AWS သည် data engineering pipeline များအတွင်း ချိတ်ဆက်အသုံးပြုနိုင်သည့် **Amazon SageMaker** data component များနှင့် managed AI service များ (Comprehend, Rekognition, Textract, Bedrock, Amazon Q Business) ကို ထောက်ပံ့ပေးထားပါသည်။

---

## 2. Key Component Breakdown

### 1. SageMaker Components
- **SageMaker Data Wrangler**: S3, Athena, Redshift သို့မဟုတ် Snowflake တို့မှ ML အတွက် data များကို တိုက်ရိုက် import လုပ်ခြင်း၊ ပြင်ဆင်ခြင်း (prepare)၊ transform လုပ်ခြင်းနှင့် analyze လုပ်ခြင်းတို့အတွက် graphical interface တစ်ခု ဖြစ်ပါသည်။
- **SageMaker Feature Store**: Team များအကြား ML feature များကို သိမ်းဆည်းရန်၊ update လုပ်ရန်၊ ပြန်လည်ရယူရန်နှင့် မျှဝေရန် (share) အတွက် central repository ဖြစ်ပါသည်။ ၎င်းသည် **Online Store** (inference အတွက် low-latency ဖြင့် feature ရယူခြင်း) နှင့် **Offline Store** (batch training အတွက် S3 တွင် historical feature များ သိမ်းဆည်းခြင်း) နှစ်မျိုးစလုံးကို support လုပ်ပါသည်။
- **SageMaker Ground Truth**: Automated ML labeling သို့မဟုတ် လူသား annotator များ (Amazon Mechanical Turk သို့မဟုတ် private team များမှတစ်ဆင့်) ကို အသုံးပြု၍ data labeling ပြုလုပ်ပေးသည့် managed service ဖြစ်ပါသည်။

### 2. High-Level AWS AI Services
- **Amazon Comprehend**: Natural Language Processing (NLP) service ဖြစ်ပြီး — sentiment analysis၊ topic modeling နှင့် စာသားများအတွင်းမှ PII entity extraction ပြုလုပ်ခြင်းတို့အတွက် အသုံးပြုပါသည်။
- **Amazon Textract**: PDF များနှင့် scanned document များမှ စာသားများနှင့် table များကို automated စနစ်ဖြင့် ထုတ်ယူပေးသည့် (extraction) service ဖြစ်ပါသည်။
- **Amazon Rekognition**: ရုပ်ပုံ (image) နှင့် ဗီဒီယို (video) analysis ပြုလုပ်ပေးသည့် service ဖြစ်ပါသည် (object detection, facial recognition)။
- **Amazon Bedrock**: ထိပ်တန်း Foundation Model များ (Generative AI) ကို serverless စနစ်ဖြင့် အသုံးပြုနိုင်စေသည့် service ဖြစ်ပါသည်။
- **Amazon Q Business**: လုပ်ငန်းသုံး enterprise data source များ (S3, Salesforce, SharePoint) ပေါ်တွင် အခြေခံ၍ configure ပြုလုပ်ထားသော Generative AI assistant ဖြစ်ပါသည်။

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Centralized ML Feature Sharing**: **Amazon SageMaker Feature Store** ကို ရွေးချယ်ပါ။
> - **Extracting Tables & Form Fields from Scanned PDF Invoices**: **Amazon Textract** ကို ရွေးချယ်ပါ။
> - **Extracting PII Entities from Free-Form Text Documents**: **Amazon Comprehend** ကို ရွေးချယ်ပါ။

---

## 📌 Related Notes
- [[s3]] — S3 တွင် offline feature data သိမ်းဆည်းခြင်း
- [[redshift]] — Redshift ML integration
