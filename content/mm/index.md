---
title: AWS DEA-C01 မြန်မာဘာသာ လေ့လာရေးဗဟို (Knowledge Hub)
type: hub
tags:
  - hub
  - dea-c01
  - burmese
date: 2026-08-24
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) မြန်မာဘာသာ လေ့လာရေးဗဟို

- **Language / ဘာသာစကား**: [English (Original)](/en/index) | **မြန်မာဘာသာ (Burmese)**
- **မူရင်းသင်ရိုး Slides**: [AWSCertifiedDataEngineerSlides.pdf](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/docs/AWSCertifiedDataEngineerSlides.pdf)
- **လက်တွေ့ Lab ကုဒ်များနှင့် Datasets များ**: [Materials Directory](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/materials) | [[mm/00-hub/lab-materials-index|lab-materials-index]]
- **လေ့လာမှု မှတ်တမ်း (Journal)**: [[journal/2026-07-28]]

---

## 🗺️ Master Navigation (ပင်မလမ်းညွှန်)

### 📌 Exam Roadmap & Catalog (စာမေးပွဲ လမ်းပြမြေပုံနှင့် ဝန်ဆောင်မှုလမ်းညွှန်)

- [[mm/00-hub/dea-c01-roadmap|dea-c01-roadmap]] — စာမေးပွဲ Domain ၄ ခု ခွဲခြမ်းစိတ်ဖြာမှု၊ ရမှတ်အလေးချိန်နှင့် လေ့လာမှု နည်းဗျူဟာ
- [[mm/00-hub/service-catalog|service-catalog]] — သင်ရိုးတွင် ပါဝင်သော AWS Services အားလုံး၏ စာရင်း
- [[mm/00-hub/lab-materials-index|lab-materials-index]] — လက်တွေ့ Lab ကုဒ်များ၊ CLI scripts များနှင့် နမူနာ Datasets များ (`content/materials/`)

---

### 🎯 DEA-C01 စာမေးပွဲ Domain များ (Official Outline)

1. [[mm/01-domains/domain-1-ingestion-and-processing|Domain 1: Data Ingestion and Processing]] _(28% Weight)_ — Batch & Streaming Ingestion၊ ETL Pipelines နှင့် Workflow Orchestration
2. [[mm/01-domains/domain-2-data-store-management|Domain 2: Data Store Management]] _(26% Weight)_ — Storage Systems ရွေးချယ်မှု၊ Schema Design၊ Lifecycle နှင့် Data Warehousing
3. [[mm/01-domains/domain-3-data-operations-and-support|Domain 3: Data Operations and Support]] _(22% Weight)_ — Pipeline Automation၊ CloudWatch Monitoring၊ Error Handling နှင့် Glue Data Quality
4. [[mm/01-domains/domain-4-data-security-and-governance|Domain 4: Data Security and Governance]] _(24% Weight)_ — IAM Access Control၊ KMS Encryption၊ Lake Formation၊ PII Masking နှင့် Macie

---

### 💡 Exam Tips & Decision Matrices (စာမေးပွဲ အကြံပြုချက်များနှင့် နှိုင်းယှဉ်ချက်များ)

- [[mm/04-exam-tips/service-comparisons|Service Comparisons & Decision Matrix]] — Storage, Ingestion, Query Engine, Security နှိုင်းယှဉ်ချက် ဇယားများ
- [[mm/04-exam-tips/high-frequency-exam-patterns|High-Frequency Exam Scenarios & Traps]] — စာမေးပွဲတွင် အမေးအများဆုံး မေးခွန်းပုံစံများနှင့် Traps များ

---

## 📘 အခြေခံ သဘောတရားများ (Fundamental Concepts)

- [[mm/03-concepts/big-data-fundamentals|Big Data Fundamentals]] — Big Data ၏ 5 V's၊ Data Lake vs Data Warehouse vs Data Swamp နှင့် Medallion Architecture
- [[mm/03-concepts/data-formats-and-compression|Data Formats & Compression]] — Row-based vs Columnar (Parquet/ORC)၊ Splittability နှင့် Compression စနစ်များ (Snappy, Gzip, Zstd)
- [[mm/03-concepts/data-modeling-and-partitioning|Data Modeling & Partitioning]] — Star Schema vs Snowflake Schema၊ S3 Partitioning နှင့် Partition Pruning
- [[mm/03-concepts/data-validation-and-profiling|Data Validation & Profiling]] — Data Profiling vs Validation၊ AWS Glue Data Quality (DQDL) နှင့် Quarantine စနစ်များ
- [[mm/03-concepts/sql-and-version-control-review|SQL & Version Control Review]] — SQL Window Functions၊ Join Matrix နှင့် Git CI/CD စနစ်များ

---

## ☁️ မြန်မာဘာသာ ပြန်ဆိုထားသော AWS Services မှတ်စုများ

