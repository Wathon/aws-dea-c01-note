---
title: AWS Glue Schema Registry
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - streaming
date: 2026-08-15
---

# 🧬 AWS Glue Schema Registry

- **Category**: Analytics / Streaming Data Governance
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-schema-registry.md)
- **Primary Use Case**: Centralized discovery and control of data schemas for streaming applications (Kafka, Kinesis).
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[msk-kafka]]` | `[[kinesis]]`

---

## 1. High-Level Summary

**AWS Glue Schema Registry** provides a central repository to discover, control, and evolve data stream schemas. When building streaming applications (e.g., using Amazon MSK / Apache Kafka, Amazon Kinesis Data Streams, or Apache Flink), data producers and consumers need to agree on the format of the data being sent. The Schema Registry enforces this contract, ensuring that downstream systems do not break when data structures change.

---

## 2. Core Capabilities

### 1. Schema Validation (Preventing Bad Data)
- The registry validates each incoming message from producers against the registered schema.
- If a producer attempts to send a message with an invalid or unexpected schema, it is rejected *before* it enters the stream, preventing downstream consumer crashes.

### 2. Schema Evolution
Data changes over time. The registry allows you to configure **compatibility modes** for schema evolution:
- **Backward Compatibility**: Consumers using the new schema can read data written by producers using the old schema.
- **Forward Compatibility**: Consumers using the old schema can read data written by producers using the new schema.
- **Full Compatibility**: Both backward and forward compatibility are enforced.

### 3. Data Compression & Cost Savings
- Because the schema is stored centrally in the registry, producers do not need to embed the full schema definition in every single message (unlike traditional JSON payloads).
- Instead, the message payload only contains the data and a tiny schema ID, which significantly reduces network bandwidth and storage costs.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Prevent bad records from entering a Kafka/Kinesis stream due to changing data formats"** $\rightarrow$ **AWS Glue Schema Registry**.
> - **"Ensure backward compatibility for an evolving Avro schema in Amazon MSK"** $\rightarrow$ **AWS Glue Schema Registry**.
> - **"Reduce network bandwidth and payload size for streaming messages"** $\rightarrow$ **Use AWS Glue Schema Registry so schemas are not embedded in every message payload**.

---

## 📌 Related Notes
- `[[msk-kafka]]` — Amazon Managed Streaming for Apache Kafka
- `[[kinesis]]` — Amazon Kinesis Data Streams
- `[[glue-data-catalog]]` — Glue Metadata Catalog
