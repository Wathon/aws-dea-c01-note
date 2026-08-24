---
title: AWS Step Functions vs. Amazon MWAA (Airflow), Observability & Troubleshooting (မြန်မာဘာသာ)
type: aws-service
category: Integration
tags:
  - aws/service
  - dea-c01
  - integration/step-functions
  - mwaa-comparison
  - airflow-comparison
  - troubleshooting
  - cloudwatch-metrics
  - x-ray
  - burmese
date: 2026-08-21
---

# 🔍 AWS Step Functions vs. Amazon MWAA (Airflow), Observability & Troubleshooting (မြန်မာဘာသာ)

- **Category**: Application Integration / Orchestrator Comparison, Observability & Production Triage
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/integration/step-functions/step-functions-vs-mwaa-and-troubleshooting) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: AWS Step Functions နှင့် Amazon MWAA (Apache Airflow) တို့အကြား ရွေးချယ်ခြင်း၊ CloudWatch နှင့် AWS X-Ray monitoring တို့ကို configure လုပ်ခြင်းနှင့် အဖြစ်များသော production state machine errors များကို ဖြေရှင်းခြင်း။
- **Slide Reference**: `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)` ရှိ စာမျက်နှာ 526–529
- **Hub Links**: `[[mm/index|index]]` | `[[mm/02-services/integration/step-functions/step-functions|step-functions]]` | `[[mm/02-services/integration/mwaa-airflow|mwaa-airflow]]` | `[[mm/02-services/networking-monitoring/cloudwatch-and-eventbridge|cloudwatch-and-eventbridge]]` | `[[mm/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]]`

---

## 1. High-Level Summary

**DEA-C01** စာမေးပွဲတွင် အဓိကကျသော architectural decision တစ်ခုမှာ သင့်လျော်မှန်ကန်သည့် data orchestration service ကို ရွေးချယ်ခြင်းဖြစ်သည်- **AWS Step Functions** (serverless, event-driven state machines) သို့မဟုတ် **Amazon MWAA / Apache Airflow** (Python-based, complex programmatic DAG orchestration)။

ထို့အပြင် data engineers များအနေဖြင့် **Amazon CloudWatch** နှင့် **AWS X-Ray** တို့ကို အသုံးပြု၍ workflows များကို မည်သို့ monitor လုပ်ရမည်၊ **`States.DataLimitExceeded`** နှင့် **task timeout failures** ကဲ့သို့သော အဖြစ်များသည့် runtime ပြဿနာများကို မည်သို့ debug လုပ်ရမည်ကို မဖြစ်မနေ နားလည်သဘောပေါက်ထားရပါမည်။

---

## 2. Step Functions vs. Amazon MWAA vs. EventBridge

| Architectural Dimension | AWS Step Functions | Amazon MWAA (Apache Airflow) | Amazon EventBridge |
| :--- | :--- | :--- | :--- |
| **Primary Paradigm** | **Serverless State Machine** orchestration။ | **Programmatic Python DAG** workflow engine။ | **Stateless Event Router** နှင့် Event Bus။ |
| **Definition Model** | **Amazon States Language (ASL - JSON)** / Visual Workflow Studio။ | **Python Code (DAGs)**။ | **JSON Event Pattern Rules**။ |
| **Infrastructure Management** | **100% Serverless** (Zero infrastructure, zero server provisioning)။ | Managed EC2/Fargate instances များ (Webservers, Workers, Schedulers)။ | **100% Serverless**။ |
| **Ecosystem & Connectors** | Native **AWS Service Integrations** များ (Glue, EMR, Athena တို့အတွက် .sync)။ | **ကျယ်ပြန့်သော Open-Source Provider Ecosystem** (Snowflake, Databricks, GCP, Azure)။ | Native AWS targets နှင့် 300+ SaaS event sources များ။ |
| **Data Lineage & Backfills** | အခြေခံ CloudWatch logs / X-Ray traces များ။ | **Historical backfills အတွက် Rich UI**, task reruns နှင့် lineage။ | မရှိပါ (None)။ |
| **Throughput & Speed** | Sub-millisecond state transitions, Express workflows >100k TPS။ | Polling-based scheduling latency (စက္ကန့်ပိုင်းမှ မိနစ်ပိုင်းအထိ)။ | Sub-second event routing။ |
| **Cost Model** | Pay-per-state-transition (Standard) သို့မဟုတ် duration (Express)။ | Environment အတွက် Hourly base fee + worker instance hours။ | routed လုပ်သည့် events တစ်သန်းလျှင် ကျသင့်ငွေ (Pay-per-million events routed)။ |

