---
title: AWS DEA-C01 English Knowledge Hub
type: hub
tags:
  - hub
  - dea-c01
  - english
date: 2026-08-15
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) Knowledge Hub (English)

- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/index)
- **Course Slides**: [AWSCertifiedDataEngineerSlides.pdf](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/docs/AWSCertifiedDataEngineerSlides.pdf)
- **Hands-on Labs & Datasets**: [Lab Materials Directory](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/materials) | [[en/00-hub/lab-materials-index|lab-materials-index]]
- **Study Journal**: [[journal/2026-07-28]]

---

## 🗺️ Master Navigation (MOCs)

### 📌 Exam Roadmap & Catalog

- [[en/00-hub/dea-c01-roadmap|dea-c01-roadmap]] — Exam domains breakdown, weightings & study strategy
- [[en/00-hub/service-catalog|service-catalog]] — Full directory of AWS services covered in the slides
- [[en/00-hub/lab-materials-index|lab-materials-index]] — Catalog of hands-on lab code, CLI scripts & sample datasets (`content/materials/`)

---

### 🎯 DEA-C01 Exam Domains (Official Outline)

1. [[en/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]] _(28% Weight)_ — Data Ingestion & Transformation Pipelines
2. [[en/01-domains/domain-2-data-store-management|domain-2-data-store-management]] _(26% Weight)_ — Storage Systems, Schemas, & Data Warehousing
3. [[en/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]] _(22% Weight)_ — Automation, Monitoring, & Troubleshooting
4. [[en/01-domains/domain-4-data-security-and-governance|domain-4-data-security-and-governance]] _(24% Weight)_ — Encryption, IAM, Governance & Compliance

---

### ☁️ AWS Services Notes (By Slide Sections)

#### 📦 Storage

