---
title: Amazon Kinesis Data Streams (KDS) Architecture & Ingestion
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/kinesis
  - kds
  - shards
  - partition-keys
  - kpl
date: 2026-08-18
---

# ⚡ Amazon Kinesis Data Streams (KDS) Architecture & Ingestion

- **Category**: Analytics / Real-Time Data Streaming & Ingestion
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/kinesis/kinesis-data-streams)
- **Primary Use Case**: Ingesting massive data streams with custom partition keys, sub-second latency, multi-consumer replay, and flexible capacity scaling.
- **Slide Reference**: Pages 414–435 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[en/index|index]]` | `[[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]]` | `[[en/02-services/analytics-streaming/kinesis/kinesis-consumers-and-scaling|kinesis-consumers-and-scaling]]` | `[[en/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]]`

---

## 1. High-Level Summary

**Amazon Kinesis Data Streams (KDS)** is a massively scalable, durable, real-time data streaming service. Data is ingested into a stream and structured into **Shards**. Each record within a stream contains a **Sequence Number**, a **Partition Key**, and a data payload (blob) of up to **1 MB**.

Records are durably replicated across three Availability Zones (AZs) in an AWS Region and retained for a configurable period (default **24 hours**, extendable up to **365 days**), allowing multiple downstream applications to consume and re-read data independently.

```mermaid
graph LR
    subgraph Producers["Stream Producers"]
        SDK["AWS SDK (PutRecords)"]
        KPL["Kinesis Producer Library (KPL)<br/>• Aggregation & Collection"]
        Agent["Kinesis Agent (Log Tailing)"]
    end

    subgraph KDSStream["Kinesis Data Stream (MD5 Hash Space: 0 to 2^128 - 1)"]
        subgraph Shard1["Shard 1 (Hash: 0 - 1.14e38)"]
            S1_Cap["Ingress: 1 MB/s (1,000 rec/s)<br/>Egress: 2 MB/s"]
        end
        subgraph Shard2["Shard 2 (Hash: 1.14e38 - 2.28e38)"]
            S2_Cap["Ingress: 1 MB/s (1,000 rec/s)<br/>Egress: 2 MB/s"]
        end
        subgraph Shard3["Shard 3 (Hash: 2.28e38 - 3.40e38)"]
            S3_Cap["Ingress: 1 MB/s (1,000 rec/s)<br/>Egress: 2 MB/s"]
        end
    end

    Producers -->|"MD5(PartitionKey)"| KDSStream

    classDef prod fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef shard fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;

    class SDK,KPL,Agent prod;
    class Shard1,Shard2,Shard3 shard;
```

---

## 2. Shard Fundamentals & Capacity Limits

A **Shard** is the base throughput unit of a Kinesis Data Stream.

| Shard Dimension | Limit / Metric per Shard | Notes & DEA-C01 Implications |
| :--- | :--- | :--- |
| **Write Throughput (Ingress)** | **1 MB / second** or **1,000 records / second** | Exceeding either limit triggers `ProvisionedThroughputExceededException`. |
| **Read Throughput (Standard Egress)** | **2 MB / second** (shared across all consumers) | Max 5 `GetRecords` API calls per second per shard. |
| **Enhanced Fan-Out (EFO Egress)** | **2 MB / second per registered consumer** | Dedicated HTTP/2 push pipeline (does not consume shared 2 MB/s). |
| **Maximum Record Size** | **1 MB** (including partition key) | Base64 encoded payload. Larger payloads must use S3 claim-check pattern. |
| **Data Retention Window** | **24 hours default** (up to **365 days / 8760 hours**) | Enables replaying historical data during application failure or backfill. |

---

## 3. Capacity Modes: Provisioned vs. On-Demand

```mermaid
graph TD
    Decision{"What is your Streaming Traffic Pattern?"}

    Decision -->|"Predictable steady volume OR predictable diurnal peaks"| Prov["Provisioned Capacity Mode<br/>• Explicitly specify number of shards<br/>• Lower cost for baseline 24/7 steady traffic<br/>• Requires manual or scheduled resharding"]
    Decision -->|"Unpredictable, spiky traffic OR unknown workload volume"| OnDem["On-Demand Capacity Mode<br/>• Zero shard management<br/>• Auto-scales from 4 MB/s up to 200 MB/s<br/>• Accommodates up to 2x peak observed volume in last 30 days"]

    classDef provStyle fill:#dbeafe,stroke:#2563eb,stroke-width:1px,color:#0f172a;
    classDef onDemStyle fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class Prov provStyle;
    class OnDem onDemStyle;
