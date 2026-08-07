---
title: AWS DEA-C01 Knowledge Hub
type: hub
tags:
  - hub
  - dea-c01
date: 2026-07-28
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) Knowledge Hub

Welcome to your **Personal Knowledge Management (PKM)** workspace for preparing for the **AWS Certified Data Engineer – Associate (DEA-C01)** certification exam!

This workspace is structured directly from the **AWS Certified Data Engineer Associate Course** by Stephane Maarek & Frank Kane ([AWSCertifiedDataEngineerSlides.pdf](docs/AWSCertifiedDataEngineerSlides.pdf)).

---

## 🗺️ Master Navigation (MOCs)

### 📌 Exam Roadmap & Catalog

- [[dea-c01-roadmap]] — Exam domains breakdown, weightings & study strategy
- [[service-catalog]] — Full directory of AWS services covered in the slides

---

### 🎯 DEA-C01 Exam Domains (Official Outline)

1. [[domain-1-ingestion-and-processing]] _(28% Weight)_ — Data Ingestion & Transformation Pipelines
2. [[domain-2-data-store-management]] _(26% Weight)_ — Storage Systems, Schemas, & Data Warehousing
3. [[domain-3-data-operations-and-support]] _(22% Weight)_ — Automation, Monitoring, & Troubleshooting
4. [[domain-4-data-security-and-governance]] _(24% Weight)_ — Encryption, IAM, Governance & Compliance

---

### ☁️ AWS Services Notes (By Slide Sections)

#### 📦 Storage

- [[s3]] — Amazon S3 Storage Classes, Policies, Lifecycle, Object Lock, Replication & Lens
- [[s3-performance]] — S3 Prefix Limits, Multipart Upload, Byte-Range Fetches, S3 Express One Zone & Bucket Keys
- [[s3-encryption]] — SSE-S3, SSE-KMS, SSE-C, Client-Side Encryption & Bucket Policies
- [[ebs-and-instance-store]] — EBS Elastic Block Store & Instance Store
- [[efs-and-fsx]] — EFS & FSx (Lustre, ONTAP, Windows)

#### 🗄️ Database & Data Warehousing

- [[redshift]] — Data Warehouse, RA3, Managed Storage, Concurrency, Serverless, Spectrum, ML
- [[dynamodb]] — Serverless NoSQL, Partition/Sort Keys, GSI/LSI, Streams, DAX
- [[rds-and-aurora]] — Relational Databases, Aurora Serverless v2, Global Database, Read Replicas
- [[nosql-specialized-databases]] — ElastiCache, Keyspaces, Neptune, Timestream

#### 🔄 Migration & Transfer

- [[dms-and-sct]] — Database Migration Service (DMS) & Schema Conversion Tool (SCT)
- [[datasync-and-snow]] — DataSync & AWS Snow Family (Snowcone, Snowball, Snowmobile)

#### ⚡ Compute & Containers

- [[lambda]] — Serverless compute, Event Triggers, `/tmp` storage, DLQ
- [[batch]] — AWS Batch compute environment & job queues
- [[ecr-ecs-eks]] — Docker container registry & orchestration (ECS Fargate, EKS)

#### 📊 Analytics & Data Pipelines

- [[glue]] — Glue Data Catalog, Crawlers, ETL, PySpark, DataBrew, Data Quality, Workflows
- [[athena]] — Serverless SQL queries on S3, Partition Projection, CTAS, Federated queries
- [[emr]] — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- [[kinesis]] — Kinesis Data Streams, Firehose, Data Analytics (Flink), Video Streams
- [[msk-kafka]] — Managed Streaming for Apache Kafka, MSK Connect
- [[opensearch]] — OpenSearch Service, Search indices, Shards & Serverless
- [[quicksight]] — Business Intelligence, SPICE engine, Dashboards, RLS

#### 🔀 Application Integration & Workflow Automation

- [[step-functions]] — Orchestrating state machines (Standard vs Express workflows)
- [[mwaa-airflow]] — Managed Workflows for Apache Airflow, DAGs & Operators
- [[sqs-and-sns]] — Simple Queue Service (Standard/FIFO) & Simple Notification Service
- [[appflow]] — SaaS & AWS integration (Salesforce, ServiceNow, S3)

#### 🔒 Security, Identity & Governance

- [[lake-formation]] — Data Lake Governance, Column/Row-level security, LF-TBAC
- [[iam]] — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- [[kms-and-secrets]] — KMS SSE-S3/SSE-KMS/SSE-C, Secrets Manager, Parameter Store
- [[macie-and-cloudtrail]] — PII scanning with Macie & CloudTrail audit logs

#### 🌐 Networking & Governance

- [[vpc-and-networking]] — VPC, Subnets, Security Groups, Gateway/Interface Endpoints
- [[cloudwatch-and-eventbridge]] — Metrics, Logs Insights, EventBridge rules

#### 🤖 ML, Developer Tools & Cost

- [[sagemaker-and-ai]] — SageMaker Data Wrangler, Feature Store, Ground Truth, Q Business
- [[cdk-cloudformation]] — CDK, CloudFormation, SAM infrastructure as code
- [[cost-management]] — Cost Explorer, AWS Budgets, Savings Plans, CUR

---

### 📘 Fundamental Concepts Notes

- [[big-data-fundamentals]] — Big Data 5 V's, Data Warehouse vs Lake vs Swamp
- [[data-formats-and-compression]] — Parquet, ORC, Avro, JSON, CSV & Snappy/Gzip compression
- [[data-modeling-and-partitioning]] — Partition strategies, Adaptive partitioning, Schema design
- [[data-validation-and-profiling]] — Data Quality rules (DQDL), profiling, Glue Data Quality, PyDeequ & anomaly detection
- [[sql-and-version-control-review]] — Window Functions, GROUP BY, Joins & Git fundamentals

---

### 💡 Exam Tips & Decision Matrices

- [[service-comparisons]] — Quick reference decision matrix (e.g., S3 vs EBS, Kinesis vs SQS)
- [[high-frequency-exam-patterns]] — Top scenario questions and architectural keywords

---

## 🏷️ Key Tags in this Workspace

`#dea-c01` `#aws/service` `#domain/ingestion` `#domain/storage` `#domain/operations` `#domain/security` `#concept/data-engineering` `#exam-tip`
