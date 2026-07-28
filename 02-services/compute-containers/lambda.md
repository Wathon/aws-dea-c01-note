---
title: AWS Lambda
type: aws-service
category: Compute
tags:
  - aws/service
  - dea-c01
  - compute/lambda
date: 2026-07-28
---

# ⚡ AWS Lambda (Serverless Compute)

- **Category**: Compute
- **Primary Use Case**: Event-driven serverless data processing, micro-batching, light ETL, event triggers.
- **Slide Reference**: Pages 286–312 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-1-ingestion-and-processing]]

---

## 1. High-Level Summary
AWS Lambda is a serverless compute service that runs code in response to events and automatically manages underlying compute resources. In data engineering, Lambda serves as the event glue connecting data lakes, streaming queues, and automated workflows.

---

## 2. Key Limits & Technical Specifications

- **Max Timeout**: **15 minutes (900 seconds)** per invocation!
- **Memory Allocation**: 128 MB to 10,240 MB (10 GB) (CPU scales proportionally with memory).
- **Ephemeral Storage (`/tmp`)**: **512 MB up to 10,240 MB (10 GB)** configurable storage space for temporary file caching during execution.
- **Deployment Package Size**: 50 MB zipped, 250 MB unzipped (or up to 10 GB container image via ECR).

---

## 3. Lambda Event Sources & Execution Models

1. **Synchronous Invocation**: API Gateway, CloudFront, Kinesis Data Firehose transformation.
2. **Asynchronous Invocation**: S3 Event Notifications, SNS, EventBridge. Automatically retries twice on failure before sending to **Dead Letter Queue (DLQ)** or **Lambda Destination**.
3. **Event Source Mapping (Polling)**: Kinesis Data Streams, DynamoDB Streams, SQS queues. Lambda polls the stream/queue on your behalf and invokes the function.

---

## 4. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **When NOT to use Lambda**:
> - If job execution time exceeds **15 minutes** or requires heavy distributed cluster memory: Choose [[glue]] ETL or [[emr]] instead!
> - **Loading Data into Redshift**: Do NOT process large files line-by-line inside Lambda and insert to Redshift. Use Lambda to trigger Redshift `COPY` command or [[glue]] instead!

---

## 📌 Related Notes
- [[s3]] — S3 Event notification triggers
- [[sqs-and-sns]] — SQS DLQs and SNS event fanout
- [[kinesis]] — Stream processing with Lambda
