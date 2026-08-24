---
title: AWS Service Catalog for DEA-C01
type: hub
tags:
  - service-catalog
  - aws/service
  - dea-c01
date: 2026-07-28
---

# 📚 AWS Service Catalog for DEA-C01

Categorized index of all AWS services covered in the **AWS Certified Data Engineer – Associate** slides (`[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`).

---

## 📦 Storage & File Systems

- [[en/02-services/storage/s3/s3|s3]] — Amazon Simple Storage Service (S3)
- [[en/02-services/storage/s3/s3-event-notifications|s3-event-notifications]] — Amazon S3 Event Notifications & EventBridge Integration
- [[en/02-services/storage/s3/s3-lifecycle-rules|s3-lifecycle-rules]] — Amazon S3 Lifecycle Rules & Automated Cost Optimization
- [[en/02-services/storage/s3/s3-replication|s3-replication]] — Amazon S3 Replication (CRR, SRR, RTC & Batch Replication)
- [[en/02-services/storage/s3/s3-versioning|s3-versioning]] — Amazon S3 Versioning, Delete Markers & MFA Delete
- [[en/02-services/storage/s3/s3-security|s3-security]] — Amazon S3 Security & Access Management
- [[en/02-services/storage/s3/s3-performance|s3-performance]] — Amazon S3 Performance & Optimization Strategies
- [[en/02-services/storage/s3/s3-encryption|s3-encryption]] — Amazon S3 Encryption (SSE-S3, SSE-KMS, SSE-C & Client-Side)
- [[en/02-services/storage/s3/s3-access-points|s3-access-points]] — Amazon S3 Access Points & Object Lambda
- [[en/02-services/storage/s3/s3-tables|s3-tables]] — Amazon S3 Tables for Apache Iceberg
- [[en/02-services/storage/s3/s3-storage-lens|s3-storage-lens]] — Amazon S3 Storage Lens Analytics & Insights
- [[en/02-services/storage/ebs-and-instance-store|ebs-and-instance-store]] — Amazon Elastic Block Store (EBS) & EC2 Instance Store
- [[en/02-services/storage/efs-and-fsx|efs-and-fsx]] — Amazon Elastic File System (EFS) & FSx (Lustre, ONTAP, Windows)
- [[en/02-services/storage/ebs-vs-efs-vs-instance-store|ebs-vs-efs-vs-instance-store]] — Storage Decision Matrix: EFS vs. EBS vs. EC2 Instance Store

## 🗄️ Databases & Data Warehouses

- [[en/02-services/database/redshift|redshift]] — Amazon Redshift (Data Warehouse, Serverless, Spectrum, ML)
- [[en/02-services/database/dynamodb|dynamodb]] — Amazon DynamoDB (NoSQL Key-Value & Document Database)
- [[en/02-services/database/rds-and-aurora|rds-and-aurora]] — Amazon RDS (PostgreSQL, MySQL) & Amazon Aurora
- [[en/02-services/database/nosql-specialized-databases|nosql-specialized-databases]] — ElastiCache (Redis/Memcached), Keyspaces (Cassandra), Neptune (Graph), Timestream (Time Series)

## 🔄 Migration & Transfer

