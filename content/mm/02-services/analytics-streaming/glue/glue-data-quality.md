---
title: AWS Glue Data Quality (မြန်မာဘာသာ)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - data-quality
  - governance
  - burmese
date: 2026-08-17
---

# ✅ AWS Glue Data Quality

- **Category**: Analytics / Data Governance & Validation
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/analytics-streaming/glue/glue-data-quality) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: အလိုအလျောက် data quality တိုင်းတာခြင်း၊ declarative DQDL rule စစ်ဆေးအတည်ပြုခြင်း၊ ချို့ယွင်းနေသော pipeline များကို circuit breaking လုပ်ခြင်း နှင့် မမှန်ကန်သော record များကို သီးခြားခွဲထုတ်ခြင်း (quarantining)။
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[glue]]` | `[[glue-etl-jobs]]` | `[[data-validation-and-profiling]]`

---

## 1. High-Level Summary (အကျဉ်းချုပ် ခြုံငုံသုံးသပ်ချက်)

**AWS Glue Data Quality** သည် serverless ဖြစ်ပြီး declarative နည်းလမ်းဖြင့် data quality တိုင်းတာခြင်းနှင့် စစ်ဆေးအတည်ပြုခြင်း (validation) ပြုလုပ်ပေးသည့် engine တစ်ခု ဖြစ်သည်။ Dataset ၏ မှန်ကန်မှုကို စစ်ဆေးအတည်ပြုရန် data engineer များအနေဖြင့် ရှုပ်ထွေးသော custom PySpark unit-testing logic ကုဒ်လိုင်း ရာပေါင်းများစွာ ရေးသားရန် မလိုတော့ဘဲ၊ AWS Glue Data Quality သည် **DQDL (Data Quality Definition Language)** ကို အသုံးပြုသည်။

၎င်းသည် operational mode နှစ်မျိုးဖြင့် data quality ကို စစ်ဆေးအကဲဖြတ် (evaluate) နိုင်ပါသည်:
1. **Data at Rest**: **[[glue-data-catalog]]** ထဲရှိ table များပေါ်တွင် တိုက်ရိုက် run သော scheduled သို့မဟုတ် on-demand စစ်ဆေးအကဲဖြတ်မှုများ။
2. **Data in Transit**: **[[glue-etl-jobs]]** သို့မဟုတ် Glue Studio pipeline များအတွင်း ထည့်သွင်းထားသော real-time evaluation node များ။

```mermaid
graph TD
    subgraph DataSources["Incoming ETL Stream / S3 Table"]
        RawData["Raw Input DynamicFrame / S3 Lake"]
    end

    subgraph DataQualityEngine["AWS Glue Data Quality Engine"]
        DQDL["DQDL Ruleset Evaluation (Completeness, Uniqueness, Ranges)"]
        RuleEval{"Pass or Fail?"}
    end

    subgraph ActionsOnFailure["Action on Failure"]
        FailJob["(1) Fail Job Immediately (Pipeline Circuit Breaker)"]
        Quarantine["(2) Split Dataset: Route Bad Rows to S3 Quarantine Bucket"]
        CloudWatch["(3) Publish Metrics to CloudWatch & EventBridge (SNS Alert)"]
    end

    subgraph CleanDataTarget["Curated Analytics Target"]
        CleanData[("S3 Curated Lake / Redshift Warehouse")]
    end

    RawData --> DQDL
    DQDL --> RuleEval
    RuleEval -->|Pass| CleanData
    RuleEval -->|Fail (Threshold Breached)| FailJob
    RuleEval -->|Fail (Record Level)| Quarantine
    RuleEval -->|Metrics| CloudWatch

    classDef source fill:#8b5cf6,stroke:#fff,stroke-width:1px,color:#fff;
    classDef engine fill:#3b82f6,stroke:#fff,stroke-width:1px,color:#fff;
    classDef fail fill:#ef4444,stroke:#fff,stroke-width:1px,color:#fff;
    classDef target fill:#10b981,stroke:#fff,stroke-width:1px,color:#fff;

    class RawData source;
    class DQDL,RuleEval engine;
    class FailJob,Quarantine,CloudWatch fail;
    class CleanData target;
