---
title: AWS DEA-C01 မြန်မာဘာသာ ဗဟိုမှတ်စု (Knowledge Hub)
type: hub
tags:
  - hub
  - dea-c01
  - burmese
date: 2026-07-28
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) မြန်မာဘာသာ ဗဟိုမှတ်စု (Knowledge Hub)

- **Language / ဘာသာစကား**: [English (Original)](/en/00-hub/index) | **မြန်မာဘာသာ (Burmese)**
- **Course Slides**: [AWSCertifiedDataEngineerSlides.pdf](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/docs/AWSCertifiedDataEngineerSlides.pdf)
- **Hands-on Labs & Datasets**: [Lab Materials Directory](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/materials) | [[mm/00-hub/lab-materials-index|lab-materials-index]]
- **Study Journal**: [[journal/2026-07-28]]

---

## 🗺️ Master Navigation (ပင်မလမ်းညွှန်)

### 📌 Exam Roadmap & Catalog (စာမေးပွဲ လမ်းပြမြေပုံနှင့် ဝန်ဆောင်မှုလမ်းညွှန်)

- [[mm/00-hub/dea-c01-roadmap|dea-c01-roadmap]] — စာမေးပွဲ Domain များ၊ ရမှတ်အလေးချိန်နှင့် လေ့လာမှု နည်းဗျူဟာ
- [[mm/00-hub/service-catalog|service-catalog]] — သင်ရိုးတွင် ပါဝင်သော AWS Services အားလုံး၏ အညွှန်း
- [[mm/00-hub/lab-materials-index|lab-materials-index]] — လက်တွေ့ Lab ကုဒ်များ၊ CLI scripts များနှင့် နမူနာ Datasets များ (`content/materials/`)

---

### 🎯 DEA-C01 စာမေးပွဲ Domain များ (Official Outline)

1. [[mm/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]] _(28% Weight)_ — Data Ingestion & Transformation Pipelines
2. [[mm/01-domains/domain-2-data-store-management|domain-2-data-store-management]] _(26% Weight)_ — Storage Systems, Schemas, & Data Warehousing
3. [[mm/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]] _(22% Weight)_ — Automation, Monitoring, & Troubleshooting
4. [[mm/01-domains/domain-4-data-security-and-governance|domain-4-data-security-and-governance]] _(24% Weight)_ — Encryption, IAM, Governance & Compliance

---

### ☁️ AWS Services မှတ်စုများ (Slide အခန်းများအလိုက်)

#### 📦 Storage (ဒေတာ သိုလှောင်မှု)

