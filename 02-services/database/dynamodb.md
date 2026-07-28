---
title: Amazon DynamoDB
type: aws-service
category: Database
tags:
  - aws/service
  - dea-c01
  - database/dynamodb
date: 2026-07-28
---

# ⚡ Amazon DynamoDB (Serverless NoSQL Database)

- **Category**: Database (NoSQL Key-Value & Document)
- **Primary Use Case**: Low-latency single-digit millisecond operational data store, session storage, key-value lookup.
- **Slide Reference**: Pages 156–195 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-2-data-store-management]]

---

## 1. High-Level Summary
Amazon DynamoDB is a fully managed, serverless, key-value and document NoSQL database designed for single-digit millisecond performance at any scale. In data pipelines, DynamoDB is frequently used for metadata tracking, state management, change data capture (CDC), and streaming ingestion.

---

## 2. Key Architecture & Features

### Primary Keys & Secondary Indexes
- **Partition Key (PK) (Hash)**: Internal hash function determines physical partition.
- **Composite Key (PK + Sort Key (SK) / Range)**: Enables range queries on items within a partition.
- **Local Secondary Index (LSI)**:
  - Must be created at table creation time!
  - Uses same Partition Key, but different Sort Key.
  - Shares read/write capacity units with base table.
- **Global Secondary Index (GSI)**:
  - Can be created or deleted at any time!
  - Can define completely different Partition Key and Sort Key.
  - Has its own provisioned throughput capacity.

---

### DynamoDB Streams (Change Data Capture - CDC)
- Time-ordered sequence of item-level modifications (INSERTS, UPDATES, DELETES) retained for **24 hours**.
- Native trigger integration with [[lambda]] for event-driven downstream processing or updating search indices in [[opensearch]] or S3!

---

### Read Consistency & Provisioned Capacity
- **Eventually Consistent Reads** (Default): Half cost. Returns data shortly after write.
- **Strongly Consistent Reads**: Double cost. Guaranteed up to-the-second data.
- **Capacity Modes**:
  - **On-Demand**: Auto-scales based on traffic spikes. Ideal for unpredictable workloads.
  - **Provisioned**: Set RCU (Read Capacity Units) & WCU (Write Capacity Units). Cost savings with auto-scaling or reserved capacity.

---

### DynamoDB Accelerator (DAX)
- Fully managed in-memory cache for DynamoDB. Microsecond latency for read-heavy workloads. Microsecond read performance without code rewrite.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Distinctions & Keywords**:
> - **Real-time Change Data Capture (CDC) from DynamoDB**: Use **DynamoDB Streams** linked to AWS Lambda or Kinesis Data Streams.
> - **DynamoDB Table Export to S3**: Use native **S3 Export feature** (uses Glue/EMR under the hood, zero RCU consumption on live table!).
> - **Automatic item deletion after expiration**: Enable **Time To Live (TTL)** on an attribute containing Epoch timestamp.

---

## 📌 Related Notes
- [[lambda]] — Lambda consumer for DynamoDB Streams
- [[s3]] — Exporting DynamoDB to S3 Data Lake
