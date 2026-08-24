---
title: AWS Glue Data Quality
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - data-quality
  - governance
date: 2026-08-17
---

# ✅ AWS Glue Data Quality

- **Category**: Analytics / Data Governance & Validation
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/glue/glue-data-quality)
- **Primary Use Case**: Automated data quality measurement, declarative DQDL rule validation, circuit breaking bad pipelines, and quarantining invalid records.
- **Slide Reference**: Pages 331–364 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[en/index|index]]` | `[[en/02-services/analytics-streaming/glue/glue|glue]]` | `[[en/02-services/analytics-streaming/glue/glue-etl-jobs|glue-etl-jobs]]` | `[[en/03-concepts/data-validation-and-profiling|data-validation-and-profiling]]`

---

## 1. High-Level Summary

**AWS Glue Data Quality** is a serverless, declarative data quality measurement and validation engine. Instead of requiring data engineers to write hundreds of lines of complex, custom PySpark unit-testing logic to assert dataset validity, AWS Glue Data Quality uses **DQDL (Data Quality Definition Language)**.

It can evaluate data quality across two distinct operational modes:
1. **Data at Rest**: Scheduled or on-demand evaluations run directly against tables in the **[[en/02-services/analytics-streaming/glue/glue-data-catalog|glue-data-catalog]]**.
2. **Data in Transit**: Real-time evaluation nodes embedded inside **[[en/02-services/analytics-streaming/glue/glue-etl-jobs|glue-etl-jobs]]** or Glue Studio pipelines.

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

## 2. Core Technical Capabilities

### 1. Data Quality Definition Language (DQDL)

DQDL is a human-readable, domain-specific language used to express data quality assertions. You group assertions into a **Ruleset**.

#### Complete DQDL Rule Syntax Examples:
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

### 2. Automatic Rule Recommendation Engine

If you do not know the exact rules to write for a new dataset:
- AWS Glue Data Quality can run a **Recommendation Task** against your Glue Data Catalog table.
- The engine profiles the existing data, discovers statistics (cardinality, data distributions, distinct values, null counts), and automatically generates a baseline DQDL ruleset.
- You can inspect, modify, and commit this generated ruleset.

---

### 3. PySpark Integration (`EvaluateDataQuality` Transform)

You can embed Data Quality directly into PySpark ETL scripts:

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

### 4. Failure Actions & Pipeline Governance

AWS Glue Data Quality acts as an enterprise gatekeeper with three primary failure responses:

1. **Stop Job Execution (Circuit Breaker)**:
   - Configured in Glue Studio or PySpark script.
   - If critical data quality rules fail, the entire job terminates immediately with a failure status, preventing corrupted data from contaminating downstream analytics tables in Amazon Redshift or S3.
2. **Conditional Routing & Quarantining**:
   - The dataset is split into two streams: `passedRecords` and `failedRecords`.
   - Good records are written to production tables, while failed records are quarantined in an S3 "dead-letter" bucket for manual inspection or remediation.
3. **Event-Driven Alerting via CloudWatch & EventBridge**:
   - Publishes metrics (e.g., `GlueDataQuality.RulesPassed`, `GlueDataQuality.RulesFailed`) to **Amazon CloudWatch**.
   - Triggers an **Amazon EventBridge rule** on failure, which sends an alert via **Amazon SNS** to the data engineering team or invokes an **AWS Lambda** remediation function.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Decision Triggers for Glue Data Quality**:
>
> - **"Validate data quality in a serverless pipeline using declarative rules without writing custom Spark validation code"** $\rightarrow$ **AWS Glue Data Quality (DQDL)**.
> - **"Halt an ETL job immediately if more than 5% of customer email addresses are null"** $\rightarrow$ Configure a DQDL rule: `Completeness "customer_email" >= 0.95` and set the action to **fail the job**.
> - **"Separate bad records from good records, writing clean data to Redshift and invalid data to an S3 quarantine bucket"** $\rightarrow$ Use **AWS Glue Data Quality dataset splitting (`passedRecords` vs. `failedRecords`)**.
> - **"Automatically generate data quality rules for an existing S3 table in the Data Catalog"** $\rightarrow$ Run the **Glue Data Quality Recommendation Engine**.
> - **"Monitor data quality trends over time across all Data Catalog tables"** $\rightarrow$ Schedule **Data Quality evaluations at rest** and publish metrics to **Amazon CloudWatch**.

---

## 📌 Related Notes
- `[[en/02-services/analytics-streaming/glue/glue|glue]]` — AWS Glue Architecture & Overview
- `[[en/02-services/analytics-streaming/glue/glue-etl-jobs|glue-etl-jobs]]` — Embedding Data Quality in PySpark Jobs
- `[[en/02-services/analytics-streaming/glue/glue-studio|glue-studio]]` — Visual Data Quality Nodes in Studio
- `[[en/03-concepts/data-validation-and-profiling|data-validation-and-profiling]]` — Concept: Data Validation vs. Profiling