- [[mm/02-services/storage/s3/s3|Amazon S3]] — S3 Storage Classes, Policies, Lifecycle, Object Lock, Replication & Lens
- [[mm/02-services/storage/s3/s3-event-notifications|S3 Event Notifications]] — SNS, SQS, Lambda Triggers & EventBridge Integration
- [[mm/02-services/storage/s3/s3-lifecycle-rules|S3 Lifecycle Rules]] — Storage Class Transitions, Expirations, Noncurrent Rules & Abort Multipart Uploads
- [[mm/02-services/storage/s3/s3-replication|S3 Replication]] — Cross-Region Replication (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- [[mm/02-services/storage/s3/s3-versioning|S3 Versioning]] — Object Revisions, Delete Markers, MFA Delete & Noncurrent Lifecycle Rules
- [[mm/02-services/storage/s3/s3-security|S3 Security]] — IAM Policies, Bucket Policies, Block Public Access, Object Lock WORM & Macie
- [[mm/02-services/storage/s3/s3-performance|S3 Performance]] — S3 Prefix Limits, Multipart Upload, Byte-Range Fetches, S3 Express One Zone & Bucket Keys
- [[mm/02-services/storage/s3/s3-encryption|S3 Encryption]] — SSE-S3, SSE-KMS, SSE-C, Client-Side Encryption & Bucket Policies
- [[mm/02-services/storage/s3/s3-access-points|S3 Access Points]] — S3 Access Points (VPC & Internet), Multi-Region Access Points & Object Lambda
- [[mm/02-services/storage/s3/s3-tables|S3 Tables]] — Purpose-Built Table Storage for Apache Iceberg & Auto-Compaction
- [[mm/02-services/storage/s3/s3-storage-lens|S3 Storage Lens]] — Organization-Wide Storage Analytics, Cost Optimization & Parquet Exports
- [[mm/02-services/storage/ebs-and-instance-store|Amazon EBS & Instance Store]] — EBS Elastic Block Store & Instance Store
- [[mm/02-services/storage/efs-and-fsx|Amazon EFS & FSx]] — EFS & FSx (Lustre, ONTAP, Windows)
- [[mm/02-services/storage/ebs-vs-efs-vs-instance-store|EBS vs. EFS vs. Instance Store]] — Storage Decision Matrix

#### 🗄️ Database & Data Warehousing (ဒေတာဘေ့စ်နှင့် Data Warehouse)

- [[mm/02-services/database/redshift|Amazon Redshift]] — Data Warehouse, RA3, Managed Storage, Concurrency, Serverless, Spectrum, ML
- [[mm/02-services/database/dynamodb|Amazon DynamoDB]] — Serverless NoSQL, Partition/Sort Keys, GSI/LSI, Streams, DAX
- [[mm/02-services/database/rds-and-aurora|Amazon RDS & Aurora]] — Relational Databases, Aurora Serverless v2, Global Database, Read Replicas
- [[mm/02-services/database/nosql-specialized-databases|Specialized Databases]] — ElastiCache, Keyspaces, Neptune, Timestream

#### 🔄 Migration & Transfer (ဒေတာ ရွှေ့ပြောင်းခြင်းနှင့် လွှဲပြောင်းခြင်း)

- [[mm/02-services/migration/dms-and-sct|AWS DMS & SCT]] — Database Migration Service (DMS) & Schema Conversion Tool (SCT)
- [[mm/02-services/migration/datasync-and-snow|AWS DataSync & Snow Family]] — DataSync & AWS Snow Family (Snowcone, Snowball, Snowmobile)
- [[mm/02-services/migration/application-discovery-and-mgn|Application Discovery & MGN]] — Application Discovery Service & Application Migration Service (MGN)
- [[mm/02-services/migration/data-exchange|AWS Data Exchange]] — Third-Party Data for S3, Redshift & APIs
- [[mm/02-services/migration/transfer-family|AWS Transfer Family]] — AWS Transfer Family (SFTP, FTPS, FTP, AS2)

#### ⚡ Compute & Containers (တွက်ချက်မှုနှင့် ကွန်တိန်နာများ)

- [[mm/02-services/compute-containers/lambda|AWS Lambda]] — Serverless event-driven compute, Event Triggers, streaming batching, `/tmp`, EFS mounts
- [[mm/02-services/compute-containers/batch|AWS Batch]] — Managed containerized batch compute, Job queues, Spot allocation, Array jobs
- [[mm/02-services/compute-containers/ecr-ecs-eks|Amazon ECR, ECS & EKS]] — Docker container registry & orchestration (ECS Fargate, EKS, EMR on EKS)
- [[mm/02-services/compute-containers/ec2-and-graviton|Amazon EC2 & Graviton]] — Amazon EC2 & AWS Graviton (On-Demand, Spot checkpointing, EMR node mapping)

#### 📊 Analytics & Data Pipelines (ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်းနှင့် စီးဆင်းမှု)

- [[mm/02-services/analytics-streaming/glue/glue|AWS Glue Overview]] — Glue Data Catalog, Crawlers, ETL, PySpark, DataBrew, Data Quality, Workflows
- [[mm/02-services/analytics-streaming/athena/athena|Amazon Athena]] — Serverless SQL queries on S3, Partition Projection, CTAS, Federated queries
- [[mm/02-services/analytics-streaming/emr/emr|Amazon EMR]] — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- [[mm/02-services/analytics-streaming/kinesis/kinesis|Amazon Kinesis]] — Kinesis Data Streams, Firehose, Data Analytics (Flink), Video Streams
- [[mm/02-services/analytics-streaming/msk/msk|Amazon MSK]] — Managed Streaming for Apache Kafka, MSK Connect
- [[mm/02-services/analytics-streaming/opensearch/opensearch|Amazon OpenSearch]] — OpenSearch Service, Search indices, Shards & Serverless
- [[mm/02-services/analytics-streaming/quicksight/quicksight|Amazon QuickSight]] — Business Intelligence, SPICE engine, Dashboards, RLS

#### 🔀 Application Integration & Workflow Automation (လုပ်ငန်းစဉ် အလိုအလျောက် ချိတ်ဆက်မှု)

- [[mm/02-services/integration/step-functions/step-functions|AWS Step Functions]] — Orchestrating state machines (Standard vs Express workflows)
- [[mm/02-services/integration/sqs/sqs|Amazon SQS]] — Amazon SQS (Simple Queue Service: Standard/FIFO, Timing, DLQ, Fan-Out & Security)
- [[mm/02-services/integration/sns/sns|Amazon SNS]] — Amazon SNS (Simple Notification Service: Topics, Filter Policies, Delivery Retries & Firehose)
- [[mm/02-services/integration/appflow/appflow|Amazon AppFlow]] — SaaS & AWS integration (Salesforce, ServiceNow, S3)

#### 🔒 Security, Identity & Governance (လုံခြုံရေးနှင့် စီမံအုပ်ချုပ်မှု)

- [[mm/02-services/security-governance/lake-formation|AWS Lake Formation]] — Data Lake Governance, Column/Row-level security, LF-TBAC
- [[mm/02-services/security-governance/iam|AWS IAM]] — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- [[mm/02-services/security-governance/kms-and-secrets|AWS KMS & Secrets Manager]] — KMS SSE-S3/SSE-KMS/SSE-C, Secrets Manager, Parameter Store
- [[mm/02-services/security-governance/macie|Amazon Macie Deep Dive]] — ML-powered PII scanning, Managed & Custom Data Identifiers
- [[mm/02-services/security-governance/macie-and-cloudtrail|Amazon Macie & CloudTrail]] — PII scanning with Macie & CloudTrail audit logs
- [[mm/02-services/security-governance/data-masking-anonymization-and-salting|Data Masking & Salting]] — Redshift DDM, Glue Sensitive Data, Tokenization & Key Salting
- [[mm/02-services/security-governance/aws-backup|AWS Backup]] — Centralized Cross-Service Backup, Vault Lock WORM & Cross-Account DR

#### 🌐 Networking & Edge Security (ကွန်ရက်နှင့် အစွန်အဖျား လုံခြုံရေး)

- [[mm/02-services/networking-monitoring/vpc-and-networking|Amazon VPC & Networking]] — VPC, Subnets, Security Groups, Gateway/Interface Endpoints
- [[mm/02-services/networking-monitoring/waf-and-shield|AWS WAF & AWS Shield]] — Web ACLs, SQLi/XSS Managed Rules, Rate-Based Rules & DDoS Mitigation
- [[mm/02-services/networking-monitoring/cloudwatch-and-eventbridge|CloudWatch & EventBridge]] — Metrics, Logs Insights, EventBridge rules

---

## 📘 Fundamental Concepts Notes (အခြေခံ သဘောတရားများ)

- [[mm/03-concepts/big-data-fundamentals|big-data-fundamentals]] — Big Data 5 V's, Data Warehouse vs Lake vs Swamp
- [[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]] — Parquet, ORC, Avro, JSON, CSV & Snappy/Gzip compression
- [[mm/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]] — Partition strategies, Adaptive partitioning, Schema design
- [[mm/03-concepts/data-validation-and-profiling|data-validation-and-profiling]] — Data Quality rules (DQDL), profiling, Glue Data Quality, PyDeequ & anomaly detection
- [[mm/03-concepts/sql-and-version-control-review|sql-and-version-control-review]] — Window Functions, GROUP BY, Joins & Git fundamentals

---

## 💡 Exam Tips & Decision Matrices (စာမေးပွဲ အကြံပြုချက်များနှင့် နှိုင်းယှဉ်ချက်များ)

- [[mm/04-exam-tips/service-comparisons|service-comparisons]] — Quick reference decision matrix (e.g., S3 vs EBS, Kinesis vs SQS)
- [[mm/04-exam-tips/high-frequency-exam-patterns|high-frequency-exam-patterns]] — အမေးအများဆုံး မေးခွန်းပုံစံများနှင့် သော့ချက်စကားလုံးများ

---

## 🏷️ Key Tags in this Workspace

`#dea-c01` `#aws/service` `#domain/ingestion` `#domain/storage` `#domain/operations` `#domain/security` `#concept/data-engineering` `#exam-tip` `#burmese`