```

### 1. Provisioned Mode (Manual Capacity Planning)
- You specify the exact number of shards.
- Formula for calculating required shards:
  $$\text{Required Shards} = \max\left(\left\lceil\frac{\text{Peak Write Data Rate (MB/sec)}}{1\text{ MB/sec}}\right\rceil, \left\lceil\frac{\text{Peak Records/sec}}{1000\text{ records/sec}}\right\rceil\right)$$
- If consumer read throughput exceeds $2\text{ MB/sec}$, add shards or enable Enhanced Fan-Out.

### 2. On-Demand Mode (Automated Elastic Scaling)
- AWS automatically manages shard provisioning and scaling without downtime.
- Default baseline: **4 MB/sec** write (4,000 records/sec) and **8 MB/sec** read.
- Auto-scales dynamically up to **200 MB/sec** write and **400 MB/sec** read per stream.
- Handles traffic spikes up to **2x the previous 30-day peak** throughput instantly without throttling.

---

## 4. Partition Keys & The Hot Shard Problem

Each incoming record requires a string **Partition Key** (up to 256 characters). Kinesis applies an **MD5 hash algorithm** to map the partition key to an ordered 128-bit integer space ($0$ to $2^{128}-1$) divided among active shards.

```mermaid
graph LR
    subgraph BadPartitionKey["(1) Poor Partition Key (e.g. DeviceType = 'Sensor')"]
        K1["PartitionKey: 'Sensor'"] -->|All Hashes Map to Same Hash Range| HotShard["Shard 1 (HOT SHARD)<br/>⚠️ 1.8 MB/s (> 1 MB/s Limit)<br/>❌ ProvisionedThroughputExceeded"]
        K2["PartitionKey: 'Gateway'"] --> ColdShard["Shard 2 (COLD)<br/>0.1 MB/s (Idle)"]
    end

    subgraph GoodPartitionKey["(2) Uniform Partition Key (e.g. DeviceUUID)"]
        G1["UUID: 'a8f1-...'"] --> S1["Shard 1 (0.6 MB/s)"]
        G2["UUID: 'b4c9-...'"] --> S2["Shard 2 (0.6 MB/s)"]
        G3["UUID: 'e710-...'"] --> S3["Shard 3 (0.6 MB/s)"]
    end

    classDef hot fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;
    classDef good fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class HotShard hot;
    class S1,S2,S3 good;
```

### Hot Shard Causes and Solutions:
1. **Cause**: Low cardinality partition keys (e.g., status code, country code, or date string) route the vast majority of records to a single shard, triggering `ProvisionedThroughputExceededException` even when total stream capacity is underutilized.
2. **Solution**: Use high-cardinality keys (e.g., `user_id`, `device_id`, or `transaction_uuid`).
3. **Random Suffixing (Salting)**: If data must be partitioned by an entity that generates uneven traffic, append a random integer suffix (e.g., `device_101#rand_04`) to distribute records uniformly across hash spaces.

---

## 5. Ingestion Producers: SDK vs. KPL vs. Kinesis Agent

```mermaid
graph TD
    subgraph ProducerLandscape["Kinesis Ingestion Ecosystem"]
        direction TB
        subgraph Option1["(1) AWS SDK"]
            SDK_Desc["• PutRecord / PutRecords API<br/>• Low latency, simple integration<br/>• Synchronous, manual retries"]
        end
        subgraph Option2["(2) Kinesis Producer Library (KPL)"]
            KPL_Desc["• High-throughput C++/Java daemon<br/>• Record Aggregation (sub-records into 1MB)<br/>• Record Collection (batching PutRecords)<br/>• Asynchronous buffer queue"]
        end
        subgraph Option3["(3) Kinesis Agent"]
            Agent_Desc["• Standalone Java daemon on Linux<br/>• Auto log rotation and file tailing<br/>• Built-in KPL aggregation & retry logic<br/>• Zero custom code"]
        end
    end
```

### 1. AWS SDK (`PutRecord` and `PutRecords`)
- Direct HTTP REST API calls.
- `PutRecords` supports up to **500 records** or **5 MB** per call.
- Synchronous; returns per-record status codes (`ErrorCode` and `ErrorMessage`) to identify individual failed records for manual retry.

### 2. Kinesis Producer Library (KPL)
- Designed for maximum write throughput and cost efficiency.
- **Aggregation**: Combines multiple micro-records (e.g., 200-byte IoT records) into a single 1 MB Kinesis record.
- **Collection**: Batches multiple Kinesis records into a single `PutRecords` HTTP call to saturate shard capacity.
- **Buffering**: Configured via `RecordMaxBufferedTime` (default 100ms).
- **Caveat**: Aggregated records must be de-aggregated by consumers using the **Kinesis Client Library (KCL)** or the KPL de-aggregation library.

### 3. Kinesis Agent
- Standalone background daemon for Linux servers (EC2 or on-premises).
- Automatically monitors log directories, handles multiline log parsing, and publishes data to KDS or Firehose with built-in retry and aggregation mechanisms.

---

## 6. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Decision Triggers for Kinesis Data Streams**:
>
> - **"Stream receives `ProvisionedThroughputExceededException` but CloudWatch shows overall stream capacity is only at 30%"** $\rightarrow$ Diagnosed as a **Hot Shard** caused by a low-cardinality partition key. Fix by selecting a high-cardinality key (e.g., `device_id`) or applying random salting.
> - **"Millions of tiny 100-byte IoT records need to be ingested into KDS cost-effectively without exceeding the 1,000 records/sec per shard limit"** $\rightarrow$ Use the **Kinesis Producer Library (KPL)** to enable **Record Aggregation**.
> - **"Need to stream Linux server system and application log files directly into Kinesis without writing custom producer code"** $\rightarrow$ Install and configure the **Amazon Kinesis Agent**.
> - **"Application requires replaying streaming transactions from 30 days ago to train a machine learning model"** $\rightarrow$ Extend KDS **Data Retention Period** from 24 hours to 30 days (up to 365 days).
> - **"Unpredictable streaming traffic with sudden 10x traffic spikes that cannot tolerate manual shard management"** $\rightarrow$ Switch stream capacity mode to **On-Demand Mode**.

---

## 📌 Related Notes
- `[[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]]` — Kinesis Streaming Ecosystem Overview Hub
- `[[en/02-services/analytics-streaming/kinesis/kinesis-consumers-and-scaling|kinesis-consumers-and-scaling]]` — Standard vs. Enhanced Fan-Out & KCL
- `[[en/02-services/analytics-streaming/kinesis/kinesis-firehose|kinesis-firehose]]` — Amazon Data Firehose Pipelines
- `[[en/02-services/analytics-streaming/kinesis/kinesis-security-and-monitoring|kinesis-security-and-monitoring]]` — KMS Encryption & CloudWatch Metrics
