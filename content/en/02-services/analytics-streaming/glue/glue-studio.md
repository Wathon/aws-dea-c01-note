---
title: AWS Glue Studio
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/glue
  - visual-etl
date: 2026-08-15
---

# 🎨 AWS Glue Studio

- **Category**: Analytics / Visual ETL & Monitoring
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/glue/glue-studio.md)
- **Primary Use Case**: Authoring, running, and monitoring AWS Glue ETL jobs using a visual drag-and-drop interface.
- **Slide Reference**: Pages 331–364 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[glue]]` | `[[glue-etl-jobs]]`

---

## 1. High-Level Summary

**AWS Glue Studio** provides a graphical, drag-and-drop interface that makes it easy to create, run, and monitor AWS Glue ETL jobs. Instead of writing PySpark or Scala code from scratch, data engineers and ETL developers can visually map out their data integration pipelines. Glue Studio automatically generates the underlying PySpark or Spark Scala code on your behalf.

---

## 2. Core Capabilities

### 1. Visual Job Authoring
- **Drag-and-Drop Nodes**: Build data pipelines by connecting Source, Transform, and Target nodes.
- **Built-in Transformations**: Easily add common data manipulations like Drop Null Fields, Rename Keys, Join, Map, and Relationalize (flattening nested JSON).
- **Code Generation**: Under the hood, the visual DAG (Directed Acyclic Graph) is translated into Apache Spark code, which you can preview, modify, and save.

### 2. Job Monitoring Dashboard
- Glue Studio includes a centralized dashboard to monitor the status and performance of all AWS Glue ETL jobs.
- It displays metrics such as success/failure rates, job duration, and resource utilization across the entire AWS account.

### 3. Notebook Integration
- If custom code is needed beyond the built-in visual transforms, Glue Studio provides built-in Jupyter Notebooks. You can seamlessly switch between the visual editor and code editor.

---

## 3. Glue Studio vs. Glue DataBrew

| Feature | AWS Glue Studio | AWS Glue DataBrew |
| :--- | :--- | :--- |
| **Target Audience** | **ETL Developers / Data Engineers** | **Data Analysts / Data Scientists** |
| **Output / Artifact** | Generates PySpark / Scala **ETL Code** | Generates Data Preparation **Recipes** |
| **Complexity** | Handles complex joins, partitions, and large-scale ETL | Focuses on data cleaning, normalization, and profiling |
| **Underlying Engine** | Apache Spark | Pre-built transformations engine |

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Author and monitor Apache Spark ETL jobs using a visual, drag-and-drop interface that automatically generates PySpark code"** $\rightarrow$ **AWS Glue Studio**.
> - **"Need a central dashboard to monitor the status, execution times, and resource usage of all Glue jobs across the account"** $\rightarrow$ **AWS Glue Studio Job Monitoring**.
> - **"Business analysts need to clean data without writing code"** $\rightarrow$ *Careful! This is **Glue DataBrew**, not Glue Studio*.

---

## 📌 Related Notes
- `[[glue-etl-jobs]]` — Code-based AWS Glue ETL Jobs
- `[[glue-databrew]]` — Visual Data Preparation for Analysts
