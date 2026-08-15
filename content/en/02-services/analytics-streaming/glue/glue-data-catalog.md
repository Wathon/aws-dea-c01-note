---
title: AWS Glue Data Catalog
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - metadata
date: 2026-08-15
---

# 📖 AWS Glue Data Catalog

- **Category**: Analytics / Metadata Management
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-data-catalog.md)
- **Primary Use Case**: Centralized Hive-compatible Metastore for S3 Data Lakes, Athena, EMR, and Redshift Spectrum.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[athena]]` | `[[lake-formation]]`

---

## 1. High-Level Summary

The **AWS Glue Data Catalog** is a managed, centralized, Apache Hive-compatible metastore. In the AWS ecosystem, it acts as an index to the location, schema, and runtime metrics of your data. Instead of keeping metadata scattered across different systems, services like **Amazon Athena**, **Amazon EMR**, and **Amazon Redshift Spectrum** seamlessly integrate with the Glue Data Catalog to query data sitting in S3.

---

## 2. Core Concepts

### 1. Databases and Tables
- **Databases**: Logical groupings of tables in the catalog.
- **Tables**: Metadata definitions that represent the underlying data. A table specifies the data location (e.g., an S3 URI), the schema (column names and data types), and the format (e.g., Parquet, JSON, CSV).

### 2. Partition Indexes
- To speed up Amazon Athena queries on highly partitioned S3 data, you can create **Partition Indexes** on the Glue Data Catalog table.
- Instead of Athena scanning the entire list of partitions (which can take minutes if there are millions of partitions), the partition index allows Athena to quickly retrieve only the relevant partitions.

### 3. Integration with Lake Formation
- The Data Catalog integrates closely with `[[lake-formation]]`, which provides fine-grained (column-level and row-level) access control over the tables and databases defined in the catalog.

### 4. Cross-Account Access
- The Data Catalog can be shared across AWS accounts using **AWS Resource Access Manager (RAM)** or Lake Formation, enabling a centralized "Data Mesh" metadata architecture.

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Centralized metastore to store schema definitions for Athena, Redshift Spectrum, and EMR"** $\rightarrow$ **AWS Glue Data Catalog**.
> - **"Hive-compatible metastore on AWS"** $\rightarrow$ **AWS Glue Data Catalog**.
> - **"Speed up Athena queries on an S3 table with millions of partitions"** $\rightarrow$ **Create a Partition Index in the Glue Data Catalog**.
> - **"Apply column-level security to a Data Catalog table"** $\rightarrow$ **AWS Lake Formation**.

---

## 📌 Related Notes
- `[[glue]]` — AWS Glue Overview
- `[[glue-crawlers]]` — Automating Data Catalog Population
- `[[athena]]` — Querying the Data Catalog
- `[[lake-formation]]` — Securing the Data Catalog
