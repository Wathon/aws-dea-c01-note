---
title: High-Frequency DEA-C01 Exam Scenarios & Traps
type: exam-tip
tags:
  - exam-tip
  - dea-c01
  - scenarios
date: 2026-07-28
---

# 🎯 High-Frequency DEA-C01 Exam Scenarios & Traps

Top high-frequency scenario patterns and traps compiled directly from the AWS Certified Data Engineer Associate course material.

---

## 🔑 Top 10 Exam Decision Patterns

### 1. The "Lowest Operational Overhead" Rule
- If the question asks for a solution with **least operational effort**, always prefer **Serverless** native AWS services over managing EC2 clusters!
  - Choose [[en/02-services/analytics-streaming/athena/athena|athena]] over setting up Presto on EC2.
  - Choose [[en/02-services/analytics-streaming/glue/glue|glue]] ETL over managing custom Spark on EC2.
  - Choose [[en/02-services/analytics-streaming/kinesis/kinesis|kinesis]] Data Firehose over custom consumer EC2 instances.

### 2. The "Glue Data Quality (DQDL)" Pattern
- If requirement asks to validate incoming dataset quality (e.g. non-null emails, valid ranges) before loading to data warehouse without writing custom code -> Choose **AWS Glue Data Quality**.

### 3. The "Incremental S3 Processing" Pattern
- If Glue job processes S3 files periodically and needs to process **only new files without reprocessing old ones** -> Enable **Glue Job Bookmarks**.

### 4. The "Single-Digit Millisecond Latency for S3 Analytics" Pattern
- If requirement asks for sub-millisecond or single-digit millisecond latency for S3 data lake analytics -> Choose **S3 Express One Zone**.

### 5. The "Redshift COPY Command Optimization" Pattern
- Never load data into Redshift using individual SQL `INSERT`s or single huge files. Always use `COPY` from S3 with files **split into multiples of the cluster slice count** and compressed in **Parquet** or **Gzip**.

### 6. The "S3 Bucket Encryption Enforcement" Pattern
- To enforce encryption for all uploads to an S3 bucket via policy: Add a Bucket Policy that **denies (`Effect: Deny`) `s3:PutObject` if `s3:x-amz-server-side-encryption` header is missing** or if `aws:SecureTransport` is false.

### 7. The "KMS Throttling on Large Datasets" Pattern
- When scanning millions of S3 objects encrypted with `SSE-KMS` causes KMS rate limit errors -> Enable **S3 Bucket Keys** to reduce KMS requests by up to 99%.

### 8. The "WORM Compliance" Pattern
- Strict regulatory requirement preventing ANY user (including root) from deleting S3 objects -> Choose **S3 Object Lock in Compliance Mode**.

### 9. The "DynamoDB CDC Stream" Pattern
- Real-time downstream reaction to database item inserts/updates in DynamoDB -> Use **DynamoDB Streams** triggering an AWS Lambda function.

### 10. The "Redshift Cross-Account Sharing" Pattern
- Sharing live Redshift tables across AWS accounts without copying data files -> Use **Redshift Data Sharing**.

---

## 📌 Master Hub Link
Return to main hub: [[en/index|index]]
