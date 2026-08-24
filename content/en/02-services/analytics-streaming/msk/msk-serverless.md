---
title: Amazon MSK Serverless Architecture, Capacity & Limits
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/msk
  - serverless-kafka
  - auto-scaling
  - cost-optimization
date: 2026-08-19
---

# ⚡ Amazon MSK Serverless Architecture, Capacity & Limits

- **Category**: Analytics / Serverless Streaming Architecture
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/msk/msk-serverless)
- **Primary Use Case**: Running Apache Kafka workloads with zero infrastructure management, automatic scaling for variable traffic, and pay-for-throughput billing.
- **Slide Reference**: Pages 450–459 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[index]]` | `[[msk]]` | `[[msk-cluster-architecture]]` | `[[kinesis-data-streams]]`

---

## 1. High-Level Summary

**Amazon MSK Serverless** is a serverless cluster type for Amazon Managed Streaming for Apache Kafka that automatically provisions and scales compute and storage resources in response to streaming throughput.

With MSK Serverless, data engineers no longer need to size broker instances, configure EBS volume auto-scaling, or rebalance partitions manually across broker nodes.

```mermaid
graph TD
    subgraph TrafficFlow["Variable & Spiky Traffic Stream"]
        T1["Low Traffic<br/>(2 MB/s Ingress)"] --> AutoScale
        T2["Peak Spikes<br/>(150 MB/s Ingress)"] --> AutoScale
    end

    subgraph ServerlessEngine["Amazon MSK Serverless Engine"]
        AutoScale["Automated Compute & Storage Scaling<br/>(Zero Broker Management)"]
        IAM_Auth["Mandatory AWS IAM Access Control<br/>(aws-msk-iam-auth)"]
        AutoScale --- IAM_Auth
    end

    subgraph TargetVPC["Customer VPC Private Subnets"]
        ENIs["Multi-AZ Serverless ENI Endpoints<br/>(Private Subnets Only)"]
    end

    AutoScale --> ENIs
    ENIs --> App["Consumer Applications (Lambda / ECS / EC2)"]

    classDef traffic fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;
    classDef srv fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a;
    classDef vpc fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;

    class T1,T2 traffic;
    class AutoScale,IAM_Auth srv;
    class ENIs,App vpc;
```

---

## 2. Technical Capabilities & Quota Limits

Understanding the operational limits of MSK Serverless is essential for architectural validation on the DEA-C01 exam:

| Operational Metric | Amazon MSK Serverless Limits |
| :--- | :--- |
| **Max Write Throughput (Ingress)** | **Up to 200 MB / second** per cluster (up to 5 MB/s per partition). |
| **Max Read Throughput (Egress)** | **Up to 400 MB / second** per cluster (up to 10 MB/s per partition). |
| **Max Partitions per Cluster** | **Up to 2,400 partitions** per cluster. |
| **Max Message Payload Size** | **1 MB** default (up to 8 MB with client-side compression). |
| **Data Retention** | Up to **1 day (24 hours)** default; configurable up to **30 days**. |
| **Authentication Requirement** | **AWS IAM Access Control ONLY** (`aws-msk-iam-auth`). SASL/SCRAM and mTLS are unsupported. |
| **Network Access** | **Private VPC subnets ONLY**. Public endpoints are not supported. |

---

## 3. MSK Serverless vs. MSK Provisioned vs. Kinesis On-Demand

```mermaid
graph TD
    Q1{"Do you require Open-Source Apache Kafka APIs?"}

    Q1 -->|"No (AWS-Native Ecosystem Preferred)"| ChooseKDS["Amazon Kinesis Data Streams (On-Demand Mode)<br/>• 100% Serverless<br/>• Auto-scaling shards<br/>• Up to 365-day replay"]
    Q1 -->|"Yes (Kafka Client Compatibility Required)"| Q2{"Is Streaming Throughput Predictable or Spiky / Variable?"}

    Q2 -->|"Unpredictable / Spiky / Low Maintenance"| ChooseMSK_S["Amazon MSK Serverless<br/>• Pay per MB and partition-hour<br/>• Zero broker sizing<br/>• IAM Authentication"]
    Q2 -->|"Predictable / High Volume / Custom Configs"| ChooseMSK_P["Amazon MSK Provisioned<br/>• Custom broker sizing (Graviton m7g)<br/>• Custom Kafka configs<br/>• Tiered Storage enabled"]

    classDef kds fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;
    classDef msks fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef mskp fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;

    class ChooseKDS kds;
    class ChooseMSK_S msks;
    class ChooseMSK_P mskp;
```

---

## 4. Cost Model & Billing Dimensions

Amazon MSK Serverless eliminates fixed EC2 broker costs and bills based on actual resource consumption across four distinct dimensions:
1. **Cluster Base Hours**: Fixed hourly charge for running the serverless cluster abstraction.
2. **Partition Hours**: Hourly charge per active partition.
3. **Data Ingress & Egress**: Per-GB pricing for data written to and read from the cluster.
4. **Storage GB-Hours**: Per-GB storage fees for data retained within the topic retention window.

---

## 5. DEA-C01 Exam Essentials

> [!IMPORTANT]
> **Key Exam Decision Triggers for MSK Serverless**:
>
> - **"Spiky Kafka Workloads with No Operational Overhead"** $\rightarrow$ Choose **Amazon MSK Serverless**.
> - **"Mandatory Security Configuration for MSK Serverless"** $\rightarrow$ Producer and consumer clients must authenticate using **AWS IAM Access Control** (`software.amazon.msk.auth.iam.IAMLoginModule`).
> - **"Public Access Required"** $\rightarrow$ MSK Serverless **does not support public endpoints**. If internet clients must connect directly, use **MSK Provisioned** with public brokers or front the cluster with an API Gateway / Network Load Balancer.

---

## 📌 Related Notes
- `[[msk]]` — Amazon MSK Master Hub
- `[[msk-cluster-architecture]]` — MSK Provisioned Clusters & Brokers
- `[[msk-security-and-monitoring]]` — IAM Authentication & Kafka ACLs
- `[[kinesis-data-streams]]` — Kinesis On-Demand Mode Comparison
