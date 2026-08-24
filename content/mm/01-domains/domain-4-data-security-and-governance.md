---
title: "Domain 4: Data Security and Governance (မြန်မာဘာသာ)"
type: domain
tags:
  - domain/security
  - dea-c01
  - exam-prep
  - burmese
date: 2026-07-28
---

# 🔒 Domain 4: Data Security and Governance (Weight: 24%)

- **Domain ID**: Domain 4
- **Language / ဘာသာစကား**: [English (Original)](/en/01-domains/domain-4-data-security-and-governance) | **မြန်မာဘာသာ (Burmese)**
- **Focus**: Data at rest နှင့် data in transit တို့တွင် data protection ကို အလေးပေးဆောင်ရွက်ခြင်း၊ identity access management၊ fine-grained permissions၊ governance၊ compliance နှင့် PII identification တို့ကို စီမံခန့်ခွဲခြင်း။
- **Hub Links**: [[mm/index]] | [[dea-c01-roadmap]] | [[service-catalog]]

---

## 📋 Task Statements & Key Competencies

### Task Statement 4.1: Apply authentication, authorization, and access control (Authentication၊ Authorization နှင့် Access Control များကို အသုံးပြုခြင်း)
- **Identity & Access Management (IAM)**:
  - Least privilege principles များ၊ Lambda/Glue/EMR အတွက် execution roles များ၊ IAM roles များမှတစ်ဆင့် cross-account access ရယူခြင်း: [[iam]]။
  - RDS၊ Aurora နှင့် Redshift တို့အတွက် Fine-grained IAM database authentication။
- **Data Lake Access Control**:
  - [[lake-formation]] ကို အသုံးပြု၍ ဗဟိုချုပ်ကိုင်မှုရှိသော fine-grained access control ပြုလုပ်ခြင်း။
  - Column-level, row-level နှင့် cell-level security။
  - Tag-Based Access Control (LF-TBAC)။

### Task Statement 4.2: Apply data protection & encryption mechanisms (Data Protection နှင့် Encryption နည်းလမ်းများကို အသုံးပြုခြင်း)
- **Encryption at Rest**:
  - S3 Server-Side Encryption: SSE-S3 (AWS managed key), SSE-KMS (Customer Master Key), SSE-C (Customer provided key): [[kms-and-secrets]]။
  - Redshift, DynamoDB, RDS, EBS နှင့် EFS တို့အတွက် KMS encryption။
- **Encryption in Transit**:
  - Database connection များအတွက် TLS/SSL ကို မဖြစ်မနေ သုံးစေခြင်း (enforce ပြုလုပ်ခြင်း)၊ `aws:SecureTransport` ကို enforce ပြုလုပ်သည့် S3 bucket policies များ။
- **Secrets Management**:
  - Database credentials များကို [[kms-and-secrets]] (Secrets Manager vs SSM Parameter Store) ဖြင့် စီမံခန့်ခွဲခြင်း။

### Task Statement 4.3: Ensure governance, compliance, and PII protection (Governance, Compliance နှင့် PII Protection သေချာစေခြင်း)
- **PII Detection & Privacy**:
  - [[macie-and-cloudtrail]] (Amazon Macie) ကို အသုံးပြု၍ S3 အတွင်း automated PII scanning ပြုလုပ်ခြင်း။
  - [[glue]] ETL jobs များတွင် sensitive data များကို ရှာဖွေဖော်ထုတ်ခြင်း (Glue Sensitive Data Detection)။
- **Data Cataloging & Discovery**:
  - AWS DataZone နှင့် [[lake-formation]] Data Catalog တို့ကို အသုံးပြု၍ centralized enterprise governance တည်ဆောက်ခြင်း။

