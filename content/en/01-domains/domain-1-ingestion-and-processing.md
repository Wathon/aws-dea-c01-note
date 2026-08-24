---
title: "Domain 1: Data Ingestion and Processing"
type: domain
tags:
  - domain/ingestion
  - dea-c01
  - exam-prep
date: 2026-07-28
---

# 📥 Domain 1: Data Ingestion and Processing (Weight: 28%)

- **Domain ID**: Domain 1
- **Focus**: Designing, implementing, and optimizing batch and streaming data ingestion pipelines and ETL processing workflows.
- **Hub Links**: [[en/index|index]] | [[en/00-hub/dea-c01-roadmap|dea-c01-roadmap]] | [[en/00-hub/service-catalog|service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 1.1: Design and implement data ingestion solutions
- **Batch & External Data Ingestion**:
  - Scheduled batch extraction from databases using [[en/02-services/migration/dms-and-sct|dms-and-sct]] or [[en/02-services/analytics-streaming/glue/glue|glue]] JDBC connections.
  - Large-scale file transfer using [[en/02-services/migration/datasync-and-snow|datasync-and-snow]] (DataSync, Snowball Edge).
  - External commercial third-party datasets using [[en/02-services/migration/data-exchange|data-exchange]] (S3 exports, Redshift data sharing, REST APIs).
  - Managed B2B partner file transfers via [[en/02-services/migration/transfer-family|transfer-family]] (SFTP, FTPS, FTP, AS2).
  - On-premises discovery & server rehosting via [[en/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] (Application Discovery Service & MGN).
- **Streaming Ingestion**:
  - Real-time streaming using [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Streams, Kinesis Data Firehose).
  - Managed Apache Kafka using [[en/02-services/analytics-streaming/msk/msk|msk]] (Amazon MSK & MSK Connect).
  - SaaS application ingestion using [[en/02-services/integration/appflow/appflow|appflow]] (Salesforce, ServiceNow, Slack).

### Task Statement 1.2: Transform and process data
- **ETL/ELT Engine Selection**:
  - Serverless Spark processing using [[en/02-services/analytics-streaming/glue/glue|glue]] ETL jobs (PySpark, Scala) and [[en/02-services/analytics-streaming/glue/glue|glue]] DataBrew.
  - Distributed cluster processing using [[en/02-services/analytics-streaming/emr/emr|emr]] (Spark, Hive, Presto, EMR Serverless, EMR on EKS).
  - Light event-driven transformations using [[en/02-services/compute-containers/lambda|lambda]] (< 15 mins).
  - Containerized batch compute & non-Spark workloads using [[en/02-services/compute-containers/batch|batch]] (Spot allocation, Docker images).
  - Container microservices & Kubernetes pipelines using [[en/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] (ECS Fargate, EKS).
  - Spot Instance topologies & Graviton price-performance optimization using [[en/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]].
- **Data Transformation Practices**:
  - Converting raw formats (CSV, JSON) into optimized columnar formats ([[en/03-concepts/data-formats-and-compression|data-formats-and-compression]] — Parquet, ORC).
  - Applying partition schemes ([[en/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]]) for query performance.

### Task Statement 1.3: Orchestrate data processing workflows
- **State Machine Orchestration**:
  - Complex multi-step workflows using [[en/02-services/integration/step-functions/step-functions|step-functions]] (Standard vs Express Workflows).
- **DAG Workflow Orchestration**:
  - Programmatic workflow management using Apache Airflow on [[en/02-services/integration/mwaa-airflow|mwaa-airflow]] (DAGs, Operators, Sensors).

---

## 🛠️ Essential AWS Services in Domain 1

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS Glue** | Serverless ETL & Crawlers | Transform data in S3 to Parquet; catalog schemas automatically | [[en/02-services/analytics-streaming/glue/glue|glue]] |
| **Amazon Kinesis** | Streaming Ingestion | Near real-time ingestion to S3/Redshift/OpenSearch | [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] |
| **Amazon MSK** | Apache Kafka | Open-source streaming compatibility with low latency | [[en/02-services/analytics-streaming/msk/msk|msk]] |
| **AWS Lambda** | Event-Driven Compute | Micro-batch processing, file upload triggers from S3 | [[en/02-services/compute-containers/lambda|lambda]] |
| **AWS Batch** | Containerized Batch Compute | Non-Spark batch processing (> 15 mins), Spot array jobs | [[en/02-services/compute-containers/batch|batch]] |
| **Amazon ECR, ECS & EKS** | Container Orchestration | Docker registries, Fargate serverless containers, EMR on EKS | [[en/02-services/compute-containers/ecr-ecs-eks|ecr-ecs-eks]] |
| **Amazon EC2 & Graviton** | Big Data Compute Infrastructure | Spot checkpointing, EMR node mapping, Graviton Arm pricing | [[en/02-services/compute-containers/ec2-and-graviton|ec2-and-graviton]] |
| **AWS Step Functions** | Workflow Orchestration | Visual state machine for ETL pipelines with error handling | [[en/02-services/integration/step-functions/step-functions|step-functions]] |
| **Amazon MWAA** | Airflow DAG Orchestration | Complex python-defined dependency workflows | [[en/02-services/integration/mwaa-airflow|mwaa-airflow]] |
| **AWS AppFlow** | SaaS Integration | Secure data flow from Salesforce, ServiceNow to S3/Redshift | [[en/02-services/integration/appflow/appflow|appflow]] |
| **AWS DMS & SCT** | Database Migration & CDC | Heterogeneous/homogeneous DB replication into S3/Redshift | [[en/02-services/migration/dms-and-sct|dms-and-sct]] |
| **AWS DataSync & Snow** | File Transfer & Edge Devices | High-speed network transfer & offline multi-TB/PB migration | [[en/02-services/migration/datasync-and-snow|datasync-and-snow]] |
| **AWS Data Exchange** | 3rd-Party Data Marketplace | S3 export, Redshift zero-ETL querying, managed APIs | [[en/02-services/migration/data-exchange|data-exchange]] |
| **AWS Transfer Family** | Managed SFTP/FTPS | B2B vendor file exchange directly into S3 and EFS | [[en/02-services/migration/transfer-family|transfer-family]] |
| **Application Discovery & MGN** | Discovery & Server Rehost | Plan migration waves and automated block-level server rehosting | [[en/02-services/migration/application-discovery-and-mgn|application-discovery-and-mgn]] |



---

## ⚡ High-Yield Exam Scenarios for Domain 1

> [!IMPORTANT]
> **Stream vs Batch Selection**:
> - If requirement is **real-time ingestion with custom transformation logic and retention up to 365 days**: Choose [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Streams).
> - If requirement is **zero-code streaming direct to S3, Redshift, or OpenSearch with micro-batching**: Choose [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] (Kinesis Data Firehose).
> - If requirement is **open-source Kafka ecosystem / custom producers**: Choose [[en/02-services/analytics-streaming/msk/msk|msk]].

> [!TIP]
> **Glue vs EMR Selection**:
> - Choose [[en/02-services/analytics-streaming/glue/glue|glue]] for **serverless ETL, AWS-native catalog integration, dynamic frames, and minimal infrastructure management**.
> - Choose [[en/02-services/analytics-streaming/emr/emr|emr]] when needing **custom open-source Spark/Hadoop libraries, fine-grained cluster tuning, long-running cluster efficiency, or EMR Serverless**.

---

## 📌 Checklist for Domain 1
- [ ] Review slide pages: 266-312 (Migration & Compute) and 331-459 (Analytics & Streaming) in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- [ ] Complete service notes: [[en/02-services/analytics-streaming/glue/glue|glue]], [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]], [[en/02-services/compute-containers/lambda|lambda]], [[en/02-services/integration/step-functions/step-functions|step-functions]], [[en/02-services/integration/mwaa-airflow|mwaa-airflow]]
- [ ] Review data formats: [[en/03-concepts/data-formats-and-compression|data-formats-and-compression]]