```mermaid
graph TD
    subgraph Decision_Matrix["Orchestrator ဆုံးဖြတ်ချက်ဆိုင်ရာ Framework (Decision Framework)"]
        Choice{"Workload ၏ သွင်ပြင်လက္ခဏာများ (Characteristics)?"}

        Choice -->|Pure AWS Serverless / Event-Driven / ထိန်းသိမ်းမှု နည်းပါးခြင်း (Low Maintenance)| SFN["✅ AWS Step Functions"]
        Choice -->|Complex Multi-Cloud ETL / Python-native DAGs / လက်ရှိသုံးနေသော Legacy Airflow| MWAA["✅ Amazon MWAA (Airflow)"]
        Choice -->|State မပါသော ရိုးရှင်းသည့် Event Routing / Fan-Out| EB["✅ Amazon EventBridge"]
    end

    classDef dec fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a;
    classDef opt fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class Choice dec;
    class SFN,MWAA,EB opt;
```

---

## 3. Observability: CloudWatch Metrics & AWS X-Ray Tracing

### အဓိက Amazon CloudWatch Metrics များ:
- **`ExecutionsFailed`**: မအောင်မြင်ဘဲ ကျရှုံးသွားသော state machine execution အရေအတွက် (operational alarms များကို trigger လုပ်သည်)။
- **`ExecutionsTimedOut`**: သတ်မှတ်ထားသော timeout limit ထက် ကျော်လွန်သွားသော execution အရေအတွက်။
- **`ExecutionTime`**: State machines များ ပြီးဆုံးသည်အထိ ကြာမြင့်သည့် စုစုပေါင်းအချိန် (pipeline performance ကျဆင်းမှုကို စောင့်ကြည့်စစ်ဆေးသည်)။
- **`ExecutionsSucceeded`**: အောင်မြင်စွာ run ပြီးမြောက်ခဲ့သော အရေအတွက်။

### AWS X-Ray Tracing:
- Step Functions state machine ပေါ်တွင် **AWS X-Ray Tracing** ကို enable ပြုလုပ်ခြင်းသည် end-to-end distributed trace map ကို ပေးစွမ်းနိုင်ပါသည်။
- Lambda၊ API calls များနှင့် downstream database operations များတစ်လျှောက် latency bottlenecks (ကြာချိန်နှောင့်နှေးမှုများ) ကို မြင်သာအောင် ဖော်ပြပေးပါသည်။

---

## 4. Master Troubleshooting Cheat Sheet