### Task Statement 4.4: Network security & isolation (Network Security နှင့် Isolation)
- **Network Isolation**:
  - Data resource များကို Amazon VPC ၏ private subnets များအတွင်း သီးခြားခွဲထုတ်ထားခြင်း (isolate ပြုလုပ်ခြင်း): [[vpc-and-networking]]။
  - Internet Gateway မလိုဘဲ private routing ပြုလုပ်နိုင်ရန် **VPC Endpoints** များကို အသုံးပြုခြင်း (S3 & DynamoDB အတွက် Gateway Endpoints; Glue, KMS, Redshift တို့အတွက် Interface Endpoints / PrivateLink)။

---

## 🛠️ Essential AWS Services in Domain 4

| Service | Primary Function | High-Frequency Exam Use Case | Note Link |
| --- | --- | --- | --- |
| **AWS Lake Formation** | Data Lake Governance | Glue Catalog မှတစ်ဆင့် S3 data lake ပေါ်ရှိ Column/Row-level access control ကို စီမံခြင်း | [[lake-formation]] |
| **AWS KMS** | Key Management & Encryption | Storage services အားလုံးတွင် SSE-KMS encryption အတွက် KMS keys များကို စီမံခန့်ခွဲခြင်း | [[kms-and-secrets]] |
| **AWS Secrets Manager** | Database Credential Rotation | Redshift/RDS password credentials များကို အလိုအလျောက် rotate လုပ်ခြင်း | [[kms-and-secrets]] |
| **Amazon Macie** | Machine Learning PII Discovery | S3 buckets များအတွင်းရှိ sensitive PII data (SSN, credit card) များကို ရှာဖွေဖော်ထုတ်ခြင်း | [[macie-and-cloudtrail]] |
| **VPC Endpoints** | Private Network Access | Public internet ပေါ် မဖြတ်သန်းဘဲ S3/DynamoDB/Glue တို့ကို private အနေဖြင့် ချိတ်ဆက်ခြင်း | [[vpc-and-networking]] |
| **AWS Backup** | Centralized Data Protection | Policy-driven multi-service backups များ၊ Vault Lock WORM compliance နှင့် cross-account DR | [[aws-backup]] |

---

## ⚡ High-Yield Exam Scenarios for Domain 4

> [!IMPORTANT]
> **Lake Formation vs IAM vs S3 Bucket Policies**:
> - လိုအပ်ချက်သည် **S3 ပေါ်ရှိ Athena/Redshift Spectrum queries များအတွက် column-level သို့မဟုတ် row-level security ဖြစ်ပါက**: **AWS Lake Formation** ကို ရွေးချယ်ပါ။ Standard S3 bucket policies နှင့် IAM တို့သည် object-level access (read/write file) ကိုသာ ပေးနိုင်ပြီး row/column filtering ကို လုံးဝ မလုပ်ဆောင်နိုင်ပါ!

> [!TIP]
> **Secrets Manager vs SSM Parameter Store**:
> - လိုအပ်ချက်တွင် **automatic database credential rotation** ပါဝင်ပါက **AWS Secrets Manager** ကို ရွေးချယ်ပါ (RDS, Aurora, Redshift တို့နှင့် native အနေဖြင့် ချိတ်ဆက်အလုပ်လုပ်သည်)။
> - Automatic rotation **မလိုအပ်ဘဲ** ကုန်ကျစရိတ် သက်သာစွာ သို့မဟုတ် အခမဲ့ဖြင့် standard parameters/configuration strings များကို သိမ်းဆည်းရန်အတွက် **SSM Parameter Store** ကို ရွေးချယ်ပါ။

---

## 📌 Checklist for Domain 4
- [ ] [[AWSCertifiedDataEngineerSlides.pdf]] ရှိ Slide စာမျက်နှာများ: 542-589 (Security) နှင့် 590-617 (Networking) တို့ကို ပြန်လည်လေ့လာရန်
- [ ] Service notes များကို အပြီးသတ်ဖတ်ရှုရန်: [[lake-formation]], [[iam]], [[kms-and-secrets]], [[macie-and-cloudtrail]], [[vpc-and-networking]], [[aws-backup]]
