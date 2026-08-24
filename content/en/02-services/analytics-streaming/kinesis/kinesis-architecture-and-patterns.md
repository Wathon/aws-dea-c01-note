---
title: Kinesis Streaming Architectures, Design Patterns & Decision Matrices
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/kinesis
  - streaming-architecture
  - deduplication
  - decision-matrix
  - end-to-end-pipeline
date: 2026-08-18
---

# 🏗️ Kinesis Streaming Architectures, Design Patterns & Decision Matrices

- **Category**: Analytics / Streaming Architecture & System Design
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/kinesis/kinesis-architecture-and-patterns)
- **Primary Use Case**: Designing end-to-end streaming data pipelines, implementing record deduplication, isolating poison pills, and choosing between KDS, Firehose, MSK, and SQS.
- **Slide Reference**: Pages 414–459 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[index]]` | `[[kinesis]]` | `[[kinesis-data-streams]]` | `[[kinesis-firehose]]` | `[[kinesis-apache-flink]]` | `[[msk]]`

---

## 1. High-Level Summary

Real-time data engineering on AWS combines multiple services to satisfy two distinct streaming workloads: **Low-Latency Stream Processing** (sub-second alerting, stateful anomaly detection) and **Continuous Managed Lakehouse Ingestion** (columnar Parquet micro-batch delivery into S3).

This guide provides end-to-end enterprise reference architectures, deduplication strategies, and a multi-dimensional decision matrix covering the complete AWS streaming and messaging landscape.

```mermaid
graph LR
    subgraph IngestionLayer["(1) Ingestion Layer"]
        IoT["IoT Sensors / Mobile Apps"] --> KDS["Amazon Kinesis Data Streams<br/>(Durable Multi-Consumer Stream)"]
    end

    subgraph FastPath["(2) Real-Time Speed Layer (Sub-Second)"]
        KDS --> Flink["Managed Service for Apache Flink<br/>(Stateful Anomaly Detection)"]
        Flink --> RealtimeDB[("Amazon DynamoDB<br/>(Hot State Store)")]
        Flink --> SNS["Amazon SNS (Alerts)"]
    end

    subgraph ServingPath["(3) Lakehouse Serving Layer (Near Real-Time)"]
        KDS --> KDF["Amazon Data Firehose<br/>• Dynamic S3 Partitioning<br/>• Parquet Format Conversion"]
        GlueMeta["AWS Glue Data Catalog"] --> KDF
        KDF --> S3[("Amazon S3 Data Lake<br/>(s3://lake/year=2026/...)")]
        S3 --> Athena["Amazon Athena (SQL Analytics)"]
        Athena --> QuickSight["Amazon QuickSight (BI Dashboards)"]
    end

    classDef ing fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef fast fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef serve fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class IoT,KDS ing;
    class Flink,RealtimeDB,SNS fast;
    class KDF,GlueMeta,S3,Athena,QuickSight serve;
```

---

## 2. Comprehensive Streaming & Messaging Decision Matrix

| Dimension | Kinesis Data Streams (KDS) | Amazon Data Firehose (KDF) | Amazon MSK (Apache Kafka) | Amazon SQS | Amazon SNS |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Delivery Model** | Streaming partition log (pull / push via EFO). | Automated streaming delivery (micro-batch push). | Distributed publish-subscribe topic partitions. | Point-to-point message queue. | Publish-subscribe fan-out topic. |
| **Target Latency** | **70 ms – 200 ms** (sub-second). | **60 s – 900 s** (near real-time). | **< 20 ms** (sub-second). | **Sub-second** (pull). | **Sub-second** (push). |
| **Data Retention & Replay** | **24 hours to 365 days** (full replay). | **None** (in-flight buffer only). | **Configurable** (hours to years). | **1 minute to 14 days** (deleted upon read). | **None** (no message storage). |
| **Message Ordering** | Strictly ordered **per Partition Key**. | Micro-batched; order not guaranteed across batches. | Strictly ordered **per Partition**. | Ordered only in **SQS FIFO**; unordered in Standard. | Ordered only in **SNS FIFO**. |
| **Max Payload Size** | **1 MB** | **1 MB** (or 10 MB with Lambda) | **1 MB** (configurable up to multi-MB) | **256 KB** (2 GB with S3 Extended Client) | **256 KB** |
| **Scaling Mechanism** | Shard scaling (Provisioned or On-Demand). | Fully serverless (auto-scales). | Broker node instance types & storage expansion. | Virtually unlimited automatic scaling. | Virtually unlimited automatic scaling. |
| **Primary Use Case** | Multi-consumer custom stream processing & replay. | Direct ingestion to S3/Redshift with Parquet format conversion. | Enterprise Kafka migration, custom Kafka Connect plugins. | Decoupling microservices & background worker queues. | Event notifications, fan-out to SQS/Lambda/Email. |

---

## 3. Data Deduplication in Streaming Pipelines

Because Kinesis operates on an **At-Least-Once Delivery** guarantee, network retries by producers or worker restarts can introduce duplicate records.

```mermaid
graph TD
    Stream["Kinesis Data Stream (At-Least-Once Delivery)"] --> Consumer["Consumer Application (KCL / Lambda)"]
    Consumer --> Extract["Extracts Unique 'transaction_id' from Payload"]
    Extract --> CheckDDB{"DynamoDB Lookup<br/>PutItem with Condition: attribute_not_exists(transaction_id)"}

    CheckDDB -->|"Transaction ID is NEW ✅"| Process["Process Record & Write to Target"]
    CheckDDB -->|"Transaction ID Exists (ConditionalCheckFailedException)"| Drop["Discard Duplicate Record ✅"]

    Process --> SetTTL["Set DynamoDB TTL = 7 Days (Auto Cleanup)"]

    classDef cond fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef proc fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;
    classDef drop fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;

    class CheckDDB cond;
    class Process,SetTTL proc;
    class Drop drop;
