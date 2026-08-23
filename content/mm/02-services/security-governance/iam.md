---
title: AWS IAM, Execution Roles, Cross-Account Access & Policy Evaluation (မြန်မာဘာသာ)
type: aws-service
category: Security & Governance
tags:
  - aws/service
  - dea-c01
  - security/iam
  - access-control
  - cross-account
  - service-roles
  - policy-evaluation
  - burmese
date: 2026-08-23
---

# 🔑 AWS IAM, Execution Roles, Cross-Account Access & Policy Evaluation

- **Category**: Security, Identity, & Compliance / Access Management & Data Authorization
- **Language / ဘာသာစကား**: [English (Original)](/en/02-services/security-governance/iam) | **မြန်မာဘာသာ (Burmese)**
- **Primary Use Case**: Least-privilege identity access management၊ pipeline execution roles (AWS Glue, Lambda, EMR, Redshift)၊ cross-account data lake access နှင့် IAM database authentication။
- **Slide Reference**: `[[AWSCertifiedDataEngineerSlides.pdf]]` ရှိ စာမျက်နှာ 542–559
- **Hub Links**: `[[mm/index]]` | `[[service-catalog]]` | `[[domain-4-data-security-and-governance]]` | `[[lake-formation]]` | `[[kms-and-secrets]]` | `[[glue]]` | `[[redshift]]`

---

## 1. High-Level Summary (ခြုံငုံသုံးသပ်ချက်)

**AWS Identity and Access Management (IAM)** သည် AWS data services အားလုံးတွင် authentication (မည်သူမည်ဝါဖြစ်ကြောင်း အတည်ပြုခြင်း) နှင့် authorization (လုပ်ပိုင်ခွင့် ခွင့်ပြုခြင်း) တို့ကို စီမံခန့်ခွဲပေးသည့် အဓိကအခြေခံ engine တစ်ခုဖြစ်ပါသည်။

**AWS Certified Data Engineer - Associate (DEA-C01)** စာမေးပွဲအတွက် ပြင်ဆင်နေသော data engineers များအနေဖြင့် IAM နှင့် ပတ်သက်၍ အောက်ပါအချက်များကို ကျွမ်းကျင်စွာ နားလည်ထားရန် လိုအပ်ပါသည်:
1. **The Policy Evaluation Logic**: Explicit `Deny`၊ explicit `Allow`၊ Permission Boundaries နှင့် SCPs (Service Control Policies) တို့ အပြန်အလှန် မည်သို့အလုပ်လုပ်ပုံ။
2. **Service Execution Roles**: Compute engines များ (**AWS Glue, AWS Lambda, Amazon EMR, Amazon Redshift**) ထံသို့ least-privilege roles များ ချိတ်ဆက်သတ်မှတ်ပုံ။
3. **Cross-Account Data Lake Access**: Trust policies နှင့်တွဲဖက်ထားသော **`sts:AssumeRole`** သို့မဟုတ် cross-account **S3 Bucket Policies** + **KMS Key Policies** များကို configure လုပ်ဆောင်ပုံ။
4. **IAM Database Authentication**: **Amazon RDS, Aurora နှင့် Redshift** များအတွက် သက်တမ်းတို short-lived IAM database authentication tokens များကို ထုတ်ယူအသုံးပြုခြင်းဖြင့် hardcoded database passwords များ ထည့်သွင်းအသုံးပြုရခြင်းကို ဖယ်ရှားပုံ။

```mermaid
graph TD
    subgraph IAM_Entities["IAM Entities & Policy Evaluation"]
        Principal["IAM Principal<br/>(User, Role, သို့မဟုတ် AWS Service)"] --> Request["API Request<br/>(ဥပမာ- s3:GetObject, glue:StartJobRun)"]

        Request --> EvalEngine{"IAM Policy Evaluation Engine"}

        EvalEngine -->|"(1) Explicit Deny တွေ့ရှိပါသလား?"| DenyRes[("⛔ Access DENIED<br/>(Explicit Deny သည် အရာအားလုံးထက် ပိုမိုဦးစားပေးသည်)")]
        EvalEngine -->|"(2) Organizations SCP Deny ဖြစ်နေပါသလား?"| DenyRes
        EvalEngine -->|"(3) Permission Boundary Allow ဖြစ်ပါသလား?"| BoundaryCheck{"Boundary & Identity Allow ဖြစ်ပါသလား?"}
        
        BoundaryCheck -->|Yes| AllowRes[("✅ Access ALLOWED")]
        BoundaryCheck -->|No / Default Deny| DenyRes
    end

    classDef princ fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef eval fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a;
    classDef allow fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#0f172a;
    classDef deny fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#0f172a;

    class Principal,Request princ;
    class EvalEngine,BoundaryCheck eval;
    class AllowRes allow;
    class DenyRes deny;
```