- [[en/02-services/storage/s3/s3|s3]] — Amazon S3 Storage Classes, Policies, Lifecycle, Object Lock, Replication & Lens
- [[en/02-services/storage/s3/s3-event-notifications|s3-event-notifications]] — SNS, SQS, Lambda Triggers & EventBridge Integration
- [[en/02-services/storage/s3/s3-lifecycle-rules|s3-lifecycle-rules]] — Storage Class Transitions, Expirations, Noncurrent Rules & Abort Multipart Uploads
- [[en/02-services/storage/s3/s3-replication|s3-replication]] — Cross-Region Replication (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- [[en/02-services/storage/s3/s3-versioning|s3-versioning]] — Object Revisions, Delete Markers, MFA Delete & Noncurrent Lifecycle Rules
- [[en/02-services/storage/s3/s3-security|s3-security]] — IAM Policies, Bucket Policies, Block Public Access, Object Lock WORM & Macie
- [[en/02-services/storage/s3/s3-performance|s3-performance]] — S3 Prefix Limits, Multipart Upload, Byte-Range Fetches, S3 Express One Zone & Bucket Keys
- [[en/02-services/storage/s3/s3-encryption|s3-encryption]] — SSE-S3, SSE-KMS, SSE-C, Client-Side Encryption & Bucket Policies
- [[en/02-services/storage/s3/s3-access-points|s3-access-points]] — S3 Access Points (VPC & Internet), Multi-Region Access Points & Object Lambda
- [[en/02-services/storage/s3/s3-tables|s3-tables]] — Purpose-Built Table Storage for Apache Iceberg & Auto-Compaction
- [[en/02-services/storage/s3/s3-storage-lens|s3-storage-lens]] — Organization-Wide Storage Analytics, Cost Optimization & Parquet Exports
- [[en/02-services/storage/ebs-and-instance-store|ebs-and-instance-store]] — EBS Elastic Block Store & Instance Store
- [[en/02-services/storage/efs-and-fsx|efs-and-fsx]] — EFS & FSx (Lustre, ONTAP, Windows)
- [[en/02-services/storage/ebs-vs-efs-vs-instance-store|ebs-vs-efs-vs-instance-store]] — Decision Matrix: EFS vs. EBS vs. EC2 Instance Store

#### 🗄️ Database & Data Warehousing

- [[en/02-services/database/redshift|redshift]] — Data Warehouse, RA3, Managed Storage, Concurrency, Serverless, Spectrum, ML
- [[en/02-services/database/dynamodb|dynamodb]] — Serverless NoSQL, Partition/Sort Keys, GSI/LSI, Streams, DAX
- [[en/02-services/database/rds-and-aurora|rds-and-aurora]] — Relational Databases, Aurora Serverless v2, Global Database, Read Replicas
- [[en/02-services/database/nosql-specialized-databases|nosql-specialized-databases]] — ElastiCache, Keyspaces, Neptune, Timestream

#### 🔄 Migration & Transfer

- [[en/02-services/migration/dms-and-sct|dms-and-sct]] — Database Migration Service (DMS) & Schema Conversion Tool (SCT)
- [[en/02-services/migration/datasync-and-snow|datasync-and-snow]] — DataSync & AWS Snow Family (Snowcone, Snowball, Snowmobile)
- [[en/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] — Application Discovery Service & Application Migration Service (MGN)
- [[en/02-services/migration/data-exchange|data-exchange]] — AWS Data Exchange (Third-Party Data for S3, Redshift & APIs)
- [[en/02-services/migration/transfer-family|transfer-family]] — AWS Transfer Family (SFTP, FTPS, FTP, AS2)

#### ⚡ Compute & Containers

- [[en/02-services/compute-containers/lambda|lambda]] — Serverless event-driven compute, Event Triggers, streaming batching, `/tmp`, EFS mounts
- [[en/02-services/compute-containers/batch|batch]] — Managed containerized batch compute, Job queues, Spot allocation, Array jobs
- [[en/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] — Docker container registry & orchestration (ECS Fargate, EKS, EMR on EKS)
- [[en/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]] — Amazon EC2 & AWS Graviton (On-Demand, Spot checkpointing, EMR node mapping)

#### 📊 Analytics & Data Pipelines

- [[en/02-services/analytics-streaming/glue/glue|AWS Glue Overview]] — Serverless Data Integration & ETL
- [[en/02-services/analytics-streaming/glue/glue-data-catalog|glue-data-catalog]] — Glue Data Catalog & Metastore
- [[en/02-services/analytics-streaming/glue/glue-crawlers|glue-crawlers]] — Glue Crawlers & Schema Inference
- [[en/02-services/analytics-streaming/glue/glue-etl-jobs|glue-etl-jobs]] — Glue ETL Jobs, DynamicFrames & Bookmarks
- [[en/02-services/analytics-streaming/glue/glue-flex|glue-flex]] — AWS Glue Flex Execution Class (Cost Optimization)
- [[en/02-services/analytics-streaming/glue/glue-studio|glue-studio]] — AWS Glue Studio Visual ETL
- [[en/02-services/analytics-streaming/glue/glue-workflows|glue-workflows]] — AWS Glue Workflows Orchestration
- [[en/02-services/analytics-streaming/glue/glue-data-quality|glue-data-quality]] — AWS Glue Data Quality (DQDL)
- [[en/02-services/analytics-streaming/glue/glue-schema-registry|glue-schema-registry]] — AWS Glue Schema Registry (Kafka/Kinesis)
- [[en/02-services/analytics-streaming/glue/glue-databrew|glue-databrew]] — AWS Glue DataBrew No-code ETL
- [[en/02-services/analytics-streaming/athena/athena|athena]] — Serverless SQL queries on S3, Partition Projection, CTAS, Federated queries
- [[en/02-services/analytics-streaming/emr/emr|emr]] — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] — Kinesis Data Streams, Firehose, Data Analytics (Flink), Video Streams
- [[en/02-services/analytics-streaming/msk/msk|msk]] — Managed Streaming for Apache Kafka, MSK Connect
- [[en/02-services/analytics-streaming/opensearch/opensearch|opensearch]] — OpenSearch Service, Search indices, Shards & Serverless
- [[en/02-services/analytics-streaming/quicksight/quicksight|quicksight]] — Business Intelligence, SPICE engine, Dashboards, RLS

#### 🔀 Application Integration & Workflow Automation

- [[en/02-services/integration/step-functions/step-functions|step-functions]] — Orchestrating state machines (Standard vs Express workflows)
- [[en/02-services/integration/mwaa-airflow|mwaa-airflow]] — Managed Workflows for Apache Airflow, DAGs & Operators
- [[en/02-services/integration/sqs/sqs|sqs]] — Amazon SQS (Simple Queue Service: Standard/FIFO, Timing, DLQ, Fan-Out & Security)
- [[en/02-services/integration/sns/sns|sns]] — Amazon SNS (Simple Notification Service: Topics, Filter Policies, Delivery Retries & Firehose)
- [[en/02-services/integration/sqs-and-sns|sqs-and-sns]] — Simple Queue Service & Simple Notification Service Overview
- [[en/02-services/integration/appflow/appflow|appflow]] — SaaS & AWS integration (Salesforce, ServiceNow, S3)

#### 🔒 Security, Identity & Governance

- [[en/02-services/security-governance/lake-formation|lake-formation]] — Data Lake Governance, Column/Row-level security, LF-TBAC
- [[en/02-services/security-governance/iam|iam]] — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- [[en/02-services/security-governance/kms-and-secrets|kms-and-secrets]] — KMS SSE-S3/SSE-KMS/SSE-C, Secrets Manager, Parameter Store
- [[en/02-services/security-governance/macie-and-cloudtrail|macie-and-cloudtrail]] — PII scanning with Macie & CloudTrail audit logs
- [[en/02-services/security-governance/aws-backup|aws-backup]] — Centralized Cross-Service Backup, Vault Lock WORM & Cross-Account DR

#### 🌐 Networking & Governance

- [[en/02-services/networking-monitoring/vpc-and-networking|vpc-and-networking]] — VPC, Subnets, Security Groups, Gateway/Interface Endpoints
- [[en/02-services/networking-monitoring/cloudwatch-and-eventbridge|cloudwatch-and-eventbridge]] — Metrics, Logs Insights, EventBridge rules

#### 🤖 ML, Developer Tools & Cost

- [[en/02-services/ml-dev-cost/sagemaker-and-ai|sagemaker-and-ai]] — SageMaker Data Wrangler, Feature Store, Ground Truth, Q Business
- [[en/02-services/ml-dev-cost/cdk-cloudformation|cdk-cloudformation]] — CDK, CloudFormation, SAM infrastructure as code
- [[en/02-services/ml-dev-cost/cost-management|cost-management]] — Cost Explorer, AWS Budgets, Savings Plans, CUR

---

## 📘 Fundamental Concepts Notes

- [[en/03-concepts/big-data-fundamentals|big-data-fundamentals]] — Big Data 5 V's, Data Warehouse vs Lake vs Swamp
- [[en/03-concepts/data-formats-and-compression|data-formats-and-compression]] — Parquet, ORC, Avro, JSON, CSV & Snappy/Gzip compression
- [[en/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]] — Partition strategies, Adaptive partitioning, Schema design
- [[en/03-concepts/data-validation-and-profiling|data-validation-and-profiling]] — Data Quality rules (DQDL), profiling, Glue Data Quality, PyDeequ & anomaly detection
- [[en/03-concepts/sql-and-version-control-review|sql-and-version-control-review]] — Window Functions, GROUP BY, Joins & Git fundamentals

---

## 💡 Exam Tips & Decision Matrices

- [[en/04-exam-tips/service-comparisons|service-comparisons]] — Quick reference decision matrix (e.g., S3 vs EBS, Kinesis vs SQS)
- [[en/04-exam-tips/high-frequency-exam-patterns|high-frequency-exam-patterns]] — Top scenario questions and architectural keywords

---

## 🏷️ Key Tags in this Workspace

`#dea-c01` `#aws/service` `#domain/ingestion` `#domain/storage` `#domain/operations` `#domain/security` `#concept/data-engineering` `#exam-tip`
