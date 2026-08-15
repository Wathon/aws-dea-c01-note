---
title: Amazon MSK (Managed Streaming for Apache Kafka)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/kafka
date: 2026-07-28
---

# ☕ Amazon MSK (Managed Streaming for Apache Kafka)

- **Category**: Analytics / Streaming
- **Primary Use Case**: Fully managed open-source Apache Kafka clusters, open-source compatibility.
- **Slide Reference**: Pages 450–459 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[kinesis]]

---

## 1. High-Level Summary
Amazon MSK is a fully managed service that makes it easy to build and run applications that use Apache Kafka to process streaming data without needing Apache Kafka infrastructure management expertise.

---

## 2. Key MSK Features & Ecosystem

1. **Open-Source Compatibility**: Compatible with native Apache Kafka APIs, Kafka Connect, and Schema Registry.
2. **MSK Connect**: Serverless component to run Kafka Connect sinks/sources (e.g. streaming data from MSK to S3 or OpenSearch) without managing infrastructure.
3. **MSK Serverless**: Automatically provisions and scales capacity based on stream traffic.
4. **Security**: IAM Authentication, TLS encryption in transit, KMS encryption at rest, Kafka ACLs.

---

## 3. Kinesis vs Amazon MSK Decision Matrix

| Feature | Amazon Kinesis Data Streams | Amazon MSK (Apache Kafka) |
| --- | --- | --- |
| **Ecosystem** | AWS-Native APIs & SDKs | Open-Source Apache Kafka APIs |
| **Max Record Size** | **1 MB** per record | **8 MB+** (configurable) |
| **Retention** | Up to 365 days | Unlimited (bounded only by storage) |
| **Use Case** | AWS-native serverless streaming | Existing Kafka applications or multi-cloud open-source strategy |

---

## 📌 Related Notes
- [[kinesis]] — Kinesis Data Streams vs MSK
- [[s3]] — MSK Connect S3 Sink
