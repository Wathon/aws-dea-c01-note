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
- [[lab-materials-index]] — Catalog of hands-on lab code, CLI scripts & sample datasets (`content/materials/`)

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
- [[s3-event-notifications]] — SNS, SQS, Lambda Triggers & EventBridge Integration
- [[s3-lifecycle-rules]] — Storage Class Transitions, Expirations, Noncurrent Rules & Abort Multipart Uploads
- [[s3-replication]] — Cross-Region Replication (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- [[s3-versioning]] — Object Revisions, Delete Markers, MFA Delete & Noncurrent Lifecycle Rules
- [[s3-security]] — IAM Policies, Bucket Policies, Block Public Access, Object Lock WORM & Macie
- [[s3-performance]] — S3 Prefix Limits, Multipart Upload, Byte-Range Fetches, S3 Express One Zone & Bucket Keys
- [[s3-encryption]] — SSE-S3, SSE-KMS, SSE-C, Client-Side Encryption & Bucket Policies
- [[s3-access-points]] — S3 Access Points (VPC & Internet), Multi-Region Access Points & Object Lambda
- [[s3-tables]] — Purpose-Built Table Storage for Apache Iceberg & Auto-Compaction
- [[s3-storage-lens]] — Organization-Wide Storage Analytics, Cost Optimization & Parquet Exports
- [[ebs-and-instance-store]] — EBS Elastic Block Store & Instance Store
- [[efs-and-fsx]] — EFS & FSx (Lustre, ONTAP, Windows)
- [[ebs-vs-efs-vs-instance-store]] — Decision Matrix: EFS vs. EBS vs. EC2 Instance Store

#### 🗄️ Database & Data Warehousing

- [[redshift]] — Data Warehouse, RA3, Managed Storage, Concurrency, Serverless, Spectrum, ML
- [[dynamodb]] — Serverless NoSQL, Partition/Sort Keys, GSI/LSI, Streams, DAX
- [[rds-and-aurora]] — Relational Databases, Aurora Serverless v2, Global Database, Read Replicas
- [[nosql-specialized-databases]] — ElastiCache, Keyspaces, Neptune, Timestream

#### 🔄 Migration & Transfer

- [[dms-and-sct]] — Database Migration Service (DMS) & Schema Conversion Tool (SCT)
- [[datasync-and-snow]] — DataSync & AWS Snow Family (Snowcone, Snowball, Snowmobile)
- [[application-discovery-and-mgn]] — Application Discovery Service & Application Migration Service (MGN)
- [[data-exchange]] — AWS Data Exchange (Third-Party Data for S3, Redshift & APIs)
- [[transfer-family]] — AWS Transfer Family (SFTP, FTPS, FTP, AS2)


#### ⚡ Compute & Containers

- [[lambda]] — Serverless event-driven compute, Event Triggers, streaming batching, `/tmp`, EFS mounts
- [[batch]] — Managed containerized batch compute, Job queues, Spot allocation, Array jobs
- [[ecr-ecs-eks]] — Docker container registry & orchestration (ECS Fargate, EKS, EMR on EKS)
- [[ec2-and-graviton]] — Amazon EC2 & AWS Graviton (On-Demand, Spot checkpointing, EMR node mapping)


#### 📊 Analytics & Data Pipelines

- [[glue]] — Glue Data Catalog, Crawlers, ETL, PySpark, DataBrew, Data Quality, Workflows
- [[athena]] — Serverless SQL queries on S3, Partition Projection, CTAS, Federated queries
- [[emr]] — Elastic MapReduce (Spark, Hadoop, Presto), EMR Serverless, EMR on EKS
- [[kinesis]] — Kinesis Data Streams, Firehose, Data Analytics (Flink), Video Streams
- [[msk]] — Managed Streaming for Apache Kafka, MSK Connect
- [[opensearch]] — OpenSearch Service, Search indices, Shards & Serverless
- [[quicksight]] — Business Intelligence, SPICE engine, Dashboards, RLS

#### 🔀 Application Integration & Workflow Automation

- [[step-functions]] — Orchestrating state machines (Standard vs Express workflows)
- [[mwaa-airflow]] — Managed Workflows for Apache Airflow, DAGs & Operators
- [[sqs]] — Amazon SQS (Simple Queue Service: Standard/FIFO, Timing, DLQ, Fan-Out & Security)
- [[sqs-and-sns]] — Simple Queue Service & Simple Notification Service Overview
- [[appflow]] — SaaS & AWS integration (Salesforce, ServiceNow, S3)

#### 🔒 Security, Identity & Governance

- [[lake-formation]] — Data Lake Governance, Column/Row-level security, LF-TBAC
- [[iam]] — IAM Roles, Policies, Service Linked Roles, Access Analyzer
- [[kms-and-secrets]] — KMS SSE-S3/SSE-KMS/SSE-C, Secrets Manager, Parameter Store
- [[macie-and-cloudtrail]] — PII scanning with Macie & CloudTrail audit logs
- [[aws-backup]] — Centralized Cross-Service Backup, Vault Lock WORM & Cross-Account DR

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
