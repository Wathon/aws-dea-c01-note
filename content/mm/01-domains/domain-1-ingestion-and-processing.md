---
title: "Domain 1: Data Ingestion and Processing (မြန်မာဘာသာ)"
type: domain
tags:
  - domain/ingestion
  - dea-c01
  - exam-prep
  - burmese
date: 2026-07-28
---

# 📥 Domain 1: Data Ingestion and Processing (Weight: 28%)

- **Domain ID**: Domain 1
- **Language / ဘာသာစကား**: [English (Original)](/en/01-domains/domain-1-ingestion-and-processing) | **မြန်မာဘာသာ (Burmese)**
- **Focus**: Batch နှင့် Streaming data ingestion pipelines များ၊ ETL processing workflows များကို ဒီဇိုင်းရေးဆွဲခြင်း၊ အကောင်အထည်ဖော်ခြင်းနှင့် optimize ပြုလုပ်ခြင်း။
- **Hub Links**: [[mm/index|index]] | [[mm/00-hub/dea-c01-roadmap|dea-c01-roadmap]] | [[mm/00-hub/service-catalog|service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 1.1: Design and implement data ingestion solutions
- **Batch & External Data Ingestion**:
  - Database များမှ [[mm/02-services/migration/dms-and-sct|dms-and-sct]] သို့မဟုတ် [[mm/02-services/analytics-streaming/glue/glue|glue]] JDBC connections များကို အသုံးပြု၍ သတ်မှတ်ချိန်အလိုက် batch extraction (Scheduled batch extraction) ပြုလုပ်ခြင်း။
  - [[mm/02-services/migration/datasync-and-snow|datasync-and-snow]] (DataSync, Snowball Edge) ကို အသုံးပြု၍ ပမာဏကြီးမားသော Data transfer (Large-scale file transfer) ပြုလုပ်ခြင်း။
  - [[mm/02-services/migration/data-exchange|data-exchange]] (S3 exports, Redshift data sharing, REST APIs) ကို အသုံးပြု၍ ပြင်ပ commercial third-party datasets များကို ရယူအသုံးပြုခြင်း။
  - [[mm/02-services/migration/transfer-family|transfer-family]] (SFTP, FTPS, FTP, AS2) မှတစ်ဆင့် B2B partner ဖိုင်လွှဲပြောင်းမှုများကို စီမံခန့်ခွဲခြင်း (Managed B2B partner file transfers)။
  - [[mm/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] (Application Discovery Service & MGN) မှတစ်ဆင့် On-premises discovery နှင့် server rehosting ပြုလုပ်ခြင်း။
- **Streaming Ingestion**:
  - [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Streams, Kinesis Data Firehose) ကို အသုံးပြု၍ Real-time streaming ingestion ပြုလုပ်ခြင်း။
  - [[mm/02-services/analytics-streaming/msk/msk|msk]] (Amazon MSK & MSK Connect) ကို အသုံးပြု၍ Managed Apache Kafka စနစ် လည်ပတ်ခြင်း။
  - [[mm/02-services/integration/appflow/appflow|appflow]] (Salesforce, ServiceNow, Slack) ကို အသုံးပြု၍ SaaS application များမှ ဒေတာများကို ရယူခြင်း (SaaS application ingestion)။

### Task Statement 1.2: Transform and process data
- **ETL/ELT Engine Selection**:
  - [[mm/02-services/analytics-streaming/glue/glue|glue]] ETL jobs (PySpark, Scala) နှင့် [[mm/02-services/analytics-streaming/glue/glue|glue]] DataBrew တို့ကို အသုံးပြု၍ Serverless Spark processing ဆောင်ရွက်ခြင်း။
  - [[mm/02-services/analytics-streaming/emr/emr|emr]] (Spark, Hive, Presto, EMR Serverless, EMR on EKS) ကို အသုံးပြု၍ Distributed cluster processing ပြုလုပ်ခြင်း။
  - [[mm/02-services/compute-containers/lambda|lambda]] (< 15 mins) ကို အသုံးပြု၍ ပေါ့ပါးသော Event-driven transformations (Light event-driven transformations) များ ဆောင်ရွက်ခြင်း။
  - [[mm/02-services/compute-containers/batch|batch]] (Spot allocation, Docker images) ကို အသုံးပြု၍ Containerized batch compute နှင့် non-Spark workloads များကို လုပ်ဆောင်ခြင်း။
  - [[mm/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] (ECS Fargate, EKS) ကို အသုံးပြု၍ Container microservices များနှင့် Kubernetes pipelines များ လည်ပတ်ခြင်း။
  - [[mm/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]] ကို အသုံးပြု၍ Spot Instance topologies များနှင့် Graviton price-performance optimization ပြုလုပ်ခြင်း။
- **Data Transformation Practices**:
  - Raw formats (CSV, JSON) များကို စွမ်းဆောင်ရည်မြင့် columnar formats များသို့ ပြောင်းလဲခြင်း ([[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]] — Parquet, ORC)။
  - Query performance ကောင်းမွန်စေရန် Partition schemes များ ([[mm/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]]) ကို အသုံးချခြင်း။

### Task Statement 1.3: Orchestrate data processing workflows
- **State Machine Orchestration**:
  - [[mm/02-services/integration/step-functions/step-functions|step-functions]] (Standard vs Express Workflows) ကို အသုံးပြု၍ ရှုပ်ထွေးသော အဆင့်များစွာပါဝင်သည့် multi-step workflows များကို စီမံခန့်ခွဲခြင်း။
- **DAG Workflow Orchestration**:
  - [[mm/02-services/integration/mwaa-airflow|mwaa-airflow]] (DAGs, Operators, Sensors) ပေါ်ရှိ Apache Airflow ကို အသုံးပြု၍ Programmatic workflow management ဆောင်ရွက်ခြင်း။

---

## 🛠️ Essential AWS Services in Domain 1

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS Glue** | Serverless ETL & Crawlers | S3 ရှိ ဒေတာများကို Parquet သို့ ပြောင်းလဲခြင်း၊ Schema များကို အလိုအလျောက် catalog ပြုလုပ်ခြင်း | [[mm/02-services/analytics-streaming/glue/glue|glue]] |
| **Amazon Kinesis** | Streaming Ingestion | S3/Redshift/OpenSearch သို့ Near real-time ingestion ပြုလုပ်ခြင်း | [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]] |
| **Amazon MSK** | Apache Kafka | Latency နည်းပါးသော Open-source streaming compatibility ပံ့ပိုးပေးခြင်း | [[mm/02-services/analytics-streaming/msk/msk|msk]] |
| **AWS Lambda** | Event-Driven Compute | Micro-batch processing ပြုလုပ်ခြင်း၊ S3 မှ file upload triggers များကို ကိုင်တွယ်ခြင်း | [[mm/02-services/compute-containers/lambda|lambda]] |
| **AWS Batch** | Containerized Batch Compute | Non-Spark batch processing (> 15 mins) လုပ်ဆောင်ခြင်း၊ Spot array jobs များ run ခြင်း | [[mm/02-services/compute-containers/batch|batch]] |
| **Amazon ECR, ECS & EKS** | Container Orchestration | Docker registries၊ Fargate serverless containers၊ EMR on EKS | [[mm/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] |
| **Amazon EC2 & Graviton** | Big Data Compute Infrastructure | Spot checkpointing၊ EMR node mapping၊ Graviton Arm pricing | [[mm/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]] |
| **AWS Step Functions** | Workflow Orchestration | Error handling ပါဝင်သော ETL pipelines များအတွက် Visual state machine | [[mm/02-services/integration/step-functions/step-functions|step-functions]] |
| **Amazon MWAA** | Airflow DAG Orchestration | Python ဖြင့် သတ်မှတ်ထားသော ရှုပ်ထွေးသည့် dependency workflows များ စီမံခြင်း | [[mm/02-services/integration/mwaa-airflow|mwaa-airflow]] |
| **AWS AppFlow** | SaaS Integration | Salesforce, ServiceNow တို့မှ S3/Redshift သို့ ဒေတာများကို လုံခြုံစွာ စီးဆင်းစေခြင်း | [[mm/02-services/integration/appflow/appflow|appflow]] |
| **AWS DMS & SCT** | Database Migration & CDC | S3/Redshift အတွင်းသို့ Heterogeneous/homogeneous DB replication ပြုလုပ်ခြင်း | [[mm/02-services/migration/dms-and-sct|dms-and-sct]] |
| **AWS DataSync & Snow** | File Transfer & Edge Devices | မြန်နှုန်းမြင့် ကွန်ရက်ဒေတာ လွှဲပြောင်းခြင်းနှင့် offline multi-TB/PB migration | [[mm/02-services/migration/datasync-and-snow|datasync-and-snow]] |
| **AWS Data Exchange** | 3rd-Party Data Marketplace | S3 export၊ Redshift zero-ETL querying၊ managed APIs များ အသုံးပြုခြင်း | [[mm/02-services/migration/data-exchange|data-exchange]] |
| **AWS Transfer Family** | Managed SFTP/FTPS | B2B vendor file exchange ကို S3 နှင့် EFS အတွင်းသို့ တိုက်ရိုက် ပြုလုပ်ခြင်း | [[mm/02-services/migration/transfer-family|transfer-family]] |
| **Application Discovery & MGN** | Discovery & Server Rehost | Migration waves များ စီစဉ်ခြင်းနှင့် automated block-level server rehosting ပြုလုပ်ခြင်း | [[mm/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 1

> [!IMPORTANT]
> **Stream vs Batch ရွေးချယ်မှု (Stream vs Batch Selection)**:
> - လိုအပ်ချက်မှာ **custom transformation logic ပါဝင်ပြီး retention ရက်ပေါင်း ၃၆၅ ရက်အထိ ထားရှိနိုင်သော real-time ingestion** ဖြစ်ပါက: [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Streams) ကို ရွေးချယ်ပါ။
> - လိုအပ်ချက်မှာ **micro-batching ဖြင့် S3, Redshift သို့မဟုတ် OpenSearch သို့ တိုက်ရိုက် zero-code streaming** ဖြစ်ပါက: [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Firehose) ကို ရွေးချယ်ပါ။
> - လိုအပ်ချက်မှာ **open-source Kafka ecosystem / custom producers** ဖြစ်ပါက: [[mm/02-services/analytics-streaming/msk/msk|msk]] ကို ရွေးချယ်ပါ။

> [!TIP]
> **Glue vs EMR ရွေးချယ်မှု (Glue vs EMR Selection)**:
> - **Serverless ETL၊ AWS-native catalog integration၊ dynamic frames များနှင့် infrastructure management အနည်းဆုံးဖြစ်စေရန်** လိုအပ်ပါက: [[mm/02-services/analytics-streaming/glue/glue|glue]] ကို ရွေးချယ်ပါ။
> - **Custom open-source Spark/Hadoop libraries များ လိုအပ်ခြင်း၊ cluster tuning ကို အသေးစိတ် စိတ်ကြိုက်ပြင်ဆင်လိုခြင်း၊ ကြာရှည်စွာ run သည့် cluster efficiency လိုအပ်ခြင်း သို့မဟုတ် EMR Serverless အသုံးပြုလိုပါက**: [[mm/02-services/analytics-streaming/emr/emr|emr]] ကို ရွေးချယ်ပါ။

---

## 📌 Checklist for Domain 1
- [ ] [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf) ရှိ slide စာမျက်နှာများဖြစ်သော 266-312 (Migration & Compute) နှင့် 331-459 (Analytics & Streaming) ကို ပြန်လည်လေ့လာရန်
- [ ] Service notes များကို အပြီးသတ်လေ့လာရန်: [[mm/02-services/analytics-streaming/glue/glue|glue]], [[mm/02-services/analytics-streaming/kinesis/kinesis|kinesis]], [[mm/02-services/compute-containers/lambda|lambda]], [[mm/02-services/integration/step-functions/step-functions|step-functions]], [[mm/02-services/integration/mwaa-airflow|mwaa-airflow]]
- [ ] Data formats များကို ပြန်လည်သုံးသပ်ရန်: [[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]]
