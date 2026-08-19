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
- **Hub Links**: [[index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 1.1: Design and implement data ingestion solutions
- **Batch & External Data Ingestion**:
  - Scheduled batch extraction from databases using [[dms-and-sct]] or [[glue]] JDBC connections.
  - Large-scale file transfer using [[datasync-and-snow]] (DataSync, Snowball Edge).
  - External commercial third-party datasets using [[data-exchange]] (S3 exports, Redshift data sharing, REST APIs).
  - Managed B2B partner file transfers via [[transfer-family]] (SFTP, FTPS, FTP, AS2).
  - On-premises discovery & server rehosting via [[application-discovery-and-mgn]] (Application Discovery Service & MGN).
- **Streaming Ingestion**:
  - Real-time streaming using [[kinesis]] (Kinesis Data Streams, Kinesis Data Firehose).
  - Managed Apache Kafka using [[msk]] (Amazon MSK & MSK Connect).
  - SaaS application ingestion using [[appflow]] (Salesforce, ServiceNow, Slack).

### Task Statement 1.2: Transform and process data
- **ETL/ELT Engine Selection**:
  - Serverless Spark processing using [[glue]] ETL jobs (PySpark, Scala) and [[glue]] DataBrew.
  - Distributed cluster processing using [[emr]] (Spark, Hive, Presto, EMR Serverless, EMR on EKS).
  - Light event-driven transformations using [[lambda]] (< 15 mins).
  - Containerized batch compute & non-Spark workloads using [[batch]] (Spot allocation, Docker images).
  - Container microservices & Kubernetes pipelines using [[ecr-ecs-eks]] (ECS Fargate, EKS).
  - Spot Instance topologies & Graviton price-performance optimization using [[ec2-and-graviton]].
- **Data Transformation Practices**:
  - Converting raw formats (CSV, JSON) into optimized columnar formats ([[data-formats-and-compression]] — Parquet, ORC).
  - Applying partition schemes ([[data-modeling-and-partitioning]]) for query performance.

### Task Statement 1.3: Orchestrate data processing workflows
- **State Machine Orchestration**:
  - Complex multi-step workflows using [[step-functions]] (Standard vs Express Workflows).
- **DAG Workflow Orchestration**:
  - Programmatic workflow management using Apache Airflow on [[mwaa-airflow]] (DAGs, Operators, Sensors).

---

## 🛠️ Essential AWS Services in Domain 1

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS Glue** | Serverless ETL & Crawlers | Transform data in S3 to Parquet; catalog schemas automatically | [[glue]] |
| **Amazon Kinesis** | Streaming Ingestion | Near real-time ingestion to S3/Redshift/OpenSearch | [[kinesis]] |
| **Amazon MSK** | Apache Kafka | Open-source streaming compatibility with low latency | [[msk]] |
| **AWS Lambda** | Event-Driven Compute | Micro-batch processing, file upload triggers from S3 | [[lambda]] |
| **AWS Batch** | Containerized Batch Compute | Non-Spark batch processing (> 15 mins), Spot array jobs | [[batch]] |
| **Amazon ECR, ECS & EKS** | Container Orchestration | Docker registries, Fargate serverless containers, EMR on EKS | [[ecr-ecs-eks]] |
| **Amazon EC2 & Graviton** | Big Data Compute Infrastructure | Spot checkpointing, EMR node mapping, Graviton Arm pricing | [[ec2-and-graviton]] |
| **AWS Step Functions** | Workflow Orchestration | Visual state machine for ETL pipelines with error handling | [[step-functions]] |
| **Amazon MWAA** | Airflow DAG Orchestration | Complex python-defined dependency workflows | [[mwaa-airflow]] |
| **AWS AppFlow** | SaaS Integration | Secure data flow from Salesforce, ServiceNow to S3/Redshift | [[appflow]] |
| **AWS DMS & SCT** | Database Migration & CDC | Heterogeneous/homogeneous DB replication into S3/Redshift | [[dms-and-sct]] |
| **AWS DataSync & Snow** | File Transfer & Edge Devices | High-speed network transfer & offline multi-TB/PB migration | [[datasync-and-snow]] |
| **AWS Data Exchange** | 3rd-Party Data Marketplace | S3 export, Redshift zero-ETL querying, managed APIs | [[data-exchange]] |
| **AWS Transfer Family** | Managed SFTP/FTPS | B2B vendor file exchange directly into S3 and EFS | [[transfer-family]] |
| **Application Discovery & MGN** | Discovery & Server Rehost | Plan migration waves and automated block-level server rehosting | [[application-discovery-and-mgn]] |



---

## ⚡ High-Yield Exam Scenarios for Domain 1

> [!IMPORTANT]
> **Stream vs Batch Selection**:
> - If requirement is **real-time ingestion with custom transformation logic and retention up to 365 days**: Choose [[kinesis]] (Kinesis Data Streams).
> - If requirement is **zero-code streaming direct to S3, Redshift, or OpenSearch with micro-batching**: Choose [[kinesis]] (Kinesis Data Firehose).
> - If requirement is **open-source Kafka ecosystem / custom producers**: Choose [[msk]].

> [!TIP]
> **Glue vs EMR Selection**:
> - Choose [[glue]] for **serverless ETL, AWS-native catalog integration, dynamic frames, and minimal infrastructure management**.
> - Choose [[emr]] when needing **custom open-source Spark/Hadoop libraries, fine-grained cluster tuning, long-running cluster efficiency, or EMR Serverless**.

---

## 📌 Checklist for Domain 1
- [ ] Review slide pages: 266-312 (Migration & Compute) and 331-459 (Analytics & Streaming) in [[AWSCertifiedDataEngineerSlides.pdf]]
- [ ] Complete service notes: [[glue]], [[kinesis]], [[lambda]], [[step-functions]], [[mwaa-airflow]]
- [ ] Review data formats: [[data-formats-and-compression]]
