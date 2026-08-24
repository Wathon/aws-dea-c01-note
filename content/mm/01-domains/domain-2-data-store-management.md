---
title: "Domain 2: Data Store Management (မြန်မာဘာသာ)"
type: domain
tags:
  - domain/storage
  - dea-c01
  - exam-prep
  - burmese
date: 2026-07-28
---

# 🗄️ Domain 2: Data Store Management (Weight: 26%)

- **Domain ID**: Domain 2
- **Language / ဘာသာစကား**: [English (Original)](/en/01-domains/domain-2-data-store-management) | **မြန်မာဘာသာ (Burmese)**
- **Focus**: သင့်လျော်သော data stores များကို ရွေးချယ်ခြင်း၊ data schemas များကို ဒီဇိုင်းရေးဆွဲခြင်း၊ data lifecycles များကို စီမံခန့်ခွဲခြင်းနှင့် storage performance နှင့် cost များကို optimize ပြုလုပ်ခြင်း။
- **Hub Links**: [[mm/index|index]] | [[mm/00-hub/dea-c01-roadmap|dea-c01-roadmap]] | [[mm/00-hub/service-catalog|service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 2.1: Choose data storage solutions
- **Object Storage**: [[mm/02-services/storage/s3/s3|s3]] (S3 Standard, Intelligent-Tiering, Glacier, S3 Express One Zone)။
- **Block & File Systems**: [[mm/02-services/storage/ebs-and-instance-store|ebs-and-instance-store]] (EBS gp3/io2, Instance Store)၊ [[mm/02-services/storage/efs-and-fsx|efs-and-fsx]] (EFS, FSx for Lustre)၊ [[mm/02-services/storage/ebs-vs-efs-vs-instance-store|ebs-vs-efs-vs-instance-store]] (Storage Comparison Matrix)။
- **Data Warehousing**: [[mm/02-services/database/redshift|redshift]] (Redshift Provisioned RA3, Redshift Serverless, Redshift Spectrum)။
- **NoSQL & Specialized Databases**: [[mm/02-services/database/dynamodb|dynamodb]]၊ [[mm/02-services/database/nosql-specialized-databases|nosql-specialized-databases]] (ElastiCache, Timestream, Neptune, OpenSearch)။

### Task Statement 2.2: Design data models and schema evolution
- **Relational vs Dimensional Modeling**: [[mm/02-services/database/redshift|redshift]] တွင် Star schema vs Snowflake schema အသုံးပြုခြင်း။
- **Partition Keys & Sort Keys**:
  - [[mm/02-services/database/dynamodb|dynamodb]] တွင် Primary key design, Partition keys, Sort keys, LSI/GSI များ။
  - [[mm/02-services/database/redshift|redshift]] တွင် Distribution keys (EVEN, KEY, ALL) များနှင့် Sort keys (COMPOUND, INTERLEAVED) များ။
- **Schema Evolution & Cataloging**: Schema drift ကို ကိုင်တွယ်ဖြေရှင်းရန် [[mm/02-services/analytics-streaming/glue/glue|glue]] Schema Registry နှင့် Data Catalog ကို အသုံးပြုခြင်း။

### Task Statement 2.3: Manage data lifecycles & storage optimization
- **S3 Lifecycle Management**: Transition rules များ (Standard -> Standard-IA -> Glacier Flexible / Deep Archive)၊ expiration rules များ။
- **S3 Object Lock & Immutability**: Compliance အတွက် WORM (Write Once Read Many) စနစ် (Governance mode vs Compliance mode)။
- **Compaction & Vacuuming**: Storage နေရာလွတ်များ ပြန်လည်ရယူရန်နှင့် query optimization ပြုလုပ်ရန်အတွက် [[mm/02-services/database/redshift|redshift]] ၏ VACUUM နှင့် ANALYZE operations များ။

---

## 🛠️ Essential AWS Services in Domain 2

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **Amazon S3** | Data Lake Object Storage | ဗဟို Data lake storage၊ lifecycle tiering၊ S3 Express One Zone | [[mm/02-services/storage/s3/s3|s3]] |
| **Amazon Redshift** | Petabyte-Scale DW | OLAP queries များ၊ RA3 managed storage၊ S3 ကို query လုပ်ရန် Redshift Spectrum | [[mm/02-services/database/redshift|redshift]] |
| **Amazon DynamoDB** | Serverless NoSQL | Low-latency key-value store၊ CDC အတွက် DynamoDB Streams | [[mm/02-services/database/dynamodb|dynamodb]] |
| **Amazon RDS & Aurora** | Hosted OLTP Databases | Relational database workloads များ၊ Aurora Serverless v2၊ Read Replicas များ | [[mm/02-services/database/rds-and-aurora|rds-and-aurora]] |
| **FSx for Lustre** | High-Perf File Storage | HPC နှင့် EMR/S3 staging အတွက် မြန်နှုန်းမြင့် parallel file system | [[mm/02-services/storage/efs-and-fsx|efs-and-fsx]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 2

> [!IMPORTANT]
> **Redshift Distribution Key ရွေးချယ်ခြင်း (Redshift Distribution Key Selection)**:
> - **KEY Distribution**: Column တစ်ခုတည်းရှိ တန်ဖိုးများပေါ် မူတည်၍ rows များကို ဖြန့်ဝေသည် (ဥပမာ- join key နှင့် ကိုက်ညီသော `customer_id`)။ ကြီးမားသော table များကို join သည့်အခါ အထူးသင့်လျော်ပါသည်!
> - **ALL Distribution**: Table တစ်ခုလုံးကို compute node တိုင်းသို့ duplicate လုပ်၍ သိမ်းဆည်းသည်။ သေးငယ်ပြီး update လုပ်ခဲသော dimension tables များအတွက် အသင့်တော်ဆုံးဖြစ်သည် (< 2-3 million rows)။
> - **EVEN Distribution**: Round-robin နည်းလမ်းဖြင့် ဖြန့်ဝေသည်။ မကြာခဏ join လေ့မရှိသော table များ သို့မဟုတ် ရှင်းလင်းသော join key မရှိသည့်အခါ default အနေဖြင့် အသုံးပြုသည်။

> [!TIP]
> **S3 Express One Zone**:
> - **တည်ငြိမ်သော single-digit millisecond latency** ရရှိစေရန်နှင့် S3 Standard ထက် latency ၁၀ ဆ ပိုမိုမြန်ဆန်စေရန် ဒီဇိုင်းထုတ်ထားသော Single-AZ storage class ဖြစ်သည်။ High-throughput analytics လုပ်ငန်းများ (EMR, Athena, SageMaker checkpointing) အတွက် အလွန်သင့်တော်ပါသည်။

---

## 📌 Checklist for Domain 2
- [ ] [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf) မှ Slide စာမျက်နှာများ: 76-154 (Storage) နှင့် 155-265 (Database) တို့ကို ပြန်လည်လေ့လာရန်
- [ ] Service မှတ်စုများကို ပြီးမြောက်အောင် ဖတ်ရှုရန်: [[mm/02-services/storage/s3/s3|s3]], [[mm/02-services/database/redshift|redshift]], [[mm/02-services/database/dynamodb|dynamodb]], [[mm/02-services/database/rds-and-aurora|rds-and-aurora]]
- [ ] အဓိက သဘောတရားများကို ပြန်လည်သုံးသပ်ရန်: [[mm/03-concepts/data-modeling-and-partitioning|data-modeling-and-partitioning]], [[mm/03-concepts/data-formats-and-compression|data-formats-and-compression]]
