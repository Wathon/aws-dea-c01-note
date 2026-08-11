---
title: AWS Backup
type: aws-service
category: Security & Governance
tags:
  - aws/service
  - dea-c01
  - security/backup
  - governance/compliance
  - storage/backup
date: 2026-08-10
---

# 🛡️ AWS Backup (Centralized Policy-Based Data Protection)

- **Category**: Security, Governance & Storage Management
- **Primary Use Case**: Centralized, automated, policy-driven backup management, disaster recovery, WORM compliance (**AWS Backup Vault Lock**), and cross-account / cross-Region data protection across AWS services.
- **Slide Reference**: Pages 139–154, 410–430 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-4-data-security-and-governance]] | [[domain-2-data-store-management]] | [[s3]] | [[ebs-and-instance-store]] | [[efs-and-fsx]]

---

## 1. High-Level Summary

**AWS Backup** is a fully managed, policy-based service that centralizes and automates data protection across AWS services (Amazon S3, EBS, EFS, FSx, RDS, Aurora, DynamoDB, Redshift, DocumentDB, Neptune, Timestream, and EC2) as well as hybrid on-premises workloads.

For the **AWS Certified Data Engineer – Associate (DEA-C01)** exam, AWS Backup is the standard answer for:
1. **Centralized Cross-Service Backup Governance**: Replacing custom snapshot scripts and fragmented service-specific backup tools with unified, tag-driven **Backup Plans**.
2. **Ransomware & Tamper Protection (WORM)**: Using **AWS Backup Vault Lock** in *Compliance Mode* to make backups immutable and non-deletable even by the AWS Account Root User.
3. **Cross-Account & Cross-Region Disaster Recovery**: Automatically replicating encrypted recovery points to an isolated, air-gapped security account in a secondary AWS Region within **AWS Organizations**.
4. **Automated Audit & Compliance**: Continuously evaluating data protection policies against organizational SLAs using **AWS Backup Audit Manager**.

```mermaid
graph TB
    subgraph Organization["AWS Organizations (Central Management)"]
        BackupPlan["AWS Backup Plan<br/>(Cron Schedule / Cold Tiering / Cross-Region Copy)"]
        TagRule["Tag-Based Resource Assignment<br/><code>Environment=Production</code><br/><code>BackupTier=Gold</code>"]
        BackupPlan --> TagRule
    end

    subgraph SourceServices["Protected AWS Resources (Primary Account)"]
        S3Data[("Amazon S3<br/>Data Lake Buckets")]
        EBSVol[("Amazon EBS<br/>Database Disks")]
        EFSShare[("Amazon EFS<br/>Shared File Systems")]
        RDSDB[("Amazon RDS / Aurora<br/>OLTP Databases")]
        DynamoTable[("Amazon DynamoDB<br/>NoSQL Tables")]
        RedshiftClust[("Amazon Redshift<br/>Data Warehouse")]
    end

    TagRule -.->|"Discovers & Protects"| SourceServices

    subgraph PrimaryVault["Primary Backup Vault (Region A)"]
        VaultLock["AWS Backup Vault Lock<br/>🔒 WORM Compliance (Immutable)<br/>🔑 Encrypted with AWS KMS"]
        RecPoints[("Recovery Points (Snapshots / PITR)")]
        VaultLock --- RecPoints
    end

    subgraph DRVault["Secondary Backup Vault (DR Region B / Air-Gapped Account)"]
        DRLock["DR Vault Lock (WORM)<br/>🔑 Independent KMS CMK"]
        DRRecPoints[("Cross-Region / Cross-Account<br/>Replicated Recovery Points")]
        DRLock --- DRRecPoints
    end

    SourceServices -->|"Automated Backup Job"| RecPoints
    RecPoints -->|"Encrypted Cross-Account / Cross-Region Copy"| DRRecPoints

    classDef plan fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef source fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef vault fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef dr fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;

    class BackupPlan,TagRule plan;
    class S3Data,EBSVol,EFSShare,RDSDB,DynamoTable,RedshiftClust source;
    class VaultLock,RecPoints vault;
    class DRLock,DRRecPoints dr;
```

---

## 2. Core Architectural Components

