---
title: Amazon Managed Workflows for Apache Airflow (MWAA) (မြန်မာဘာသာ)
type: aws-service
category: Integration
tags:
  - aws/service
  - dea-c01
  - integration/mwaa
  - burmese
date: 2026-07-28
---

# 🌀 Amazon MWAA (Managed Workflows for Apache Airflow)

- **Category**: Application Integration / Orchestration
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/integration/mwaa-airflow) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Managed open-source Apache Airflow orchestration, Python DAG-based workflows, multi-cloud ETL coordination များ ဆောင်ရွက်ခြင်း။
- **Slide Reference**: `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)` ရှိ စာမျက်နှာ 538–541
- **Hub Links**: `[[mm/index|index]]` | `[[mm/00-hub/service-catalog|service-catalog]]` | `[[mm/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]]`

---

## 1. High-Level Summary
Amazon MWAA သည် Apache Airflow အတွက် managed orchestration service တစ်ခုဖြစ်ပြီး Python DAGs (Directed Acyclic Graphs) များကို အသုံးပြု၍ cloud ပေါ်တွင် end-to-end data pipelines များကို လွယ်ကူစွာ setup လုပ်ခြင်းနှင့် operate ပြုလုပ်ခြင်းတို့ကို ဆောင်ရွက်ပေးပါသည်။

---

## 2. Architecture & Airflow Concepts
- **DAGs (Directed Acyclic Graphs)**: Tasks များနှင့် ၎င်းတို့၏ execution order ကို သတ်မှတ်ပေးသည့် Python code ဖြစ်သည်။ MWAA အတွက် configure လုပ်ထားသော S3 bucket ထဲတွင် သိမ်းဆည်းသည်။
- **Operators**: ကြိုတင်တည်ဆောက်ထားသော building blocks များဖြစ်သည် (ဥပမာ - `BashOperator`, `PythonOperator`, `GlueJobOperator`, `AthenaOperator`, `S3ToRedshiftOperator`)။
- **Executors**: Celery Executor သည် task queue workload ပေါ် အခြေခံ၍ worker nodes များကို auto-scale ပြုလုပ်ပေးသည်။

---

## 3. MWAA vs Step Functions Decision Matrix

| Feature | AWS Step Functions | Amazon MWAA (Apache Airflow) |
| --- | --- | --- |
| **Workflow Definition** | JSON / Amazon States Language (ASL) | **Python Code (DAGs)** |
| **Serverless Nature** | Fully serverless (Zero compute management) | Managed Airflow environment (Workers auto-scale) |
| **Ecosystem** | AWS-Native service integration | Open-source Airflow operators & multi-cloud connectors |
| **Use Case** | AWS-native serverless state machines | Existing Airflow codebase သို့မဟုတ် complex Python dependency logic |

---

## 📌 Related Notes
- `[[mm/02-services/integration/step-functions/step-functions|step-functions]]` — Step Functions vs MWAA
- `[[mm/02-services/analytics-streaming/glue/glue|glue]]` — Airflow operators များမှတစ်ဆင့် Glue jobs များကို execute လုပ်ခြင်း
