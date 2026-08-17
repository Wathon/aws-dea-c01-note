---
title: Athena Workgroups & Cost Management
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/athena
  - governance
date: 2026-08-17
---

# 🛡️ Athena Workgroups & Cost Management

- **Category**: Analytics / Governance & Security
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/mm/02-services/analytics-streaming/athena/athena-workgroups.md)
- **Primary Use Case**: Separating query execution environments for different teams, enforcing cost limits, and isolating query histories.
- **Hub Links**: `[[index]]` | `[[athena]]` | `[[domain-5-security-and-governance]]`

---

## 1. High-Level Summary

Because Amazon Athena charges based on the amount of data scanned ($5 per TB), a poorly written query (e.g., `SELECT *` on a non-partitioned Petabyte-scale table) can accidentally cost thousands of dollars in a single run. 

**Athena Workgroups** are used to isolate users, teams, or applications, allowing administrators to enforce strict governance, track costs per team, and prevent runaway queries.

---

## 2. Core Capabilities of Workgroups

### 1. Cost Control & Data Usage Limits
- You can set a **Data Usage Control Limit** per workgroup (e.g., maximum 100 GB scanned per query).
- If a user runs a query that attempts to scan more data than the limit, Athena will **automatically cancel the query** before it incurs excessive charges.
- Limits can be set on a **per-query** basis or as a **workgroup-wide daily/hourly limit**.

### 2. Separation of Environments
- Every query runs in a specific Workgroup. 
- **Query History Isolation**: Users in the "Marketing" workgroup cannot see the query history, saved queries, or query results of the "Finance" workgroup.
- **IAM Integration**: You can use IAM policies to allow a user access only to a specific Workgroup.

### 3. Overriding Client Settings
- A workgroup can be configured to **override client-side settings**.
- For example, you can force all queries run in a specific workgroup to encrypt their result sets in S3 using a specific AWS KMS key, regardless of what the user requested.
- You can force all query results for a workgroup to be saved to a specific S3 bucket path.

### 4. CloudWatch Metrics Integration
- Workgroups automatically publish query metrics (data scanned, query execution time) to **Amazon CloudWatch**.
- This enables billing alerts and dashboards per team.

---

## 3. DEA-C01 Exam Tips & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Prevent users from running expensive queries that scan too much data"** $\rightarrow$ **Set per-query data usage limits on Athena Workgroups**.
> - **"Separate query history and saved queries between the Data Science and Marketing teams"** $\rightarrow$ **Create separate Athena Workgroups and assign IAM permissions**.
> - **"Force all query results to be encrypted with a specific KMS key"** $\rightarrow$ **Configure the Workgroup to override client-side settings for output encryption**.

---

## 📌 Related Notes
- `[[athena]]` — Athena Overview
- `[[macie]]` — S3 data discovery and protection
- `[[kms]]` — AWS Key Management Service