```mermaid
graph LR
    Plan["1. Backup Plan<br/>(Rules & Schedules)"] -->|"Assigns via Tags / ARNs"| Resources["2. Resource Assignment<br/>(S3, EBS, EFS, RDS, DDB)"]
    Resources -->|"Executes Backup"| Vault["3. Backup Vault<br/>(KMS Encrypted Storage)"]
    Vault -->|"Stores"| Points["4. Recovery Points<br/>(Point-in-Time Copies)"]
    Points -->|"Enforces Immutability"| Lock["5. Vault Lock<br/>(WORM Compliance Mode)"]
    Points -->|"Automated Testing"| Audit["6. Audit Manager &<br/>Restore Testing"]

    classDef comp fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    class Plan,Resources,Vault,Points,Lock,Audit comp;
```

### 1. Backup Plans
A **Backup Plan** is a policy definition that specifies when and how AWS Backup protects your resources:
- **Backup Frequency**: Scheduled via cron expressions (e.g., hourly, daily at 02:00 UTC, weekly).
- **Backup Window**: Specifies the start time window (e.g., must start within 8 hours) and completion duration.
- **Lifecycle Rules**:
  - Transition to **Cold Storage** after $X$ days (supported for Amazon EFS, DynamoDB, S3, EBS, etc.).
  - **Expire / Delete** recovery points after $Y$ days (e.g., retain for 365 days for regulatory compliance).
- **Copy Actions**: Automated replication rules to copy recovery points to another **AWS Region** or another **AWS Account** within your AWS Organization.

### 2. Resource Assignment
- Resources are automatically attached to Backup Plans using **Tags** (e.g., `BackupPolicy = DailyGold`, `DataType = FinancialRecords`) or explicit Resource ARNs.
- Dynamically discovers new resources as they are created without requiring manual reconfiguration.

### 3. Backup Vaults & Access Policies
- A **Backup Vault** is a secure, logical container in AWS Backup that stores and organizes **Recovery Points**.
- **Encryption**: Every vault is encrypted at rest using an **AWS KMS Key** (AWS managed key `aws/backup` or Customer Managed Key CMK).
- **Vault Access Policy**: A JSON resource-based policy assigned to the vault to restrict permissions (e.g., denying `backup:DeleteRecoveryPoint` to all non-admin roles).

### 4. Recovery Points
- A **Recovery Point** represents the backed-up content of an AWS resource at a specific point in time (e.g., an EBS snapshot, EFS snapshot, RDS automated snapshot, or S3 continuous PITR baseline).

---

## 3. AWS Backup Vault Lock (WORM Compliance & Ransomware Defense)

**AWS Backup Vault Lock** is a critical security and compliance capability that enforces **WORM (Write Once, Read Many)** immutability on backup vaults. It prevents backups from being deleted or altered by unauthorized users, compromised credentials, or ransomware attacks.

```mermaid
graph TD
    VaultLock["AWS Backup Vault Lock"] --> GovMode["1. Governance Mode<br/>👥 Administrative Protection<br/>🔓 Can be unlocked/deleted by users with<br/>explicit IAM permissions (backup:DeleteVaultLockConfiguration)"]
    VaultLock --> CompMode["2. Compliance Mode<br/>🔒 True WORM (Regulatory Compliance)<br/>⏳ Cooling-Off Period (Grace Period: 3 to 365 days)<br/>🚫 CANNOT BE REMOVED OR DELETED BY ANYONE<br/>(Including AWS Root User and AWS Support!)"]

    CompMode --> RetentionEnforce["Enforced Retention Bounds<br/>(Min / Max Days: 90 to 2555 Days)<br/>🚫 Blocks Out-of-Bounds Backup Jobs"]

    classDef mode fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef comp fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef rule fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class GovMode mode;
    class CompMode comp;
    class RetentionEnforce rule;
```

### Governance Mode vs. Compliance Mode

| Dimension | Governance Mode | Compliance Mode (WORM) |
| :--- | :--- | :--- |
| **Primary Goal** | Guardrail against accidental deletion by operators | Strict regulatory compliance (SEC Rule 17a-4, HIPAA, FINRA) & Ransomware defense |
| **Can Lock be Removed?** | ✅ **Yes** (By users with `backup:DeleteVaultLockConfiguration`) | ❌ **NO** (Once the cooling-off period expires, the lock is permanent) |
| **Can Backups be Deleted Early?** | ✅ **Yes** (By users with administrative IAM permissions) | ❌ **NO (Impossible for anyone, including AWS Root Account and AWS Support)** |
| **Cooling-Off Grace Period** | None (Configurable immediately) | Mandatory grace period (between **3 days and 365 days**) during which the lock can still be deleted |
| **Retention Bounds Enforcement** | Optional | **Mandatory**: Enforces `MinRetentionDays` and `MaxRetentionDays` on all recovery points |