```

### Deduplication Strategies:
1. **Idempotent Destination Writes**: Use primary key upserts in DynamoDB (`PutItem`) or `MERGE INTO` in Apache Iceberg / Delta Lake.
2. **DynamoDB State Tracker**: Track processed message UUIDs in a dedicated DynamoDB table using conditional writes (`attribute_not_exists(id)`). Attach a **Time to Live (TTL)** of 7 days to purge historical keys automatically.
3. **Apache Flink Stateful Deduplication**: Flink maintains an in-memory RocksDB state bounded by a time window (e.g. 1 hour) to filter duplicates before emitting downstream.

---

## 4. Isolating Poison Pills (Corrupted Records)

A malformed or unparseable record ("poison pill") must never be allowed to stall an entire stream pipeline:

```mermaid
graph TD
    KDS["Kinesis Shard"] --> LambdaESM["AWS Lambda Event Source Mapping"]
    LambdaESM --> Config{"Lambda Error Configuration"}

    Config -->|"BisectBatchOnFunctionError = True"| Bisect["Recursively splits failing batch in half"]
    Config -->|"MaximumRetryAttempts = 2"| Retry["Limits retries before discarding"]
    Config -->|"On-Failure Destination"| SQS_DLQ["Amazon SQS Dead-Letter Queue (Auditing & Fixes)"]

    Bisect --> SQS_DLQ

    classDef kds fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef conf fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef dlq fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;

    class KDS kds;
    class Config,Bisect,Retry conf;
    class SQS_DLQ dlq;
```

---

## 5. DEA-C01 Scenario Decision Guide

> [!IMPORTANT]
> **Key Exam Decision Triggers for Streaming Architecture**:
>
> - **"Need real-time sub-second anomaly detection AND automated delivery to an S3 Parquet data lake"** $\rightarrow$ Ingest via **Kinesis Data Streams**, connect **Managed Service for Apache Flink** for real-time alerts, and attach **Amazon Data Firehose** for S3 Parquet delivery.
> - **"Prevent duplicate records from causing duplicate accounting entries when processing streams"** $\rightarrow$ Implement **Idempotency keys with Amazon DynamoDB conditional writes**.
> - **"Existing infrastructure uses Apache Kafka APIs and custom Kafka Connect plugins"** $\rightarrow$ Migrate to **Amazon MSK**.
> - **"Decouple background web worker tasks where each task is processed once by a single worker and deleted"** $\rightarrow$ Use **Amazon SQS**.
> - **"Fan-out a single streaming event to 10 different subscriber queues simultaneously"** $\rightarrow$ Publish to **Amazon SNS** subscribed to multiple **Amazon SQS queues**.

---

## 📌 Related Notes
- `[[kinesis]]` — Kinesis Streaming Ecosystem Overview Hub
- `[[kinesis-data-streams]]` — KDS Ingestion & Shards
- `[[kinesis-firehose]]` — Micro-Batch Streaming Delivery
- `[[kinesis-apache-flink]]` — Real-Time Stateful Stream Processing
- `[[msk]]` — Amazon Managed Streaming for Apache Kafka
- `[[dynamodb]]` — Deduplication State Storage
