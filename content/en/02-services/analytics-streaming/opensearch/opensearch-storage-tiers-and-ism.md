---
title: Amazon OpenSearch Storage Tiers & Index State Management (ISM)
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/opensearch
  - ultrawarm
  - cold-storage
  - ism-policy
  - storage-tiering
date: 2026-08-19
---

# 📦 Amazon OpenSearch Storage Tiers & Index State Management (ISM)

- **Category**: Analytics / Storage Optimization & Lifecycle Automation
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/opensearch/opensearch-storage-tiers-and-ism)
- **Primary Use Case**: Cost-effective log retention across Hot, UltraWarm, and Cold storage tiers, automated index rollovers, and defining Index State Management (ISM) lifecycle policies.
- **Slide Reference**: Pages 460–478 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[en/index|index]]` | `[[en/02-services/analytics-streaming/opensearch/opensearch|opensearch]]` | `[[en/02-services/analytics-streaming/opensearch/opensearch-cluster-architecture|opensearch-cluster-architecture]]` | `[[en/02-services/storage/s3/s3|s3]]`

---

## 1. High-Level Summary

Managing massive time-series log data in Amazon OpenSearch Service requires balancing **sub-second query performance** with **storage cost efficiency**.

Amazon OpenSearch decouples storage across three primary tiers: **Hot**, **UltraWarm** (backed by Amazon S3 with warm node caching), and **Cold Storage** (detached S3 data). **Index State Management (ISM)** automates index transitions between these tiers without manual administrative scripts.

```mermaid
graph LR
    subgraph Hot["(1) Hot Tier (Days 0 - 7)"]
        H_Node["Data Nodes (EBS gp3 SSD)<br/>• Fast Sub-Second Queries<br/>• Active Real-Time Ingestion<br/>• Full Read/Write Support"]
    end

    subgraph Warm["(2) UltraWarm Tier (Days 8 - 30)"]
        W_Node["UltraWarm Nodes (S3-Backed)<br/>• Interactive Read-Only Queries<br/>• Up to 90% Cost Reduction<br/>• Local Caching on NVMe/RAM"]
    end

    subgraph Cold["(3) Cold Storage Tier (Days 31 - 365)"]
        C_Node["Cold Tier (Pure Amazon S3)<br/>• Zero Active Compute Cost<br/>• Detached S3 Index Storage<br/>• On-Demand Warm Mounting"]
    end

    subgraph Purge["(4) Deletion Tier"]
        Delete[("Automated Purge / Delete")]
    end

    H_Node -->|"ISM: warm_migration"| W_Node
    W_Node -->|"ISM: cold_migration"| C_Node
    C_Node -->|"ISM: delete action"| Delete

    classDef hot fill:#fee2e2,stroke:#dc2626,stroke-width:1px,color:#0f172a;
    classDef warm fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef cold fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef del fill:#f1f5f9,stroke:#475569,stroke-width:1px,color:#0f172a;

    class H_Node hot;
    class W_Node warm;
    class C_Node cold;
    class Delete del;
```

---

## 2. Storage Tier Comparison Matrix

| Storage Tier | Underlying Media | Read/Write Access | Query Latency | Cost Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Hot Storage** | High-performance EBS SSDs (`gp3`, `io2`) or NVMe instance stores. | **Read & Write** (Active indexing target). | **Single-digit milliseconds** ($< 10\text{ ms}$). | High (standard EBS storage + data node instance hours). |
| **UltraWarm Storage** | Amazon S3 storage queried via specialized UltraWarm compute nodes. | **Read-Only** (Indices must be set to read-only before migration). | Near-hot latency (sub-second to seconds via smart caching). | **Up to 90% cheaper** than hot EBS storage. |
| **Cold Storage** | Amazon S3 managed indices completely detached from compute. | **Read-Only** (Requires mounting/warming before querying). | Minutes (must mount index to UltraWarm nodes to query). | **Lowest cost** (pure S3 storage fees, zero compute overhead). |

---

## 3. Index State Management (ISM) Policies

**Index State Management (ISM)** is an automated policy engine built into OpenSearch that manages index lifecycles based on document age, index size, or document count.

```mermaid
graph TD
    HotState["State 1: Hot (Active Ingestion)"] --> Condition1{"Age >= 1 Day OR Size >= 50 GB"}

    Condition1 -->|"Trigger Met"| Rollover["Action: rollover & force_merge"]
    Rollover --> StateWarm["State 2: UltraWarm (Interactive Queries)"]

    StateWarm --> Condition2{"Age >= 30 Days"}
    Condition2 -->|"Trigger Met"| MigrationCold["Action: cold_migration"]

    MigrationCold --> StateCold["State 3: Cold Storage (Archived S3)"]
    StateCold --> Condition3{"Age >= 365 Days"}
    Condition3 -->|"Trigger Met"| ActionDelete["Action: delete (Purge from S3)"]

    classDef st fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef cond fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef act fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class HotState,StateWarm,StateCold st;
    class Condition1,Condition2,Condition3 cond;
    class Rollover,MigrationCold,ActionDelete act;
