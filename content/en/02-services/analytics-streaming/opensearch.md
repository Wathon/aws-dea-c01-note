---
title: Amazon OpenSearch Service
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/opensearch
date: 2026-07-28
---

# 🔍 Amazon OpenSearch Service

- **Category**: Analytics / Search
- **Primary Use Case**: Real-time search, log analytics, vector search, unstructured data index.
- **Slide Reference**: Pages 460–478 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-2-data-store-management]]

---

## 1. High-Level Summary
Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) is a fully managed search and analytics engine used for log analytics, real-time application monitoring, text search, and vector search for ML applications.

---

## 2. Key Architecture Concepts
- **Index, Documents & JSON**: Data stored as JSON documents inside an index.
- **Shards & Replicas**: Primary shards for write/read parallelism; replica shards for high availability and query throughput.
- **Storage Tiering**: Hot Storage (SSD) -> UltraWarm Storage (S3-backed) -> Cold Storage (archived indices).
- **OpenSearch Serverless**: Decouples compute and storage to run search workloads without cluster sizing.

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Log Analysis Pipeline**: Route logs from CloudWatch / Kinesis Data Firehose -> **Amazon OpenSearch Service** -> OpenSearch Dashboards (Kibana) for real-time visualization.
> - **UltraWarm Tier**: Use UltraWarm for cost savings on historical log retention requiring occasional interactive querying.

---

## 📌 Related Notes
- [[kinesis]] — Firehose to OpenSearch destination
- [[cloudwatch-and-eventbridge]] — CloudWatch log stream subscription