```

---

## 2. Core Technical Capabilities (အဓိက နည်းပညာဆိုင်ရာ စွမ်းဆောင်ရည်များ)

### 1. Data Quality Definition Language (DQDL)

DQDL သည် data quality ဆိုင်ရာ assertions များကို ဖော်ပြရန် အသုံးပြုသည့် လူဖတ်ရလွယ်ကူသော (human-readable) domain-specific language တစ်ခု ဖြစ်သည်။ Assertions များကို **Ruleset** တစ်ခုအဖြစ် စုစည်းထားရှိသည်။

#### ပြည့်စုံသော DQDL Rule Syntax ဥပမာများ (Complete DQDL Rule Syntax Examples):
```text
Rules = [
    # 1. Dataset-level completeness and size assertions
    RowCount > 0,
    Completeness "email" >= 0.98,              # 98% of rows must have non-null email
    IsComplete "customer_id",                   # 100% of rows must be non-null

    # 2. Uniqueness & Key integrity
    IsUnique "customer_id",                     # Zero duplicate customer IDs
    Uniqueness "order_id" >= 0.99,

    # 3. Column value ranges and allowable sets
    ColumnValues "status" in ["PENDING", "PROCESSING", "SHIPPED", "CANCELLED"],
    ColumnValues "age" between 18 and 120,
    ColumnValues "total_amount" > 0.0,

    # 4. String formatting & Length assertions
    ColumnLength "postal_code" = 5,
    ColumnValues "email" matches "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",

    # 5. Statistical distribution checks
    StandardDeviation "salary" < 50000,
    Mean "transaction_amount" between 50 and 200,

    # 6. Custom SQL validation logic
    CustomSql "SELECT COUNT(*) FROM primary WHERE amount < 0" = 0
]
```

---

### 2. Automatic Rule Recommendation Engine (အလိုအလျောက် Rule အကြံပြုပေးသည့် Engine)

Dataset အသစ်တစ်ခုအတွက် မည်သည့် rule များကို ရေးသားရမည်ကို အတိအကျ မသိသေးပါက:
- AWS Glue Data Quality သည် သင်၏ Glue Data Catalog table ပေါ်တွင် **Recommendation Task** တစ်ခုကို run ပေးနိုင်သည်။
- အဆိုပါ engine သည် ရှိပြီးသား data များကို profile လုပ်ပြီး statistics များ (cardinality, data distributions, distinct values, null counts) ကို ရှာဖွေဖော်ထုတ်ကာ baseline DQDL ruleset တစ်ခုကို အလိုအလျောက် ထုတ်ပေးသည် (generate လုပ်သည်)။
- ထုတ်ပေးထားသော ဤ ruleset ကို သင်ကိုယ်တိုင် စစ်ဆေးကြည့်ရှုခြင်း (inspect)၊ ပြင်ဆင်မွမ်းမံခြင်း (modify) နှင့် အတည်ပြုသိမ်းဆည်းခြင်း (commit) ပြုလုပ်နိုင်သည်။

---

### 3. PySpark Integration (`EvaluateDataQuality` Transform)

Data Quality ကို PySpark ETL script များအတွင်း တိုက်ရိုက် ထည့်သွင်းအသုံးပြုနိုင်သည်:

```python
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsgluedq.transforms import EvaluateDataQuality

glueContext = GlueContext(SparkContext.getOrCreate())

# 1. Read input dataset
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="ecommerce", 
    table_name="orders_raw"
)

# 2. Define DQDL ruleset
dq_ruleset = """
Rules = [
    RowCount > 0,
    IsComplete "order_id",
    IsUnique "order_id",
    Completeness "customer_email" >= 0.95,
    ColumnValues "order_total" > 0
]
"""

# 3. Evaluate Data Quality
dq_results = EvaluateDataQuality.apply(
    frame=datasource,
    ruleset=dq_ruleset,
    publishing_options={
        "dataQualityEvaluationRunId": "run_101",
        "cloudWatchMetricsEnabled": True,
        "resultsS3Prefix": "s3://my-lake/data-quality-results/"
    }
)

# 4. Access evaluation outcomes
rule_outcomes = dq_results.select("ruleOutcomes")
passed_records = dq_results.select("passedRecords")
failed_records = dq_results.select("failedRecords")