```

### Key ISM Actions for DEA-C01:
1. **`rollover`**: Closes the active index and creates a new index when target size (e.g. 50 GB) or age (e.g. 1 day) is reached.
2. **`force_merge`**: Merges underlying Lucene segments (`max_num_segments: 1`) to reclaim deleted document space and accelerate search performance before moving to warm storage.
3. **`read_only`**: Locks the index from further write modifications (mandatory step before UltraWarm migration).
4. **`warm_migration`**: Migrates the index from EBS hot data nodes to S3-backed UltraWarm storage.
5. **`cold_migration`**: Moves warm indices to Cold storage, releasing UltraWarm node resources.
6. **`delete`**: Permanently purges expired indices from S3.

---

## 4. Production ISM Policy Example

Below is a production-grade ISM JSON policy that enforces hot-to-warm-to-cold migration for daily logs:

```json
{
  "policy": {
    "description": "Lifecycle policy for production application logs",
    "default_state": "hot",
    "states": [
      {
        "name": "hot",
        "actions": [
          {
            "rollover": {
              "min_index_age": "1d",
              "min_primary_shard_size": "45gb"
            }
          }
        ],
        "transitions": [
          {
            "state_name": "warm",
            "conditions": {
              "min_index_age": "7d"
            }
          }
        ]
      },
      {
        "name": "warm",
        "actions": [
          {
            "replica_count": {
              "number_of_replicas": 0
            }
          },
          {
            "warm_migration": {}
          }
        ],
        "transitions": [
          {
            "state_name": "cold",
            "conditions": {
              "min_index_age": "30d"
            }
          }
        ]
      },
      {
        "name": "cold",
        "actions": [
          {
            "cold_migration": {
              "timestamp_field": "@timestamp"
            }
          }
        ],
        "transitions": [
          {
            "state_name": "delete",
            "conditions": {
              "min_index_age": "365d"
            }
          }
        ]
      },
      {
        "name": "delete",
        "actions": [
          {
            "delete": {}
          }
        ],
        "transitions": []
      }
    ]
  }
}
```

---

## 5. DEA-C01 Exam Essentials

> [!IMPORTANT]
> **Key Exam Decision Triggers for OpenSearch Storage & ISM**:
>
> - **"Cost-effective interactive querying of 6-month historical log data in OpenSearch"** $\rightarrow$ Migrate indices to **UltraWarm Storage**.
> - **"Archive 1-year compliance log data at minimal cost without deleting indices"** $\rightarrow$ Migrate indices to **Cold Storage**.
> - **"Automate shard rollover and tier migration without custom Python/Lambda scripts"** $\rightarrow$ Define an **Index State Management (ISM)** policy.
> - **"Optimize query speed and storage before moving to UltraWarm"** $\rightarrow$ Execute a **`force_merge`** action to consolidate Lucene segments into a single segment.

---

## 📌 Related Notes
- `[[en/02-services/analytics-streaming/opensearch/opensearch|opensearch]]` — OpenSearch Service Master Hub
- `[[en/02-services/analytics-streaming/opensearch/opensearch-cluster-architecture|opensearch-cluster-architecture]]` — Primary & Replica Shards
- `[[en/02-services/analytics-streaming/opensearch/opensearch-troubleshooting-and-tuning|opensearch-troubleshooting-and-tuning]]` — Disk Watermarks & Heap Pressures
- `[[en/02-services/storage/s3/s3|s3]]` — S3 Data Lake Durability & Lifecycle
