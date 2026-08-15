---
title: AWS DEA-C01 မြန်မာဘာသာ လေ့လာရေးဗဟို (Knowledge Hub)
type: hub
tags:
  - hub
  - dea-c01
  - burmese
date: 2026-08-15
---

# 🧠 AWS Certified Data Engineer – Associate (DEA-C01) မြန်မာဘာသာ လေ့လာရေးဗဟို

- **Language / ဘာသာစကား**: [English (Original)](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/index.md) | **မြန်မာဘာသာ (Burmese)**
- **မူရင်းသင်ရိုး Slides**: [AWSCertifiedDataEngineerSlides.pdf](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/docs/AWSCertifiedDataEngineerSlides.pdf)
- **လက်တွေ့ Lab ကုဒ်များနှင့် Datasets များ**: [Materials Directory](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/materials)
- **လေ့လာမှု မှတ်တမ်း (Journal)**: [[journal/2026-07-28]]

---

## 📘 အခြေခံ သဘောတရားများ (Fundamental Concepts)

- `[[mm/03-concepts/big-data-fundamentals|big-data-fundamentals]]` — Big Data ၏ 5 V's၊ Data Lake vs Data Warehouse vs Data Swamp နှင့် Medallion Architecture
- `[[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]]` — Row-based vs Columnar (Parquet/ORC)၊ Splittability နှင့် Compression စနစ်များ (Snappy, Gzip, Zstd)
- `[[mm/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]]` — Star Schema vs Snowflake Schema၊ S3 Partitioning နှင့် Partition Pruning
- `[[mm/03-concepts/data-validation-and-profiling|data-validation-and-profiling]]` — Data Profiling vs Validation၊ AWS Glue Data Quality (DQDL) နှင့် Quarantine စနစ်များ
- `[[mm/03-concepts/sql-and-version-control-review|sql-and-version-control-review]]` — SQL Window Functions၊ Join Matrix နှင့် Git CI/CD စနစ်များ

---

## ☁️ မြန်မာဘာသာ ပြန်ဆိုထားသော AWS Services မှတ်စုများ

### 📦 Storage (သိုလှောင်မှု စနစ်များ)
- `[[mm/02-services/storage/s3/s3|Amazon S3 Overview]]` — S3 Object Storage & Storage Classes Matrix
- `[[mm/02-services/storage/s3/s3-performance|S3 Performance]]` — Prefix Partitioning limits, Multipart upload & Byte-Range Fetches
- `[[mm/02-services/storage/s3/s3-lifecycle-rules|S3 Lifecycle Rules]]` — Automated Tiering transitions & Abort Incomplete Multipart Uploads
- `[[mm/02-services/storage/s3/s3-replication|S3 Replication]]` — Cross-Region (CRR), Same-Region (SRR), RTC 15-min SLA & Batch Replication
- `[[mm/02-services/storage/s3/s3-versioning|S3 Versioning]]` — Object versions, Delete Markers & MFA Delete
- `[[mm/02-services/storage/s3/s3-security|S3 Security]]` — Bucket Policies, Block Public Access & Object Lock WORM (Compliance mode)
- `[[mm/02-services/storage/s3/s3-encryption|S3 Encryption]]` — SSE-S3, SSE-KMS, DSSE-KMS, SSE-C & S3 Bucket Keys
- `[[mm/02-services/storage/s3/s3-access-points|S3 Access Points]]` — Multi-tenant access points & S3 Object Lambda PII masking
- `[[mm/02-services/storage/s3/s3-tables|S3 Tables]]` — Apache Iceberg purpose-built storage with automated file compaction
- `[[mm/02-services/storage/s3/s3-storage-lens|S3 Storage Lens]]` — Organization-wide storage analytics & Parquet exports
- `[[mm/02-services/storage/ebs-and-instance-store|Amazon EBS & Instance Store]]` — Persistent block storage vs Ephemeral NVMe
- `[[mm/02-services/storage/efs-and-fsx|Amazon EFS & AWS FSx]]` — POSIX Shared File systems & FSx for Lustre S3 data sync
- `[[mm/02-services/storage/ebs-vs-efs-vs-instance-store|EBS vs. EFS vs. Instance Store]]` — Decision Matrix & Trade-offs