> [!CAUTION]
> **Compliance Mode Lock is Irreversible**:
> Once the cooling-off grace period expires in Compliance Mode, **no one**—not even the AWS account root user, organization administrators, or AWS Technical Support—can delete the vault lock or delete recovery points before their scheduled retention expiration date!

---

## 4. Cross-Region & Cross-Account Backup Architecture

To meet stringent Business Continuity and Disaster Recovery (BC/DR) requirements, AWS Backup natively supports cross-region and cross-account copy operations within **AWS Organizations**.

```mermaid
sequenceDiagram
    autonumber
    participant WorkloadAcct as Primary Workload Account (us-east-1)
    participant PrimaryVault as Primary Backup Vault (us-east-1)
    participant DRVault as DR Backup Vault (us-west-2)
    participant SecAcct as Isolated Security / Backup Account

    Note over WorkloadAcct,PrimaryVault: 1. Scheduled Backup Job Executes
    WorkloadAcct->>PrimaryVault: Snapshot RDS, EFS, DynamoDB, S3
    Note over PrimaryVault: Encrypted with Primary KMS CMK

    Note over PrimaryVault,DRVault: 2. Cross-Region Disaster Recovery Copy
    PrimaryVault->>DRVault: Copy Recovery Point to us-west-2
    Note over DRVault: Re-encrypted with Destination KMS CMK

    Note over PrimaryVault,SecAcct: 3. Cross-Account Air-Gapped Archive Copy
    PrimaryVault->>SecAcct: Copy Recovery Point to Isolated Account Vault
    Note over SecAcct: Encrypted with Security Account KMS CMK<br/>Protected by Immutable Vault Lock!
```

### Key Multi-Account & Multi-Region Rules

1. **Cross-Account Copy Prerequisites**:
   - Both source and destination accounts must belong to the **same AWS Organization**.
   - Must enable **Backup Policies** at the AWS Organizations root/OU level.
   - Destination Backup Vault Access Policy must allow the source account's AWS Backup service principal (`backup.amazonaws.com`) to copy recovery points.
2. **KMS Re-Encryption**:
   - When a recovery point is copied to another Region or Account, it is **automatically decrypted in-flight using the source KMS key and re-encrypted using the destination vault's KMS key**.
   - AWS default managed keys (`aws/backup`) cannot be shared across accounts; **Customer Managed Keys (KMS CMKs)** are mandatory for cross-account copying.

---

## 5. Supported AWS Services Matrix for Data Engineers

| AWS Service | Backup Type / Granularity | Continuous Backup (PITR) | Lifecycle to Cold Storage | Primary Data Engineering Use Case |
| :--- | :--- | :---: | :---: | :--- |
| **Amazon S3** | Scheduled bucket snapshots + Continuous PITR | ✅ **Yes** (Up to 35 days) | ✅ **Yes** | Protecting Data Lake metadata and object stores from accidental deletion |
| **Amazon EFS** | Entire file system snapshot | ❌ No | ✅ **Yes** | Shared container persistent volumes and Lambda code/model repositories |
| **Amazon EBS** | Block-level incremental snapshots | ❌ No | ✅ **Yes** (EBS Archive) | Hosted PostgreSQL, MySQL, and Kafka broker disks on EC2 |
| **Amazon DynamoDB** | Table-level snapshots + Continuous PITR | ✅ **Yes** (Up to 35 days) | ✅ **Yes** | Application state stores and real-time streaming metadata |
| **Amazon RDS / Aurora** | Database instance snapshots + PITR | ✅ **Yes** (Up to 35 days) | ❌ No | Central transactional relational databases |
| **Amazon Redshift** | Provisioned cluster manual / automated snapshots | ❌ No | ❌ No | Petabyte-scale analytical data warehouse clusters |
| **AWS FSx (Lustre, ONTAP, Windows)** | Entire file system snapshots | ❌ No | ❌ No | HPC cluster staging and enterprise file servers |
| **Amazon DocumentDB / Neptune** | Cluster snapshots | ❌ No | ❌ No | NoSQL document and graph database clusters |

