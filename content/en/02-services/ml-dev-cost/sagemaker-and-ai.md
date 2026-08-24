---
title: Amazon SageMaker & AWS AI Services
type: aws-service
category: Machine Learning
tags:
  - aws/service
  - dea-c01
  - ml/sagemaker
date: 2026-07-28
---

# 🤖 Amazon SageMaker & AWS AI Services for Data Engineers

- **Category**: Machine Learning
- **Primary Use Case**: Data preparation (Data Wrangler), feature management (Feature Store), dataset labeling (Ground Truth), generative AI (Amazon Bedrock, Amazon Q Business).
- **Slide Reference**: Pages 671–741 in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- **Hub Links**: [[en/index|index]] | [[en/00-hub/service-catalog|service-catalog]] | [[en/01-domains/domain-1-ingestion-and-processing|domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
Data engineers provide cleaned, structured feature sets for machine learning models. AWS provides **Amazon SageMaker** data components and managed AI services (Comprehend, Rekognition, Textract, Bedrock, Amazon Q Business) that integrate into data engineering pipelines.

---

## 2. Key Component Breakdown

### 1. SageMaker Components
- **SageMaker Data Wrangler**: Graphical interface to import, prepare, transform, and analyze data for ML directly from S3, Athena, Redshift, or Snowflake.
- **SageMaker Feature Store**: Central repository to store, update, retrieve, and share ML features across teams. Supports **Online Store** (low latency retrieval for inference) and **Offline Store** (historical features in S3 for batch training).
- **SageMaker Ground Truth**: Managed data labeling service using automated ML labeling or human annotators (via Amazon Mechanical Turk or private teams).

### 2. High-Level AWS AI Services
- **Amazon Comprehend**: Natural Language Processing (NLP) — sentiment analysis, topic modeling, PII entity extraction in text.
- **Amazon Textract**: Automated document text & table extraction from PDFs/scans.
- **Amazon Rekognition**: Image & video analysis (object detection, facial recognition).
- **Amazon Bedrock**: Serverless access to Leading Foundation Models (Generative AI).
- **Amazon Q Business**: Generative AI assistant configured over corporate enterprise data sources (S3, Salesforce, SharePoint).

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Centralized ML Feature Sharing**: Choose **Amazon SageMaker Feature Store**.
> - **Extracting Tables & Form Fields from Scanned PDF Invoices**: Choose **Amazon Textract**.
> - **Extracting PII Entities from Free-Form Text Documents**: Choose **Amazon Comprehend**.

---

## 📌 Related Notes
- [[en/02-services/storage/s3/s3|s3]] — Storing offline feature data in S3
- [[en/02-services/database/redshift|redshift]] — Redshift ML integration