### 🗄️ Database (ဒေတာဘေ့စ်နှင့် Data Warehousing)
- `[[mm/02-services/database/redshift|Amazon Redshift]]` — Petabyte-scale Columnar OLAP Data Warehouse, DISTSTYLE, SORTKEY, `COPY`, & Spectrum
- `[[mm/02-services/database/dynamodb|Amazon DynamoDB]]` — Serverless NoSQL Key-Value store, LSI vs GSI, Streams (CDC), & S3 PITR Export
- `[[mm/02-services/database/rds-and-aurora|Amazon RDS & Aurora]]` — Relational OLTP, Multi-AZ vs Read Replicas, & Redshift Zero-ETL
- `[[mm/02-services/database/nosql-specialized-databases|Specialized Databases]]` — ElastiCache, MemoryDB, Keyspaces, Neptune, & Timestream

### 🔄 Migration & Transfer (ဒေတာ ရွှေ့ပြောင်းခြင်းနှင့် လွှဲပြောင်းခြင်း)
- `[[mm/02-services/migration/dms-and-sct|AWS DMS & AWS SCT]]` — Database Migration Service, Schema Conversion Tool, & Continuous CDC
- `[[mm/02-services/migration/datasync-and-snow|AWS DataSync & Snow Family]]` — Online high-speed network sync vs Snowball Edge / Snowmobile
- `[[mm/02-services/migration/transfer-family|AWS Transfer Family]]` — Managed SFTP, FTPS, FTP, & AS2 directly to S3 / EFS
- `[[mm/02-services/migration/data-exchange|AWS Data Exchange]]` — Third-party commercial dataset subscriptions & Redshift Data Sharing
- `[[mm/02-services/migration/application-discovery-and-mgn|Application Discovery & MGN]]` — Server discovery and automated Lift-and-Shift rehosting

### ⚡ Compute & Containers (တွက်ချက်မှုနှင့် ကွန်တိန်နာများ)
- `[[mm/02-services/compute-containers/lambda|AWS Lambda]]` — Serverless event-driven compute, stream batching tuning, & `/tmp` / EFS storage
- `[[mm/02-services/compute-containers/batch|AWS Batch]]` — Managed containerized batch processing, Spot instances, & Array jobs
- `[[mm/02-services/compute-containers/ec2-and-graviton|EC2 & AWS Graviton]]` — Spot instance strategies, EMR node mapping, & Arm price-performance
- `[[mm/02-services/compute-containers/ecr-ecs-eks|Amazon ECR, ECS & EKS]]` — Container registries, ECS Fargate, & Amazon EMR on EKS Spark

---

## 🗺️ အင်္ဂလိပ်ဘာသာ အပြည့်အစုံ မှတ်စုများ (Full English Notes)

- `[[en/index|English Knowledge Hub]]` — အင်္ဂလိပ်ဘာသာဖြင့် ရေးသားထားသော ဝန်ဆောင်မှုအားလုံး၏ အသေးစိတ် မှတ်စုများ။
- `[[dea-c01-roadmap]]` — စာမေးပွဲ အပိုင်း ၄ ပိုင်း အလေးချိန်နှင့် လေ့လာရန် နည်းဗျူဟာများ
- `[[service-catalog]]` — AWS Services အားလုံး၏ စာရင်း
- `[[service-comparisons]]` — ဆာဗစ်များ နှိုင်းယှဉ်ချက် Decision Matrix
- `[[high-frequency-exam-patterns]]` — စာမေးပွဲတွင် အမေးအများဆုံး မေးခွန်းပုံစံများနှင့် Keywords များ

---

## 🏷️ Tags

`#dea-c01` `#aws/service` `#burmese` `#concept/data-engineering` `#storage` `#database` `#migration` `#compute`
