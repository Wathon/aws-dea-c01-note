---
title: AWS CDK, CloudFormation & SAM (မြန်မာဘာသာ)
type: aws-service
category: Developer Tools
tags:
  - aws/service
  - dea-c01
  - dev/iac
  - burmese
date: 2026-07-28
---

# 🏗️ AWS CDK, CloudFormation & SAM (Infrastructure as Code)

- **Category**: Developer Tools
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/ml-dev-cost/cdk-cloudformation) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Infrastructure as Code (IaC)၊ data pipeline များကို automate လုပ်ပြီး deploy ပြုလုပ်ခြင်း၊ ပြန်လည်အသုံးပြုနိုင်သော stack creation ပြုလုပ်ခြင်း။
- **Slide Reference**: [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf) မှ Pages 742–755
- **Hub Links**: [[mm/index|index]] | [[mm/00-hub/service-catalog|service-catalog]] | [[mm/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]]

---

## 1. High-Level Summary
Production data engineering pipeline များကို deploy ပြုလုပ်ရာတွင် Development, Staging နှင့် Production environment များအကြား ကိုက်ညီမှုရှိစေရန် (consistent)၊ ထပ်ခါတလဲလဲ ပြုလုပ်နိုင်စေရန် (repeatable) နှင့် version-controlled ဖြစ်သော infrastructure ရရှိစေရန်အတွက် Infrastructure as Code (IaC) လိုအပ်ပါသည်။

---

## 2. Tool Breakdown

| Tool | Format | Ideal Use Case |
| --- | --- | --- |
| **AWS CloudFormation** | Declarative JSON / YAML templates | Native AWS IaC stack deployment နှင့် rollback safety ရရှိစေခြင်း။ |
| **AWS CDK (Cloud Development Kit)** | Imperative code (Python, TypeScript, Java) | ရင်းနှီးကျွမ်းဝင်ပြီးသား programming language များကို အသုံးပြု၍ data pipeline များကို သတ်မှတ်နိုင်ခြင်း၊ CloudFormation template များအဖြစ် compile လုပ်ပေးခြင်း။ |
| **AWS SAM (Serverless Application Model)** | Shorthand YAML extending CloudFormation | Serverless ဖြစ်သော Lambda, API Gateway နှင့် DynamoDB resource များကို သတ်မှတ်တည်ဆောက်ရန် အထူးပြုလုပ်ထားသည့် framework ဖြစ်ခြင်း။ |

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Region အများအပြားတွင် standard pipeline resource များကို programmatic နည်းလမ်းဖြင့် deploy ပြုလုပ်ခြင်း**: **AWS CloudFormation StackSets** ကို အသုံးပြုပါ။
> - **Python code ဖြင့် ရှုပ်ထွေးသော Glue / Step Functions pipeline များကို သတ်မှတ်ရေးသားခြင်း**: **AWS CDK** ကို အသုံးပြုပါ။

---

## 📌 Related Notes
- [[mm/02-services/compute-containers/lambda|lambda]] — SAM deployment target
- [[mm/02-services/integration/step-functions/step-functions|step-functions]] — CDK workflow deployment