- [[en/02-services/migration/dms-and-sct|dms-and-sct]] — AWS Database Migration Service (DMS) & Schema Conversion Tool (SCT)
- [[en/02-services/migration/datasync-and-snow|datasync-and-snow]] — AWS DataSync & AWS Snow Family (Snowcone, Snowball Edge, Snowmobile)
- [[en/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] — AWS Application Discovery Service & AWS Application Migration Service (MGN)
- [[en/02-services/migration/data-exchange|data-exchange]] — AWS Data Exchange (Third-Party Data for S3, Redshift & APIs)
- [[en/02-services/migration/transfer-family|transfer-family]] — AWS Transfer Family (SFTP, FTPS, FTP, AS2)


## ⚡ Compute & Containers

- [[en/02-services/compute-containers/lambda|lambda]] — AWS Lambda (Serverless Event-Driven Compute)
- [[en/02-services/compute-containers/batch|batch]] — AWS Batch (Managed Containerized Batch Computing)
- [[en/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] — Amazon ECR, Amazon ECS & Amazon EKS (Containerized Workloads)
- [[en/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]] — Amazon EC2 & AWS Graviton in Big Data (Purchasing Models & Arm Architecture)


## 📊 Analytics & Streaming

- [[en/02-services/analytics-streaming/glue/glue|glue]] — AWS Glue (Data Catalog, Crawlers, ETL, DataBrew, Data Quality)
- [[en/02-services/analytics-streaming/athena/athena|athena]] — Amazon Athena (Interactive Serverless SQL)
- [[en/02-services/analytics-streaming/emr/emr|emr]] — Amazon EMR (Spark, Hadoop, Hive, Presto, EMR Serverless)
- [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] — Amazon Kinesis (Data Streams, Data Firehose, Data Analytics/Flink, Video Streams)
- [[en/02-services/analytics-streaming/msk/msk|msk]] — Amazon MSK (Managed Streaming for Apache Kafka)
- [[en/02-services/analytics-streaming/opensearch/opensearch|opensearch]] — Amazon OpenSearch Service (Search & Analytics)
- [[en/02-services/analytics-streaming/quicksight/quicksight|quicksight]] — Amazon QuickSight (Business Intelligence & Dashboards)

## 🔀 Integration & Orchestration

- [[en/02-services/integration/sqs/sqs|sqs]] — Amazon SQS (Simple Queue Service Modular Suite)
- [[en/02-services/integration/sns/sns|sns]] — Amazon SNS (Simple Notification Service Modular Suite)
- [[en/02-services/integration/sqs-and-sns|sqs-and-sns]] — Amazon SQS & Amazon SNS Overview
- [[en/02-services/integration/step-functions/step-functions|step-functions]] — AWS Step Functions (State Machines)
- [[en/02-services/integration/appflow/appflow|appflow]] — AWS AppFlow (SaaS Data Integration)
- [[en/02-services/integration/mwaa-airflow|mwaa-airflow]] — Amazon Managed Workflows for Apache Airflow (MWAA)

## 🔒 Security, Identity & Governance

- [[en/02-services/security-governance/iam|iam]] — AWS Identity and Access Management (IAM)
- [[en/02-services/security-governance/kms-and-secrets|kms-and-secrets]] — AWS KMS, AWS Secrets Manager & SSM Parameter Store
- [[en/02-services/security-governance/lake-formation|lake-formation]] — AWS Lake Formation (Data Lake Access Control & Fine-Grained Permissions)
- [[en/02-services/security-governance/macie-and-cloudtrail|macie-and-cloudtrail]] — AWS Macie (PII Discovery) & AWS CloudTrail (Audit Logging)
- [[en/02-services/security-governance/aws-backup|aws-backup]] — AWS Backup (Centralized Policy-Based Data Protection & Vault Lock WORM)

## 🌐 Networking & Management

- [[en/02-services/networking-monitoring/vpc-and-networking|vpc-and-networking]] — Amazon VPC, Subnets, Security Groups, VPC Endpoints
- [[en/02-services/networking-monitoring/cloudwatch-and-eventbridge|cloudwatch-and-eventbridge]] — Amazon CloudWatch & Amazon EventBridge

## 🤖 ML, Developer Tools & Cost

- [[en/02-services/ml-dev-cost/sagemaker-and-ai|sagemaker-and-ai]] — Amazon SageMaker (Data Wrangler, Feature Store) & AI Services
- [[en/02-services/ml-dev-cost/cdk-cloudformation|cdk-cloudformation]] — AWS CDK, CloudFormation, SAM
- [[en/02-services/ml-dev-cost/cost-management|cost-management]] — AWS Cost Explorer, AWS Budgets, Savings Plans, CUR

---

## 📌 Master Hub Link

Return to main hub: [[en/index|index]]
