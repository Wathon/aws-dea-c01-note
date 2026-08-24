---
title: Big Data Fundamentals & Data Lake Architecture
type: concept
tags:
  - concept/data-engineering
  - dea-c01
  - fundamentals
  - data-lake
  - medallion-architecture
date: 2026-08-15
---

# 🌐 Big Data Fundamentals & Data Lake Architecture

- **Category**: Fundamentals (Data Engineering Core Architecture)
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/03-concepts/big-data-fundamentals)
- **Slide Reference**: Pages 12–37 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[index]]` | `[[service-catalog]]` | `[[domain-1-ingestion-and-processing]]` | `[[domain-2-data-store-management]]` | `[[s3]]` | `[[redshift]]` | `[[glue]]`

---

## 1. The 5 V's of Big Data

Big Data refers to datasets whose size, complexity, and velocity exceed the storage, management, and processing capacity of traditional relational database management systems (RDBMS).

```mermaid
mindmap
  root((Big Data 5 V's))
    Volume
      Terabytes to Petabytes
      Decoupled S3 Storage
    Velocity
      Real-time Streams & Batch Ingestion
      Kinesis / MSK / Firehose
    Variety
      Structured SQL Tables
      Semi-Structured JSON / Parquet
      Unstructured Images / Audio / Video
    Veracity
      Data Quality & Trustworthiness
      Glue Data Quality / Validation
    Value
      Actionable BI & ML Predictions
      QuickSight / SageMaker
```

1. **Volume**: The massive scale of data generated (ranging from gigabytes to terabytes and petabytes). AWS solves this through **Amazon S3**, which provides virtually unlimited, decoupled object storage.
2. **Velocity**: The speed at which new data is generated, ingested, and processed. AWS handles this via streaming ingestion services like **Amazon Kinesis Data Streams** and **Amazon MSK (Apache Kafka)**.
3. **Variety**: The diversity of data formats:
   - **Structured**: RDBMS tables, CSV files with rigid schemas.
   - **Semi-Structured**: JSON, XML, Apache Avro, Apache Parquet, and ORC.
   - **Unstructured**: Video, audio, PDFs, and raw server logs.
4. **Veracity**: The accuracy, cleanliness, and trustworthiness of the data. Managed using **AWS Glue Data Quality (DQDL)** to quarantine malformed records.
5. **Value**: The ultimate business utility extracted through Business Intelligence (**Amazon QuickSight**) and Machine Learning (**Amazon SageMaker**).

---

## 2. Decoupled Storage and Compute Principle

A foundational design pattern in cloud data engineering is **decoupling storage from compute**:

```mermaid
graph LR
    subgraph StorageLayer["Decoupled Storage Layer"]
        S3Bucket[("Amazon S3 Data Lake<br/>(Central Single Source of Truth)")]
    end

    subgraph ComputeEngines["Independent Compute Engines"]
        Athena["Amazon Athena<br/>(Serverless Interactive SQL)"]
        EMR["Amazon EMR<br/>(Distributed Spark / Hadoop)"]
        Glue["AWS Glue ETL<br/>(Serverless PySpark)"]
        Redshift["Amazon Redshift<br/>(Data Warehouse / Spectrum)"]
        SageMaker["Amazon SageMaker<br/>(ML Feature Training)"]
    end

    S3Bucket <--> Athena
    S3Bucket <--> EMR
    S3Bucket <--> Glue
    S3Bucket <--> Redshift
    S3Bucket <--> SageMaker

    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef comp fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;

    class S3Bucket store;
    class Athena,EMR,Glue,Redshift,SageMaker comp;
```

- **Traditional On-Premise**: Storage and compute are tightly coupled on physical servers (scaling storage requires buying expensive compute nodes).
- **AWS Modern Cloud**: Data is stored cheaply and durability in **Amazon S3** (11 9's durability). Multiple diverse compute engines (Athena, Glue, EMR, SageMaker) can spin up on demand, query the same data simultaneously, and spin down to zero cost when idle.

---

## 3. Data Warehouse vs. Data Lake vs. Data Swamp

```mermaid
graph TD
    subgraph DWH["Data Warehouse (Amazon Redshift)"]
        DWH_Desc["• Schema-on-Write<br/>• Structured Relational / OLAP<br/>• High Concurrency BI Reporting"]
    end

    subgraph DL["Data Lake (Amazon S3)"]
        DL_Desc["• Schema-on-Read<br/>• Multi-Format (Raw, Parquet, JSON)<br/>• Governed by Lake Formation & Catalog"]
    end

    subgraph DS["Data Swamp (Anti-Pattern to Avoid)"]
        DS_Desc["• Ungoverned Data Dump<br/>• Zero Metadata / No Catalog<br/>• Unsearchable & Incurring Idle Costs"]
    end

    classDef dwh fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef dl fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef ds fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;

    class DWH,DWH_Desc dwh;
    class DL,DL_Desc dl;
    class DS,DS_Desc ds;
```

| Characteristic | Data Warehouse (e.g. `[[redshift]]`) | Data Lake (e.g. `[[s3]]`) | Data Swamp (Anti-Pattern) |
| :--- | :--- | :--- | :--- |
| **Data Structure** | **Schema-on-Write**: Schema must be defined before loading data. | **Schema-on-Read**: Raw data is stored first; schema is applied upon query. | Unstructured, ungoverned data dumps without schemas. |
| **Data Formats** | Structured relational tables (OLAP columnar). | Structured, semi-structured (JSON, Parquet), and unstructured. | Disorganized files with no consistent format. |
| **Storage vs. Compute** | Managed scaling (Redshift Serverless or provisioned clusters). | **Fully Decoupled** (Cheap S3 storage + independent compute). | Decoupled but unorganized and unindexed. |
| **Governance** | Strict ACID transactions, primary/foreign keys. | Governed via `[[lake-formation]]` & `[[glue]]` Data Catalog. | Zero governance, no security tagging or catalog. |
| **Primary Users** | Business Analysts, BI Developers, SQL power users. | Data Engineers, Data Scientists, Machine Learning Engineers. | None (Data is unusable and untrusted). |

---

## 4. Medallion Architecture (Data Lake Tiering Strategy)

To ensure data quality and maintain performance as data progresses through a pipeline, modern data lakes follow the **Medallion Architecture**:

```mermaid
graph LR
    Raw["(1) Bronze Layer<br/>Raw Landing Zone<br/>(Immutable CSV / JSON / API)"] -->|"AWS Glue ETL / DQDL Cleansing"| Silver["(2) Silver Layer<br/>Cleaned & Filtered<br/>(Snappy Parquet / Partitioned)"]
    Silver -->|"Business Aggregations & Joins"| Gold["(3) Gold Layer<br/>Curated Data Marts<br/>(Aggregated Business Views)"]
    Gold --> BI["Amazon QuickSight Dashboards"]
    Gold --> ML["Amazon SageMaker ML Models"]

    classDef b fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef s fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef g fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef c fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;

    class Raw b;
    class Silver s;
    class Gold g;
    class BI,ML c;
```

1. **Bronze Layer (Raw Landing Zone)**:
   - Contains raw, un-transformed historical data in its original format (CSV, JSON, streaming events).
   - Serves as an immutable source of truth for reprocessing or auditing.
2. **Silver Layer (Processed / Standardized Zone)**:
   - Cleaned, validated, deduplicated, and converted to optimized columnar formats (**Apache Parquet with Snappy compression**).
   - Partitioned by Date/Region for fast downstream queries.
3. **Gold Layer (Curated / Business Data Marts)**:
   - Pre-aggregated, denormalized, and structured data ready for high-performance consumption by BI dashboards, executive reporting, and machine learning feature stores.

---

## 5. High-Yield DEA-C01 Exam Tips & Traps

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Decoupled Storage and Compute for Big Data"** $\rightarrow$ **Amazon S3 (Storage) + Amazon Athena / Amazon EMR / AWS Glue (Compute)**.
> - **"Preventing Data Swamp"** $\rightarrow$ **AWS Glue Crawlers** to populate Glue Data Catalog + **AWS Lake Formation** for centralized fine-grained access control.
> - **"Optimizing analytical query costs on S3 Data Lake"** $\rightarrow$ Convert raw data to **Apache Parquet with Snappy compression** and partition by high-cardinality query filter columns.

---

## 📌 Related Notes

- `[[data-formats-and-compression]]` — Parquet, ORC, Avro, and Compression Codecs
- `[[data-modeling-and-partitioning]]` — Dimensional modeling and S3 partitioning strategies
- `[[data-validation-and-profiling]]` — Glue Data Quality (DQDL) and data profiling
- `[[s3]]` — Amazon S3 Data Lake architecture
- `[[redshift]]` — Amazon Redshift Data Warehouse and Spectrum
- `[[glue]]` — AWS Glue ETL and Data Catalog