### 📦 Storage (သိုလှောင်မှု စနစ်များ)
- [[mm/02-services/storage/s3/s3|Amazon S3 Overview]] — S3 Object Storage & Storage Classes Matrix
- [[mm/02-services/storage/s3/s3-performance|S3 Performance]] — Prefix Partitioning limits, Multipart upload & Byte-Range Fetches
- [[mm/02-services/storage/s3/s3-lifecycle-rules|S3 Lifecycle Rules]] — Automated Tiering transitions & Abort Incomplete Multipart Uploads
- [[mm/02-services/storage/s3/s3-replication|S3 Replication]] — Cross-Region (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- [[mm/02-services/storage/s3/s3-versioning|S3 Versioning]] — Object versions, Delete Markers & MFA Delete
- [[mm/02-services/storage/s3/s3-security|S3 Security]] — Bucket Policies, Block Public Access & Object Lock WORM (Compliance mode)
- [[mm/02-services/storage/s3/s3-encryption|S3 Encryption]] — SSE-S3, SSE-KMS, DSSE-KMS, SSE-C & S3 Bucket Keys
- [[mm/02-services/storage/s3/s3-access-points|S3 Access Points]] — Multi-tenant access points & S3 Object Lambda PII masking
- [[mm/02-services/storage/s3/s3-tables|S3 Tables]] — Apache Iceberg purpose-built storage with automated file compaction
- [[mm/02-services/storage/s3/s3-storage-lens|S3 Storage Lens]] — Organization-wide storage analytics & Parquet exports
- [[mm/02-services/storage/ebs-and-instance-store|Amazon EBS & Instance Store]] — Persistent block storage vs Ephemeral NVMe
- [[mm/02-services/storage/efs-and-fsx|Amazon EFS & AWS FSx]] — POSIX Shared File systems & FSx for Lustre S3 data sync
- [[mm/02-services/storage/ebs-vs-efs-vs-instance-store|EBS vs. EFS vs. Instance Store]] — Decision Matrix & Trade-offs

### 🗄️ Database (ဒေတာဘေ့စ်နှင့် Data Warehousing)
- [[mm/02-services/database/redshift|Amazon Redshift]] — Petabyte-scale Columnar OLAP Data Warehouse, DISTSTYLE, SORTKEY, `COPY`, & Spectrum
- [[mm/02-services/database/dynamodb|Amazon DynamoDB]] — Serverless NoSQL Key-Value store, LSI vs GSI, Streams (CDC), & S3 PITR Export
- [[mm/02-services/database/rds-and-aurora|Amazon RDS & Aurora]] — Relational OLTP, Multi-AZ vs Read Replicas, & Redshift Zero-ETL
- [[mm/02-services/database/nosql-specialized-databases|Specialized Databases]] — ElastiCache, MemoryDB, Keyspaces, Neptune, & Timestream

### 🔄 Migration & Transfer (ဒေတာ ရွှေ့ပြောင်းခြင်းနှင့် လွှဲပြောင်းခြင်း)
- [[mm/02-services/migration/dms-and-sct|AWS DMS & AWS SCT]] — Database Migration Service, Schema Conversion Tool, & Continuous CDC
- [[mm/02-services/migration/datasync-and-snow|AWS DataSync & Snow Family]] — Online high-speed network sync vs Snowball Edge / Snowmobile
- [[mm/02-services/migration/transfer-family|AWS Transfer Family]] — Managed SFTP, FTPS, FTP, & AS2 directly to S3 / EFS
- [[mm/02-services/migration/data-exchange|AWS Data Exchange]] — Third-party commercial dataset subscriptions & Redshift Data Sharing
- [[mm/02-services/migration/application-discovery-and-mgn|Application Discovery & MGN]] — Server discovery and automated Lift-and-Shift rehosting

### ⚡ Compute & Containers (တွက်ချက်မှုနှင့် ကွန်တိန်နာများ)
- [[mm/02-services/compute-containers/lambda|AWS Lambda]] — Serverless event-driven compute, stream batching tuning, & `/tmp` / EFS storage
- [[mm/02-services/compute-containers/batch|AWS Batch]] — Managed containerized batch processing, Spot instances, & Array jobs
- [[mm/02-services/compute-containers/ec2-and-graviton|EC2 & AWS Graviton]] — Spot instance strategies, EMR node mapping, & Arm price-performance
- [[mm/02-services/compute-containers/ecr-ecs-eks|Amazon ECR, ECS & EKS]] — Container registries, ECS Fargate, & Amazon EMR on EKS Spark

### 📊 Analytics & Data Pipelines (ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် ပိုက်လိုင်းများ)
- [[mm/02-services/analytics-streaming/glue/glue|AWS Glue Overview]] — Serverless Data Integration & ETL အကျဉ်းချုပ်
- [[mm/02-services/analytics-streaming/glue/glue-data-catalog|AWS Glue Data Catalog]] — S3, Athena, EMR အတွက် ဗဟို Metadata သိုလှောင်မှု
- [[mm/02-services/analytics-streaming/glue/glue-crawlers|AWS Glue Crawlers]] — ဒေတာ Format, Schema နှင့် Partition များကို အလိုအလျောက် ရှာဖွေခြင်း
- [[mm/02-services/analytics-streaming/glue/glue-etl-jobs|AWS Glue ETL Jobs]] — Serverless PySpark, DynamicFrames နှင့် Incremental Processing (Bookmarks)
- [[mm/02-services/analytics-streaming/glue/glue-flex|AWS Glue Flex]] — ကုန်ကျစရိတ် သက်သာသော Execution Class
- [[mm/02-services/analytics-streaming/glue/glue-studio|AWS Glue Studio]] — Code ရေးစရာမလိုဘဲ UI မှတစ်ဆင့် Visual ETL တည်ဆောက်ခြင်း
- [[mm/02-services/analytics-streaming/glue/glue-workflows|AWS Glue Workflows]] — ETL အဆင့်များကို ချိတ်ဆက်ခြင်း (Orchestration)
- [[mm/02-services/analytics-streaming/glue/glue-data-quality|AWS Glue Data Quality]] — DQDL rules များဖြင့် ဒေတာမှန်ကန်မှုကို အလိုအလျောက် စစ်ဆေးခြင်း
- [[mm/02-services/analytics-streaming/glue/glue-schema-registry|AWS Glue Schema Registry]] — Streaming ဒေတာများ၏ Schema ကို ထိန်းချုပ်ခြင်း
- [[mm/02-services/analytics-streaming/glue/glue-databrew|AWS Glue DataBrew]] — Code ရေးစရာမလိုဘဲ UI မှတစ်ဆင့် Data Preparation ပြုလုပ်ခြင်း
- [[mm/02-services/analytics-streaming/athena/athena|Amazon Athena]] — Serverless SQL queries on S3, Partition Projection, CTAS, Federated Queries
- [[mm/02-services/analytics-streaming/emr/emr|Amazon EMR]] — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- [[mm/02-services/analytics-streaming/kinesis/kinesis|Amazon Kinesis]] — Kinesis Data Streams, Firehose, Data Analytics (Flink), Video Streams
- [[mm/02-services/analytics-streaming/msk/msk|Amazon MSK]] — Managed Streaming for Apache Kafka, MSK Connect
- [[mm/02-services/analytics-streaming/opensearch/opensearch|Amazon OpenSearch]] — OpenSearch Service, Search indices, Shards & Serverless
- [[mm/02-services/analytics-streaming/quicksight/quicksight|Amazon QuickSight]] — Business Intelligence, SPICE engine, Dashboards, RLS

### 🔀 Application Integration & Workflow Automation
- [[mm/02-services/integration/step-functions/step-functions|AWS Step Functions]] — Orchestrating state machines (Standard vs Express workflows)
- [[mm/02-services/integration/sqs/sqs|Amazon SQS]] — Simple Queue Service (Standard/FIFO, Timing, DLQ, Fan-Out & Security)
- [[mm/02-services/integration/sns/sns|Amazon SNS]] — Simple Notification Service (Topics, Filter Policies, Delivery Retries & Firehose)
- [[mm/02-services/integration/appflow/appflow|Amazon AppFlow]] — SaaS & AWS integration (Salesforce, ServiceNow, S3)

### 🔒 Security, Identity & Governance
- [[mm/02-services/security-governance/lake-formation|AWS Lake Formation]] — Data Lake Governance, Column/Row-level security, LF-TBAC
- [[mm/02-services/security-governance/iam|AWS IAM]] — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- [[mm/02-services/security-governance/kms-and-secrets|AWS KMS & Secrets Manager]] — KMS SSE-S3/SSE-KMS/SSE-C, Secrets Manager, Parameter Store
- [[mm/02-services/security-governance/macie|Amazon Macie Deep Dive]] — ML-powered PII scanning, Managed & Custom Data Identifiers
- [[mm/02-services/security-governance/macie-and-cloudtrail|Amazon Macie & CloudTrail]] — PII scanning with Macie & CloudTrail audit logs
- [[mm/02-services/security-governance/data-masking-anonymization-and-salting|Data Masking & Salting]] — Redshift DDM, Glue Sensitive Data, Tokenization & Key Salting
- [[mm/02-services/security-governance/aws-backup|AWS Backup]] — Centralized Cross-Service Backup, Vault Lock WORM & Cross-Account DR

### 🌐 Networking & Monitoring
- [[mm/02-services/networking-monitoring/vpc-and-networking|Amazon VPC & Networking]] — VPC, Subnets, Security Groups, Endpoints
- [[mm/02-services/networking-monitoring/waf-and-shield|AWS WAF & AWS Shield]] — Web ACLs, Managed Rules, Rate-Based Rules, DDoS Mitigation
- [[mm/02-services/networking-monitoring/cloudwatch-and-eventbridge|CloudWatch & EventBridge]] — Metrics, Logs Insights, EventBridge rules

---

## 🏷️ Tags

`#dea-c01` `#aws/service` `#burmese` `#concept/data-engineering` `#storage` `#database` `#migration` `#compute` `#exam-tip`