---

## 2. IAM Policy Structure & Evaluation Logic (IAM Policy တည်ဆောက်ပုံနှင့် ဆန်းစစ်ဆုံးဖြတ်မှု လုပ်ငန်းစဉ်)

IAM Policy ဆိုသည်မှာ statements တစ်ခု သို့မဟုတ် တစ်ခုထက်ပိုမိုပါဝင်သော JSON document တစ်ခု ဖြစ်ပါသည်:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGlueS3GoldReadWrite",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::company-gold-lakehouse",
        "arn:aws:s3:::company-gold-lakehouse/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "true"
        }
      }
    }
  ]
}
```

### Core Policy Elements (အဓိက ပါဝင်သော အစိတ်အပိုင်းများ):
- **`Effect`**: `Allow` သို့မဟုတ် `Deny` ဖြစ်သည်။
- **`Principal`**: လုပ်ပိုင်ခွင့်ရရှိမည့် account၊ user၊ role သို့မဟုတ် service ဖြစ်သည် (S3 Bucket Policies ကဲ့သို့သော **Resource-Based Policies** များတွင် ထည့်သွင်းရန် လိုအပ်ပြီး Identity-Based policies များတွင် ထည့်သွင်းရန်မလိုပါ)။
- **`Action`**: ခွင့်ပြုထားသော သို့မဟုတ် တားမြစ်ထားသော သီးခြား API actions များ (ဥပမာ `s3:GetObject`၊ `glue:StartJobRun`)။
- **`Resource`**: ပစ်မှတ်ထားသော AWS resource ၏ ARN (ဥပမာ `arn:aws:s3:::bucket-name/*`)။
- **`Condition`**: Policy စတင်အကျိုးသက်ရောက်မည့် သတ်မှတ်ချက် Key-value ကန့်သတ်ချက်များ:
  - `aws:SecureTransport`: Data transit ကာလအတွင်း HTTPS/TLS ကို မဖြစ်မနေ အသုံးပြုစေခြင်း။
  - `aws:PrincipalArn`: ခေါ်ယူအသုံးပြုသည့် သီးခြား role များကိုသာ ကန့်သတ်ခွင့်ပြုခြင်း။
  - `s3:x-amz-server-side-encryption`: Data upload ပြုလုပ်စဉ် encryption header ပါဝင်စေရန် မဖြစ်မနေ သတ်မှတ်ခြင်း။
  - `aws:sourceVpce`: သီးခြား VPC Gateway Endpoint တစ်ခုမှတစ်ဆင့် ဝင်ရောက်အသုံးပြုမှုကိုသာ ကန့်သတ်ခြင်း။

### Policy Evaluation Rules (Policy ဆန်းစစ်ဆုံးဖြတ်မှု စည်းမျဉ်းများ):
1. **Default Deny**: ပုံမှန်အားဖြင့် request အားလုံးကို implicitly deny (အလိုအလျောက် ပိတ်ပင်) ထားပါသည်။
2. **Explicit Allow**: Identity-based၊ resource-based သို့မဟုတ် boundary policies များတွင် ကိုက်ညီမှုရှိပါက access ခွင့်ပြုပေးပါသည်။
3. **Explicit Deny Overrides All**: မည်သည့်သက်ဆိုင်ရာ policy တွင်မဆို ပါဝင်သော explicit `Deny` သည် `Allow` statement မည်မျှပင် ရှိစေကာမူ access ကို ချက်ချင်း ပိတ်ပင်တားဆီးပါသည်။

---

## 3. Service Execution Roles for Data Pipelines (Data Pipelines အတွက် Service Execution Roles များ)

Data services များသည် သင့်ကိုယ်စား လုပ်ငန်းဆောင်တာများကို ဆောင်ရွက်ရန်အတွက် **IAM Execution Roles** လိုအပ်ပါသည်:

```mermaid
graph LR
    subgraph DataServices["Data Pipeline Compute Services"]
        Glue["AWS Glue Spark Job"]
        Lambda["AWS Lambda Ingestion"]
        EMR["Amazon EMR Cluster"]
        Redshift["Amazon Redshift Cluster"]
    end

    subgraph IAMRoles["IAM Execution Roles (AssumeRole)"]
        GlueRole["Glue Service Role<br/>(AWSGlueServiceRole + S3 Access)"]
        LambdaRole["Lambda Basic Execution Role<br/>(& S3/KMS permissions)"]
        EMRRole["EMR Service Role &<br/>EC2 Instance Profile"]
        RedshiftRole["Redshift Spectrum Role<br/>(S3 Read + Glue Catalog Read)"]
    end

    subgraph Targets["Target Resources"]
        S3[("Amazon S3 Data Lake")]
        KMS["AWS KMS CMK Key"]
        CW["CloudWatch Logs"]
    end

    Glue --> GlueRole --> S3 & KMS & CW
    Lambda --> LambdaRole --> S3 & KMS & CW
    EMR --> EMRRole --> S3 & KMS
    Redshift --> RedshiftRole --> S3 & KMS

    classDef srv fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef role fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef tgt fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class Glue,Lambda,EMR,Redshift srv;
    class GlueRole,LambdaRole,EMRRole,RedshiftRole role;
    class S3,KMS,CW tgt;
```

### 1. AWS Glue Execution Role
- **Trust Policy Principal**: `glue.amazonaws.com` ဖြစ်သည်။
- **Managed Policy**: `AWSGlueServiceRole` (Glue အနေဖြင့် network interfaces ဖန်တီးခြင်း၊ Data Catalog နှင့် ချိတ်ဆက်ဆက်သွယ်ခြင်းနှင့် CloudWatch သို့ logs ရေးသားခြင်းတို့ကို ခွင့်ပြုသည်)။
- **Custom Policy**: Data lake buckets များပေါ်တွင် S3 read/write permissions + S3 KMS key ပေါ်တွင် `kms:Decrypt` နှင့် `kms:GenerateDataKey` လုပ်ပိုင်ခွင့်များ။

### 2. Amazon EMR Roles
- **EMR Service Role**: EMR control plane အား EC2 instances များ provision လုပ်ခြင်း၊ EBS volumes များ ချိတ်ဆက်ခြင်းနှင့် security groups များကို configure လုပ်ခြင်းတို့အတွက် ခွင့်ပြုပေးပါသည်။
- **EC2 Instance Profile (Job Flow Role)**: အောက်ခံ EC2 nodes များသို့ သတ်မှတ်ပေးပြီး Hadoop/Spark applications များအား Amazon S3 (`EMRFS`) မှ data ဖတ်ရှု/ရေးသားခွင့် ပြုပေးပါသည်။

### 3. Amazon Redshift Spectrum IAM Role
- **Trust Policy Principal**: `redshift.amazonaws.com` ဖြစ်သည်။
- **Permissions**: `AmazonS3ReadOnlyAccess` (ပြင်ပ S3 data lake ပေါ်တွင်) + `AWSGlueConsoleFullAccess` / `glue:GetTable` (Glue Catalog metadata ကို ဖတ်ရှုရန်)။

---

## 4. Cross-Account Data Lake Access Patterns (Cross-Account Data Lake ဝင်ရောက်အသုံးပြုမှု ပုံစံများ)

Enterprise data mesh ပတ်ဝန်းကျင်များတွင် Account A ရှိ analytical datasets များကို Account B ရှိ Glue/Athena/EMR jobs များမှ မကြာခဏ ရယူသုံးစွဲရန် လိုအပ်ပါသည်။

```mermaid
sequenceDiagram
    autonumber
    participant Job as Account B ရှိ Glue / EMR (111122223333)
    participant STS as AWS STS (Account A)
    participant RoleA as Account A ရှိ Cross-Account Role (444455556666)
    participant S3A as S3 Data Lake (Account A)
    participant KMS_A as KMS CMK (Account A)

    Note over Job,RoleA: Pattern A: Role Assumption (sts:AssumeRole)
    Job->>STS: sts:AssumeRole(RoleARN_A, ExternalId) ကို ခေါ်ယူခြင်း
    STS->>RoleA: Trust Policy ကို စစ်ဆေးအတည်ပြုခြင်း (Principal: Account B)
    STS-->>Job: Temporary Security Credentials (AccessKey, Secret, Token) ပြန်လည်ပေးပို့ခြင်း
    Job->>S3A: Temporary credentials ကို အသုံးပြု၍ s3:GetObject လုပ်ဆောင်ခြင်း
    Job->>KMS_A: Temporary credentials ကို အသုံးပြု၍ kms:Decrypt လုပ်ဆောင်ခြင်း
    S3A-->>Job: Encrypted Parquet Data ကို အောင်မြင်စွာ ဖတ်ရှုခြင်း ✅
```

### Pattern Comparison: Role Assumption vs. Bucket Policy (ပုံစံနှစ်မျိုး နှိုင်းယှဉ်ချက် - Role Assumption နှင့် Bucket Policy)

| Dimension (ရှုထောင့်) | Pattern A: Cross-Account IAM Role (`AssumeRole`) | Pattern B: Cross-Account S3 Bucket Policy |
| :--- | :--- | :--- |
| **How It Works (အလုပ်လုပ်ပုံ)** | Account B သည် AWS STS ကို အသုံးပြု၍ Account A ရှိ role တစ်ခုကို assume လုပ်သည်။ | Account A ၏ S3 Bucket Policy သည် Account B ၏ IAM principal သို့ တိုက်ရိုက် access ခွင့်ပြုပေးသည်။ |
| **KMS Decryption (KMS Data ဖြေဖျက်ခြင်း)** | Temporary credentials များသည် Account A ၏ standard KMS key policy ကို အသုံးပြုပြီး Account A အတွင်း၌သာ execute လုပ်ဆောင်သည်။ | Account A ၏ KMS Key Policy တွင် **Account B ၏ principal သို့ `kms:Decrypt` လုပ်ပိုင်ခွင့်ကို explicitly ပေးထားရမည်**။ |
| **Object Ownership (Object ပိုင်ဆိုင်မှု)** | Upload လုပ်လိုက်သော objects များကို **Account A မှ ပိုင်ဆိုင်သည်** (Account A ရှိ Role က ရေးသားသောကြောင့်ဖြစ်သည်)။ | **S3 Object Ownership (Bucket Owner Enforced)** ကို enable မလုပ်ထားပါက upload လုပ်သော objects များကို မူလအားဖြင့် Account B မှ ပိုင်ဆိုင်သည်။ |
| **Best Used When (အသုံးပြုရန် အသင့်တော်ဆုံး အခြေအနေ)** | Account A အတွင်း၌ လုပ်ပိုင်ခွင့် အတူတူ လိုအပ်သော Third-party vendors များ သို့မဟုတ် multi-step pipelines များအတွက် သင့်တော်သည်။ | Role switching ပြုလုပ်ရန်မလိုဘဲ account များအကြား S3 buckets များကို တိုက်ရိုက် query လုပ်လိုသော Athena သို့မဟုတ် EMR များအတွက် သင့်တော်သည်။ |

---

## 5. IAM Database Authentication (RDS, Aurora & Redshift)

ETL connection strings သို့မဟုတ် config files များတွင် database passwords များကို hardcode ရေးသားခြင်းသည် enterprise security စံနှုန်းများနှင့် မကိုက်ညီပါ။

```mermaid
graph LR
    App["AWS Lambda / Glue ETL"] -->|"(1) Generate Auth Token<br/>(RDS IAM Auth / GetClusterCredentials)"| STS["AWS IAM / STS"]
    STS -->|"(2) 15-Min Signed Token"| App
    App -->|"(3) Connect via JDBC/ODBC<br/>(Password = Token)"| DB[("Amazon Redshift / RDS Aurora")]
    DB -->|"(4) Validates IAM Token"| DB

    classDef app fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef sts fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef db fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class App app;
    class STS sts;
    class DB db;
```

1. **Amazon RDS & Aurora IAM Database Authentication**:
   - AWS SDK (`rds:connect`) ကို အသုံးပြု၍ သက်တမ်းတို **15-minute authentication token** ကို ထုတ်ယူပေးပါသည်။
   - Database user ကို `IDENTIFIED WITH AWSAuthenticationPlugin` ဖြင့် configure ပြုလုပ်ထားပါသည်။
2. **Amazon Redshift IAM Authentication**:
   - Database user တစ်ဦးအတွက် temporary database credentials များ (သက်တမ်း ၁၅ မိနစ်) ထုတ်ယူရန် `redshift:GetClusterCredentials` ကို ခေါ်ယူပါသည်။
   - Users များကို အလိုအလျောက် provision ပြုလုပ်ပေးခြင်း သို့မဟုတ် IAM groups များကို Redshift database groups များနှင့် ချိတ်ဆက်ပေးခြင်း (mapping) တို့ကို လုပ်ဆောင်ပေးပါသည်။

---

## 6. S3 Bucket Policies vs. IAM Policies vs. Lake Formation

| Capability (လုပ်ဆောင်နိုင်စွမ်း) | IAM Policy | S3 Bucket Policy | AWS Lake Formation |
| :--- | :--- | :--- | :--- |
| **Attachment Target (ချိတ်ဆက်ရမည့် ပစ်မှတ်)** | Users, Groups, Roles. | S3 Bucket (Resource-based). | Glue Data Catalog Tables, Columns, Rows. |
| **Object-Level Control (Object အဆင့် ထိန်းချုပ်မှု)** | ✅ Yes (`s3:GetObject`, `s3:PutObject`). | ✅ Yes (`s3:GetObject`, `s3:PutObject`). | ✅ Yes (S3 data access ကို စီမံခန့်ခွဲသည်). |
| **Column-Level Masking (ကော်လံအဆင့် Masking ပြုလုပ်မှု)** | ❌ No (Columns များကို filter မလုပ်နိုင်ပါ). | ❌ No (Columns များကို filter မလုပ်နိုင်ပါ). | ✅ **Yes (Columns များကို Exclude / Mask ပြုလုပ်နိုင်သည်)**. |
| **Row-Level Filtering (အတန်းအဆင့် Filtering ပြုလုပ်မှု)** | ❌ No (Rows များကို filter မလုပ်နိုင်ပါ). | ❌ No (Rows များကို filter မလုပ်နိုင်ပါ). | ✅ **Yes (SQL row filter expressions များဖြင့် ရရှိသည်)**. |
| **Cross-Account Sharing (Cross-Account မျှဝေမှု)** | `sts:AssumeRole` မှတစ်ဆင့်။ | Direct principal grants များမှတစ်ဆင့်။ | **AWS RAM (LF Resource Share) မှတစ်ဆင့်**။ |

---

## 7. DEA-C01 Exam Essentials (စာမေးပွဲအတွက် မဖြစ်မနေ သိထားသင့်သည့် အချက်များ)

> [!IMPORTANT]
> **Key Exam Decision Triggers for IAM (IAM ဆိုင်ရာ အဓိက စာမေးပွဲ ဆုံးဖြတ်ချက် လမ်းညွှန်များ)**:
>
> - **"Grant an AWS Glue Spark job access to an S3 data lake encrypted with AWS KMS"** $\rightarrow$ `AWSGlueServiceRole`၊ S3 bucket permissions (`s3:GetObject`, `s3:PutObject`) နှင့် KMS permissions (`kms:Decrypt`, `kms:GenerateDataKey`) ပါဝင်သော IAM Role တစ်ခုကို ချိတ်ဆက်သတ်မှတ်ပေးပါ။
> - **"Eliminate hardcoded database passwords in AWS Lambda connecting to Amazon Redshift"** $\rightarrow$ **IAM Database Authentication** (`redshift:GetClusterCredentials`) သို့မဟုတ် **AWS Secrets Manager** ကို အသုံးပြုပါ။
> - **"Cross-Account S3 access fails with Access Denied even though S3 Bucket Policy allows Account B"** $\rightarrow$ S3 bucket သည် **KMS Customer Managed Key (CMK)** ဖြင့် encrypt လုပ်ထားခြင်း ရှိမရှိ စစ်ဆေးပြီး **KMS Key Policy တွင် Account B သို့ `kms:Decrypt` ကို explicitly ခွင့်ပြုထားကြောင်း** သေချာအောင် လုပ်ဆောင်ပါ။
> - **"Enforce TLS 1.2+ encryption in transit on an S3 data lake"** $\rightarrow$ `"aws:SecureTransport": "false"` ဖြစ်ချိန်တွင် S3 Bucket Policy ထဲ၌ explicit `Deny` statement တစ်ခုကို ထည့်သွင်းပါ။
> - **"Restrict access to S3 data lake exclusively from within a VPC"** $\rightarrow$ S3 Bucket Policy တွင် `"aws:sourceVpce": "vpce-12345678"` ဟူသော Condition key ကို ထည့်သွင်းပါ။

---

## 📌 Related Notes (ဆက်စပ် လေ့လာရန်များ)
- `[[lake-formation]]` — Fine-Grained Lake Formation Governance vs IAM
- `[[kms-and-secrets]]` — KMS Key Policies & Secrets Manager
- `[[glue]]` — AWS Glue Execution Roles
- `[[redshift]]` — Amazon Redshift Spectrum IAM Role & Query Federation
- `[[domain-4-data-security-and-governance]]` — DEA-C01 Domain 4 Study Guide