# 5. Quarantine failed records to separate S3 prefix
glueContext.write_dynamic_frame.from_options(
    frame=failed_records,
    connection_type="s3",
    connection_options={"path": "s3://my-lake/quarantine/orders/"},
    format="parquet"
)
```

---

### 4. Failure Actions & Pipeline Governance (ကျရှုံးမှုအတွက် လုပ်ဆောင်ချက်များနှင့် Pipeline Governance)

AWS Glue Data Quality သည် enterprise gatekeeper တစ်ခုအဖြစ် လုပ်ဆောင်ပေးပြီး အဓိက failure response ၃ မျိုး ရှိသည်:

1. **Stop Job Execution (Circuit Breaker)**:
   - Glue Studio သို့မဟုတ် PySpark script တွင် configure ပြုလုပ်နိုင်သည်။
   - အရေးကြီးသော data quality rule များ ကျရှုံးပါက၊ Amazon Redshift သို့မဟုတ် S3 ရှိ downstream analytics table များကို ပျက်စီးနေသော ဒေတာများ ညစ်ညမ်းမသွားစေရန် တားဆီးရန်အတွက် job တစ်ခုလုံးသည် failure status ဖြင့် ချက်ချင်း ရပ်တန့်သွားမည် (terminate ဖြစ်မည်)။
2. **Conditional Routing & Quarantining**:
   - Dataset ကို stream နှစ်ခုအဖြစ် ခွဲထုတ်သည်: `passedRecords` နှင့် `failedRecords`။
   - ကောင်းမွန်သော record များကို production table များသို့ ရေးသားပြီး၊ ကျရှုံးသော record များကို လူကိုယ်တိုင် စစ်ဆေးရန် သို့မဟုတ် ပြင်ဆင်ရန်အတွက် S3 "dead-letter" bucket တစ်ခုထဲသို့ quarantine အဖြစ် သီးခြားဖယ်ထုတ်ပေးသည်။
3. **Event-Driven Alerting via CloudWatch & EventBridge**:
   - Metrics များ (ဥပမာ `GlueDataQuality.RulesPassed`, `GlueDataQuality.RulesFailed`) ကို **Amazon CloudWatch** သို့ ပေးပို့ထုတ်ပြန်ပေးသည် (publish လုပ်သည်)။
   - Failure ဖြစ်ပါက **Amazon EventBridge rule** တစ်ခုကို trigger လုပ်ပေးပြီး၊ ၎င်းမှတစ်ဆင့် **Amazon SNS** မှ data engineering team သို့ alert ပေးပို့ခြင်း သို့မဟုတ် ပြင်ဆင်ဖြေရှင်းမည့် **AWS Lambda** function ကို ခေါ်ယူစေခြင်း (invoke) ပြုလုပ်နိုင်သည်။

---

## 3. DEA-C01 Exam Tips & Scenarios (စာမေးပွဲ အကြံပြုချက်များနှင့် အခြေအနေများ)

> [!IMPORTANT]
> **Key Exam Decision Triggers for Glue Data Quality**:
>
> - **"Validate data quality in a serverless pipeline using declarative rules without writing custom Spark validation code"** $\rightarrow$ **AWS Glue Data Quality (DQDL)** ကို အသုံးပြုပါ။
> - **"Halt an ETL job immediately if more than 5% of customer email addresses are null"** $\rightarrow$ DQDL rule ဖြစ်သော `Completeness "customer_email" >= 0.95` ကို configure လုပ်ပြီး action အား **fail the job** အဖြစ် သတ်မှတ်ပါ။
> - **"Separate bad records from good records, writing clean data to Redshift and invalid data to an S3 quarantine bucket"** $\rightarrow$ **AWS Glue Data Quality dataset splitting (`passedRecords` vs. `failedRecords`)** ကို အသုံးပြုပါ။
> - **"Automatically generate data quality rules for an existing S3 table in the Data Catalog"** $\rightarrow$ **Glue Data Quality Recommendation Engine** ကို run ပါ။
> - **"Monitor data quality trends over time across all Data Catalog tables"** $\rightarrow$ **Data Quality evaluations at rest** ကို schedule ဆွဲပြီး metrics များကို **Amazon CloudWatch** သို့ ပေးပို့ထုတ်ပြန်ပါ။

---

## 📌 Related Notes (ဆက်စပ် မှတ်စုများ)
- `[[glue]]` — AWS Glue Architecture & Overview
- `[[glue-etl-jobs]]` — Embedding Data Quality in PySpark Jobs
- `[[glue-studio]]` — Visual Data Quality Nodes in Studio
- `[[data-validation-and-profiling]]` — Concept: Data Validation vs. Profiling