---

## 6. AWS Backup vs. DLM vs. S3 Native vs. RDS Native

Understanding when to use AWS Backup versus native tools is tested heavily across **Domain 2, 3, and 4**.

```mermaid
graph TD
    Start["Backup Requirement?"] --> Q1{"Scope of Services to Protect?"}

    Q1 -- "Single Service Only" --> Q2{"Which Service?"}
    Q2 -- "EBS Snapshots / EC2 AMIs Only" --> DLM[["Amazon Data Lifecycle Manager (DLM)<br/>💾 Policy-based EBS/EC2 snapshots"]]
    Q2 -- "S3 Data Lake Buckets Only" --> S3Native[["Amazon S3 Versioning + CRR + S3 Lifecycle<br/>📦 Native object lifecycle & replication"]]
    Q2 -- "RDS / Aurora Databases Only" --> RDSNative[["RDS Automated Backups & Snapshots<br/>🗄️ Built-in 35-day PITR & multi-AZ"]]

    Q1 -- "Multi-Service Centralized Governance / Compliance" --> Q3{"Regulatory WORM / Multi-Account Vault?"}
    Q3 -- "Yes (WORM / Centralized Audit / Multi-Service)" --> AWSBackup[["AWS Backup<br/>🛡️ Centralized Cross-Service Governance<br/>🔒 AWS Backup Vault Lock (WORM)<br/>🌐 Cross-Account & Cross-Region"]]

    classDef single fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef multi fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class DLM,S3Native,RDSNative single;
    class AWSBackup multi;
```

### Detailed Feature Comparison

| Feature Dimension | AWS Backup | Amazon Data Lifecycle Manager (DLM) | S3 Native (Versioning / CRR) | RDS Native Backups |
| :--- | :--- | :--- | :--- | :--- |
| **Supported Services** | **15+ AWS Services** (S3, EBS, EFS, RDS, DDB, Redshift, FSx) | **EBS Volumes & EC2 AMIs only** | Amazon S3 only | Amazon RDS & Aurora only |
| **Centralized Console** | ✅ **Yes** (Single pane of glass across services) | ❌ No (EC2 console only) | ❌ No (S3 console only) | ❌ No (RDS console only) |
| **WORM Tamper Protection** | ✅ **Yes (Vault Lock Compliance Mode)** | ❌ No | ✅ Yes (S3 Object Lock) | ❌ No |
| **Cross-Account Replication** | ✅ **Yes** (AWS Organizations integrated) | ✅ Yes (EBS snapshots only) | ✅ Yes (S3 CRR / Batch Copy) | ⚠️ Manual snapshot share |
| **Automated Restore Testing** | ✅ **Yes** (AWS Backup Restore Testing) | ❌ No | ❌ No | ❌ No |
| **Compliance Auditing** | ✅ **Yes** (AWS Backup Audit Manager) | ❌ No | ❌ No | ❌ No |

---

## 7. Production Architecture Patterns for Data Engineers

### Pattern A: Ransomware-Resistant Air-Gapped Data Lake & Database Backup

- **Challenge**: Critical analytical tables in S3, DynamoDB, and RDS are vulnerable to compromised admin credentials or ransomware attacks deleting production databases.
- **Solution**:
  - Create a central **Backup Plan** in AWS Organizations with automated hourly/daily backups.
  - Configure a **Cross-Account Copy Rule** targeting a dedicated, air-gapped **Security/Archive AWS Account**.
  - Enforce **AWS Backup Vault Lock in Compliance Mode** on the destination vault with a 365-day retention policy.
- **Result**: Even if the primary workload AWS account is completely compromised or deleted, all recovery points remain untouched, immutable, and restorable from the security account.

