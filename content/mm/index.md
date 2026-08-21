---
title: AWS DEA-C01 မြန်မာဘာသာ လေ့လာရေးဗဟို (Knowledge Hub)
type: hub
tags:
  - hub
  - dea-c01
  - burmese
date: 2026-08-15
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) မြန်မာဘာသာ လေ့လာရေးဗဟို

- **Language / ဘာသာစကား**: [English (Original)](/en/index) | **မြန်မာဘာသာ (Burmese)**
- **မူရင်းသင်ရိုး Slides**: [AWSCertifiedDataEngineerSlides.pdf](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/docs/AWSCertifiedDataEngineerSlides.pdf)
- **လက်တွေ့ Lab ကုဒ်များနှင့် Datasets များ**: [Materials Directory](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/materials)
- **လေ့လာမှု မှတ်တမ်း (Journal)**: [[journal/2026-07-28]]

---

## 📘 အခြေခံ သဘောတရားများ (Fundamental Concepts)

- `[[mm/03-concepts/big-data-fundamentals|big-data-fundamentals]]` — Big Data ၏ 5 V's၊ Data Lake vs Data Warehouse vs Data Swamp နှင့် Medallion Architecture
- `[[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]]` — Row-based vs Columnar (Parquet/ORC)၊ Splittability နှင့် Compression စနစ်များ (Snappy, Gzip, Zstd)
- `[[mm/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]]` — Star Schema vs Snowflake Schema၊ S3 Partitioning နှင့် Partition Pruning
- `[[mm/03-concepts/data-validation-and-profiling|data-validation-and-profiling]]` — Data Profiling vs Validation၊ AWS Glue Data Quality (DQDL) နှင့် Quarantine စနစ်များ
- `[[mm/03-concepts/sql-and-version-control-review|sql-and-version-control-review]]` — SQL Window Functions၊ Join Matrix နှင့် Git CI/CD စနစ်များ

---

## ☁️ မြန်မာဘာသာ ပြန်ဆိုထားသော AWS Services မှတ်စုများ

