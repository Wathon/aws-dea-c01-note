---
title: Specialized AWS Databases (ElastiCache, Keyspaces, Neptune, Timestream)
type: aws-service
category: Database
tags:
  - aws/service
  - dea-c01
  - database/specialized
date: 2026-07-28
---

# 🔮 Specialized AWS Databases

- **Category**: Database
- **Primary Use Case**: In-memory caching, Cassandra workloads, Graph analytics, Time-Series telemetry.
- **Slide Reference**: Pages 214–219 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-2-data-store-management]]

---

## 1. High-Level Summary
AWS offers purpose-built specialized database engines tailored for specific data access patterns outside traditional SQL and key-value paradigms.

---

## 2. Specialized Database Summary Matrix

| Database Engine | Type | Primary Protocol / Language | High-Yield Exam Use Case |
| --- | --- | --- | --- |
| **Amazon ElastiCache** | In-Memory Cache | Redis / Memcached | Microsecond read caching for databases & session stores |
| **Amazon MemoryDB** | Ultra-Fast DB | Redis API | Redis-compatible durable in-memory primary database |
| **Amazon Keyspaces** | Serverless Cassandra | CQL (Cassandra Query Language) | Managed Apache Cassandra migration with zero infra overhead |
| **Amazon Neptune** | Graph Database | Apache TinkerPop Gremlin / SPARQL | Social graphs, fraud detection networks, recommendation relationships |
| **Amazon Timestream** | Time-Series Database | SQL-compatible | IoT telemetry, clickstreams, metrics, automated time-based tiering |

---

## 3. DEA-C01 Exam Decision Triggers

> [!IMPORTANT]
> - **IoT Telemetry / Metric Storage with automated lifecycle to magnetic storage**: Choose **Amazon Timestream**.
> - **Relationship Graphing (Fraud Networks / Knowledge Graphs)**: Choose **Amazon Neptune**.
> - **Migrating Apache Cassandra workload without rearchitecting**: Choose **Amazon Keyspaces**.

---

## 📌 Related Notes
- [[dynamodb]] — Serverless Key-Value store
- [[kinesis]] — Streaming metrics into Timestream