```mermaid
graph LR
    subgraph PrimaryAcct["Primary Production Account"]
        ProdData[("Production Data<br/>S3 + RDS + DynamoDB + EFS")]
        PrimaryPlan["AWS Backup Plan"]
        ProdData --> PrimaryPlan
    end

    subgraph SecurityAcct["Air-Gapped Security / Archive Account"]
        SecVault[("Secured Backup Vault<br/>🔒 Vault Lock Compliance Mode<br/>🔑 Customer Managed KMS Key")]
        SecAudit["AWS Backup Audit Manager<br/>(Daily Compliance Reports)"]
        SecVault --- SecAudit
    end

    PrimaryPlan -->|"Automated Cross-Account Copy<br/>(Re-encrypted with Sec KMS Key)"| SecVault

    classDef primary fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef sec fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class ProdData,PrimaryPlan primary;
    class SecVault,SecAudit sec;
```

### Pattern B: Automated Restore Validation & RTO/RPO Compliance

- **Challenge**: Regulatory standards require verifying that backups are not corrupted and can meet strict Recovery Time Objectives (RTO).
- **Solution**:
  - Enable **AWS Backup Restore Testing**.
  - Configure automated restore plans that spin up isolated test instances (e.g., test RDS instance or test EFS file system), run synthetic data verification queries, and cleanly delete the test infrastructure.
  - Generate automated audit reports via **AWS Backup Audit Manager** to satisfy compliance auditors.

---

## 8. DEA-C01 Exam Tips, Pitfalls & Scenario Triggers

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
>
> - **"Centralized, automated policy-driven backup across multiple AWS services (S3, EBS, EFS, RDS, DynamoDB)"** $\rightarrow$ **AWS Backup**.
> - **"Prevent deletion or modification of backups by ANY user including the root user / ransomware protection / WORM"** $\rightarrow$ **AWS Backup Vault Lock in Compliance Mode**.
> - **"Allow authorized administrators to delete backups for cost control while preventing standard operators from doing so"** $\rightarrow$ **AWS Backup Vault Lock in Governance Mode**.
> - **"Automatically copy backups to an isolated secondary account in a different AWS Region"** $\rightarrow$ **AWS Backup Cross-Account & Cross-Region Copy with AWS Organizations**.
> - **"Continuously validate backup compliance and automated restore capabilities"** $\rightarrow$ **AWS Backup Audit Manager & Restore Testing**.
> - **"Automate snapshot schedules for EBS volumes and EC2 instances ONLY"** $\rightarrow$ **Amazon Data Lifecycle Manager (DLM)**.

> [!WARNING]
> **Exam Traps & Failure Modes**:
>
> 1. **Vault Lock Compliance Mode is Permanent**:
>    - Once the cooling-off period expires, Compliance Mode cannot be deleted by AWS account root or AWS Support. Do not select Compliance Mode if the requirement states administrators must be able to delete backups to reduce costs.
> 2. **Cross-Account KMS Key Requirement**:
>    - You cannot use AWS default managed keys (`aws/backup` or `aws/s3`) for cross-account backup copying. You **must use a Customer Managed Key (CMK)** with cross-account access granted in the KMS key policy.
> 3. **AWS Backup vs. DLM Scope**:
>    - DLM only handles EBS volumes and EC2 AMIs. If a scenario involves **EFS**, **RDS**, **DynamoDB**, or **S3**, DLM is incorrect; the answer must be **AWS Backup**.
> 4. **S3 Backup vs. S3 Versioning**:
>    - S3 Versioning protects against accidental deletes within the same bucket. AWS Backup for S3 provides centralized management, cross-account vault storage, and independent lifecycle retention outside the primary S3 bucket boundary.

---

## 📌 Related Notes

- [[kms-and-secrets]] — AWS KMS encryption keys, CMKs, and cross-account key policies
- [[lake-formation]] — Data Lake security, governance, and centralized access control
- [[macie-and-cloudtrail]] — Amazon Macie PII discovery and CloudTrail API auditing
- [[s3]] — Amazon S3 object storage and central Data Lake protection
- [[ebs-and-instance-store]] — Amazon EBS volume snapshots and lifecycle management
- [[efs-and-fsx]] — Amazon EFS and AWS FSx backup integrations
- [[ebs-vs-efs-vs-instance-store]] — Storage Decision Matrix (EFS vs. EBS vs. Instance Store)
- [[domain-4-data-security-and-governance]] — DEA-C01 Domain 4 Study Guide
- [[domain-2-data-store-management]] — DEA-C01 Domain 2 Study Guide
- [[domain-3-data-operations-and-support]] — DEA-C01 Domain 3 Study Guide