### 📦 Storage (သိုလှောင်မှု စနစ်များ)
- `[[mm/02-services/storage/s3/s3|Amazon S3 Overview]]` — S3 Object Storage & Storage Classes Matrix
- `[[mm/02-services/storage/s3/s3-performance|S3 Performance]]` — Prefix Partitioning limits, Multipart upload & Byte-Range Fetches
- `[[mm/02-services/storage/s3/s3-lifecycle-rules|S3 Lifecycle Rules]]` — Automated Tiering transitions & Abort Incomplete Multipart Uploads
- `[[mm/02-services/storage/s3/s3-replication|S3 Replication]]` — Cross-Region (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- `[[mm/02-services/storage/s3/s3-versioning|S3 Versioning]]` — Object versions, Delete Markers & MFA Delete
- `[[mm/02-services/storage/s3/s3-security|S3 Security]]` — Bucket Policies, Block Public Access & Object Lock WORM (Compliance mode)
- `[[mm/02-services/storage/s3/s3-encryption|S3 Encryption]]` — SSE-S3, SSE-KMS, DSSE-KMS, SSE-C & S3 Bucket Keys
- `[[mm/02-services/storage/s3/s3-access-points|S3 Access Points]]` — Multi-tenant access points & S3 Object Lambda PII masking
- `[[mm/02-services/storage/s3/s3-tables|S3 Tables]]` — Apache Iceberg purpose-built storage with automated file compaction
- `[[mm/02-services/storage/s3/s3-storage-lens|S3 Storage Lens]]` — Organization-wide storage analytics & Parquet exports
- `[[mm/02-services/storage/ebs-and-instance-store|Amazon EBS & Instance Store]]` — Persistent block storage vs Ephemeral NVMe
- `[[mm/02-services/storage/efs-and-fsx|Amazon EFS & AWS FSx]]` — POSIX Shared File systems & FSx for Lustre S3 data sync
- `[[mm/02-services/storage/ebs-vs-efs-vs-instance-store|EBS vs. EFS vs. Instance Store]]` — Decision Matrix & Trade-offs

### 🗄️ Database (ဒေတာဘေ့စ်နှင့် Data Warehousing)
- `[[mm/02-services/database/redshift|Amazon Redshift]]` — Petabyte-scale Columnar OLAP Data Warehouse, DISTSTYLE, SORTKEY, `COPY`, & Spectrum
- `[[mm/02-services/database/dynamodb|Amazon DynamoDB]]` — Serverless NoSQL Key-Value store, LSI vs GSI, Streams (CDC), & S3 PITR Export
- `[[mm/02-services/database/rds-and-aurora|Amazon RDS & Aurora]]` — Relational OLTP, Multi-AZ vs Read Replicas, & Redshift Zero-ETL
- `[[mm/02-services/database/nosql-specialized-databases|Specialized Databases]]` — ElastiCache, MemoryDB, Keyspaces, Neptune, & Timestream

### 🔄 Migration & Transfer (ဒေတာ ရွှေ့ပြောင်းခြင်းနှင့် လွှဲပြောင်းခြင်း)
- `[[mm/02-services/migration/dms-and-sct|AWS DMS & AWS SCT]]` — Database Migration Service, Schema Conversion Tool, & Continuous CDC
- `[[mm/02-services/migration/datasync-and-snow|AWS DataSync & Snow Family]]` — Online high-speed network sync vs Snowball Edge / Snowmobile
- `[[mm/02-services/migration/transfer-family|AWS Transfer Family]]` — Managed SFTP, FTPS, FTP, & AS2 directly to S3 / EFS
- `[[mm/02-services/migration/data-exchange|AWS Data Exchange]]` — Third-party commercial dataset subscriptions & Redshift Data Sharing
- `[[mm/02-services/migration/application-discovery-and-mgn|Application Discovery & MGN]]` — Server discovery and automated Lift-and-Shift rehosting

### ⚡ Compute & Containers (တွက်ချက်မှုနှင့် ကွန်တိန်နာများ)
- `[[mm/02-services/compute-containers/lambda|AWS Lambda]]` — Serverless event-driven compute, stream batching tuning, & `/tmp` / EFS storage
- `[[mm/02-services/compute-containers/batch|AWS Batch]]` — Managed containerized batch processing, Spot instances, & Array jobs
- `[[mm/02-services/compute-containers/ec2-and-graviton|EC2 & AWS Graviton]]` — Spot instance strategies, EMR node mapping, & Arm price-performance
- `[[mm/02-services/compute-containers/ecr-ecs-eks|Amazon ECR, ECS & EKS]]` — Container registries, ECS Fargate, & Amazon EMR on EKS Spark

### 📊 Analytics & Data Pipelines (ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် ပိုက်လိုင်းများ)
- `[[mm/02-services/analytics-streaming/glue/glue|AWS Glue Overview]]` — Serverless Data Integration & ETL အကျဉ်းချုပ်
- `[[mm/02-services/analytics-streaming/glue/glue-data-catalog|AWS Glue Data Catalog]]` — S3, Athena, EMR အတွက် ဗဟို Metadata သိုလှောင်မှု
- `[[mm/02-services/analytics-streaming/glue/glue-crawlers|AWS Glue Crawlers]]` — ဒေတာ Format, Schema နှင့် Partition များကို အလိုအလျောက် ရှာဖွေခြင်း
- `[[mm/02-services/analytics-streaming/glue/glue-etl-jobs|AWS Glue ETL Jobs]]` — Serverless PySpark, DynamicFrames နှင့် Incremental Processing (Bookmarks)
- `[[mm/02-services/analytics-streaming/glue/glue-flex|AWS Glue Flex]]` — ကုန်ကျစရိတ် သက်သာသော Execution Class
- `[[mm/02-services/analytics-streaming/glue/glue-studio|AWS Glue Studio]]` — Code ရေးစရာမလိုဘဲ UI မှတစ်ဆင့် Visual ETL တည်ဆောက်ခြင်း
- `[[mm/02-services/analytics-streaming/glue/glue-workflows|AWS Glue Workflows]]` — ETL အဆင့်များကို ချိတ်ဆက်ခြင်း (Orchestration)
- `[[mm/02-services/analytics-streaming/glue/glue-data-quality|AWS Glue Data Quality]]` — DQDL rules များဖြင့် ဒေတာမှန်ကန်မှုကို အလိုအလျောက် စစ်ဆေးခြင်း
- `[[mm/02-services/analytics-streaming/glue/glue-schema-registry|AWS Glue Schema Registry]]` — Streaming ဒေတာများ၏ Schema ကို ထိန်းချုပ်ခြင်း
- `[[mm/02-services/analytics-streaming/glue/glue-databrew|AWS Glue DataBrew]]` — Code ရေးစရာမလိုဘဲ UI မှတစ်ဆင့် Data Preparation ပြုလုပ်ခြင်း
- `[[en/02-services/analytics-streaming/athena|Amazon Athena]]` — Serverless SQL queries on S3, Partition Projection, CTAS
- `[[en/02-services/analytics-streaming/emr|Amazon EMR]]` — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- `[[en/02-services/analytics-streaming/kinesis|Amazon Kinesis]]` — Kinesis Data Streams, Firehose, Data Analytics, Video Streams
- `[[en/02-services/analytics-streaming/msk/msk|Amazon MSK]]` — Managed Streaming for Apache Kafka, MSK Connect
- `[[en/02-services/analytics-streaming/opensearch|Amazon OpenSearch]]` — OpenSearch Service, Search indices, Shards
- `[[en/02-services/analytics-streaming/quicksight|Amazon QuickSight]]` — Business Intelligence, SPICE engine, Dashboards

### 🔀 Application Integration & Workflow Automation
- `[[en/02-services/application-integration/step-functions|AWS Step Functions]]` — Orchestrating state machines (Standard vs Express workflows)
- `[[en/02-services/application-integration/mwaa-airflow|Amazon MWAA (Airflow)]]` — Managed Workflows for Apache Airflow, DAGs & Operators
- `[[mm/02-services/integration/sqs/sqs|Amazon SQS]]` — Simple Queue Service (Standard/FIFO, Timing, DLQ, Fan-Out & Security)
- `[[mm/02-services/integration/sns/sns|Amazon SNS]]` — Simple Notification Service (Topics, Filter Policies, Delivery Retries & Firehose)
- `[[en/02-services/application-integration/sqs-and-sns|Amazon SQS & SNS]]` — Simple Queue Service & Simple Notification Service
- `[[en/02-services/application-integration/appflow|Amazon AppFlow]]` — SaaS & AWS integration (Salesforce, ServiceNow, S3)

### 🔒 Security, Identity & Governance
- `[[en/02-services/security-governance/lake-formation|AWS Lake Formation]]` — Data Lake Governance, Column/Row-level security
- `[[en/02-services/security-governance/iam|AWS IAM]]` — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- `[[en/02-services/security-governance/kms-and-secrets|AWS KMS & Secrets Manager]]` — Encryption, Parameter Store
- `[[en/02-services/security-governance/macie-and-cloudtrail|Amazon Macie & CloudTrail]]` — PII scanning with Macie & CloudTrail audit logs
- `[[en/02-services/security-governance/aws-backup|AWS Backup]]` — Centralized Cross-Service Backup, Vault Lock WORM

### 🌐 Networking & Governance
- `[[en/02-services/networking/vpc-and-networking|Amazon VPC & Networking]]` — VPC, Subnets, Security Groups, Endpoints
- `[[en/02-services/networking/cloudwatch-and-eventbridge|CloudWatch & EventBridge]]` — Metrics, Logs Insights, EventBridge rules

### 🤖 ML, Developer Tools & Cost
- `[[en/02-services/ml-developer-tools/sagemaker-and-ai|Amazon SageMaker & AI]]` — SageMaker Data Wrangler, Feature Store
- `[[en/02-services/ml-developer-tools/cdk-cloudformation|CDK & CloudFormation]]` — Infrastructure as code
- `[[en/02-services/ml-developer-tools/cost-management|AWS Cost Management]]` — Cost Explorer, Budgets, Savings Plans, CUR

---

## 🗺️ အင်္ဂလိပ်ဘာသာ အပြည့်အစုံ မှတ်စုများ (Full English Notes)

- `[[en/index|English Knowledge Hub]]` — အင်္ဂလိပ်ဘာသာဖြင့် ရေးသားထားသော ဝန်ဆောင်မှုအားလုံး၏ အသေးစိတ် မှတ်စုများ။
- `[[dea-c01-roadmap]]` — စာမေးပွဲ အပိုင်း ၄ ပိုင်း အလေးချိန်နှင့် လေ့လာရန် နည်းဗျူဟာများ
- `[[service-catalog]]` — AWS Services အားလုံး၏ စာရင်း
- `[[service-comparisons]]` — ဆာဗစ်များ နှိုင်းယှဉ်ချက် Decision Matrix
- `[[high-frequency-exam-patterns]]` — စာမေးပွဲတွင် အမေးအများဆုံး မေးခွန်းပုံစံများနှင့် Keywords များ

---

## 🏷️ Tags

`#dea-c01` `#aws/service` `#burmese` `#concept/data-engineering` `#storage` `#database` `#migration` `#compute`
