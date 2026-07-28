---
title: Amazon Managed Workflows for Apache Airflow (MWAA)
type: aws-service
category: Integration
tags:
  - aws/service
  - dea-c01
  - integration/mwaa
date: 2026-07-28
---

# 🌀 Amazon MWAA (Managed Workflows for Apache Airflow)

- **Category**: Application Integration / Orchestration
- **Primary Use Case**: Managed open-source Apache Airflow orchestration, Python DAG-based workflows, multi-cloud ETL coordination.
- **Slide Reference**: Pages 538–541 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
Amazon MWAA is a managed orchestration service for Apache Airflow that makes it easy to setup and operate end-to-end data pipelines in the cloud using Python DAGs (Directed Acyclic Graphs).

---

## 2. Architecture & Airflow Concepts
- **DAGs (Directed Acyclic Graphs)**: Python code defining tasks and their execution order. Stored in an S3 bucket configured for MWAA.
- **Operators**: Pre-built building blocks (e.g. `BashOperator`, `PythonOperator`, `GlueJobOperator`, `AthenaOperator`, `S3ToRedshiftOperator`).
- **Executors**: Celery Executor auto-scales worker nodes based on task queue workload.

---

## 3. MWAA vs Step Functions Decision Matrix

| Feature | AWS Step Functions | Amazon MWAA (Apache Airflow) |
| --- | --- | --- |
| **Workflow Definition** | JSON / Amazon States Language (ASL) | **Python Code (DAGs)** |
| **Serverless Nature** | Fully serverless (Zero compute management) | Managed Airflow environment (Workers auto-scale) |
| **Ecosystem** | AWS-Native service integration | Open-source Airflow operators & multi-cloud connectors |
| **Use Case** | AWS-native serverless state machines | Existing Airflow codebase or complex Python dependency logic |

---

## 📌 Related Notes
- [[step-functions]] — Step Functions vs MWAA
- [[glue]] — Executing Glue jobs via Airflow operators