| Production Error / ရောဂါလက္ခဏာ (Symptom) | မူလဇစ်မြစ် အကြောင်းရင်း (Root Cause) | ဖြေရှင်းနည်းနှင့် ပြင်ဆင်မှု (Remediation & Fix) |
| :--- | :--- | :--- |
| **`States.DataLimitExceeded`** | State payload သည် **256 KB JSON limit** ထက် ကျော်လွန်သွားခြင်း (ဥပမာ- ကြီးမားသော array တစ်ခုကို state input တွင် တိုက်ရိုက် pass လုပ်ခြင်း)။ | **ကြီးမားသော payload ကို Amazon S3 သို့ offload လုပ်ပါ** ပြီးနောက် states များအကြား `s3://` URI ကိုသာ pass လုပ်ပါ၊ သို့မဟုတ် **Distributed Map** သို့ ပြောင်းလဲအသုံးပြုပါ။ |
| **S3 data မရှိသေးသောကြောင့် Downstream state ကျရှုံးခြင်း (Race Condition)** | Upstream task သည် job ပြီးဆုံးသည်အထိ စောင့်ဆိုင်းမည့်အစား default Request-Response ကို အသုံးပြုခဲ့ခြင်း။ | Task Resource ARN ၏ အဆုံးတွင် **`.sync`** ကို ထည့်သွင်းပါ (ဥပမာ- `arn:aws:states:::glue:startJobRun.sync`)။ |
| **Task သည် `States.Timeout` ဖြင့် ကျရှုံးခြင်း** | Task သည် default သို့မဟုတ် configure လုပ်ထားသော `TimeoutSeconds` ထက် ကျော်လွန်သွားခြင်း။ | `TimeoutSeconds` ကို တိုးမြှင့်ပေးပါ သို့မဟုတ် အောက်ခြေရှိ Lambda / Glue job သည် ရပ်တန့် (hanging ဖြစ်) နေခြင်း ရှိ/မရှိ စစ်ဆေးပါ။ |
| **Task သည် `States.Permissions` ဖြင့် ကျရှုံးခြင်း** | Step Functions execution role တွင် target service API အတွက် IAM permissions များ မရှိခြင်း။ | Step Functions Role တွင် `glue:StartJobRun`၊ `athena:StartQueryExecution` စသည်တို့ကို ခွင့်ပြုပေးသည့် လိုအပ်သော IAM policy ကို တွဲချိတ် (attach) ပါ။ |
| **Console တွင် Express Workflow steps များကို စစ်ဆေးကြည့်ရှု၍ မရခြင်း** | Express workflows များသည် visual execution history ကို console ထဲတွင် သိမ်းဆည်းမထားခြင်း။ | Express state machine settings တွင် **CloudWatch Logs integration** ကို enable ပြုလုပ်ပြီး CloudWatch log streams များကို စစ်ဆေးပါ။ |

---

## 5. DEA-C01 Exam Essentials

> [!IMPORTANT]
> **Key Exam Decision Triggers for Orchestrator Selection & Triage**:
>
> - **"Multi-cloud systems တစ်လျှောက် ရှုပ်ထွေးသော DAG dependencies များပါဝင်ပြီး data pipelines အားလုံးကို Python သီးသန့်ဖြင့်သာ ရေးသားသော engineering team အတွက် Step Functions နှင့် Airflow အကြား ရွေးချယ်ပါ"** $\rightarrow$ **Amazon MWAA (Managed Workflows for Apache Airflow)** ကို ရွေးချယ်ပါ။
> - **"Server management လုံးဝမလို (ZERO server management)၊ serverless visual workflows များကို ထောက်ပံ့ပေးပြီး AWS Glue `.sync` နှင့် natively ချိတ်ဆက်ပေးနိုင်သော orchestration service ကို ရွေးချယ်ပါ"** $\rightarrow$ **AWS Step Functions** ကို ရွေးချယ်ပါ။
> - **"Step Functions ရှိ `States.DataLimitExceeded` error ကို ဖြေရှင်းပါ"** $\rightarrow$ **ကြီးမားသော payload ကို Amazon S3 တွင် သိမ်းဆည်းပြီး** state payload ထဲတွင် S3 object reference ကို pass လုပ်ပါ။
> - **"Step Functions task တစ်ခုသည် Athena ကို မ trigger မချင်း AWS Glue job ပြီးဆုံးသည်အထိ စောင့်ဆိုင်းစေရန် သေချာစေပါ"** $\rightarrow$ **Optimized Integration pattern (`glue:startJobRun.sync`)** ကို အသုံးပြုပါ။

---

## 📌 Related Notes
- `[[mm/02-services/integration/step-functions/step-functions|step-functions]]` — Step Functions Master Hub
- `[[mm/02-services/integration/mwaa-airflow|mwaa-airflow]]` — Amazon MWAA Deep-Dive Suite
- `[[mm/02-services/integration/step-functions/step-functions-service-integrations-and-sync-patterns|step-functions-service-integrations-and-sync-patterns]]` — Service Integrations (.sync)
- `[[mm/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]]` — CloudWatch & Incident Triage
