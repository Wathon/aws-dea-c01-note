---
title: Amazon EFS & AWS FSx
type: aws-service
category: Storage
tags:
  - aws/service
  - dea-c01
  - storage/file
  - efs
  - fsx
  - lustre
date: 2026-08-09
---

# 📁 Amazon EFS & AWS FSx (Lustre, ONTAP, Windows, OpenZFS)

- **Category**: Storage (Shared Managed File Systems)
- **Primary Use Case**: Shared POSIX file storage for distributed Linux compute clusters, container persistent volumes ([[ecr-ecs-eks]]), serverless functions ([[lambda]]), and ultra-high-throughput HPC / ML data staging from [[s3]].
- **Slide Reference**: Pages 139–154 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-2-data-store-management]] | [[s3]] | [[ebs-and-instance-store]]

---

## 1. High-Level Summary

Shared file storage allows hundreds to thousands of concurrent compute instances (EC2, ECS tasks, EKS pods, Lambda functions, and on-premises servers) to access a single, shared, POSIX-compliant file system simultaneously over standard network protocols (**NFSv4** for EFS; **Lustre / SMB / NFS** for FSx).

For the **AWS Certified Data Engineer – Associate (DEA-C01)** exam, you must distinguish when to use:
1. **Amazon EFS**: Fully managed, serverless, Multi-AZ elastic file storage for standard Linux workloads, containers, Lambda, and cross-AZ shared directories.
2. **AWS FSx for Lustre**: Ultra-high-performance parallel file storage optimized for compute-heavy workloads (HPC, distributed machine learning, video rendering, big data analytics) with **native, bi-directional synchronization with Amazon S3**.
3. **AWS FSx for NetApp ONTAP / Windows / OpenZFS**: Enterprise multi-protocol storage, native Windows SMB environments, and ZFS-powered workflows.

```mermaid
graph TB
    subgraph ComputeLayer["Compute Layer (Multi-AZ & Hybrid)"]
        EC2Node["EC2 Linux Instances<br/>(Cluster Compute / Spark)"]
        EKSContainers["Amazon ECR / ECS / EKS<br/>(Container Stateful Volumes)"]
        Serverless["AWS Lambda Functions<br/>(Serverless ML / ETL)"]
        OnPrem["On-Premises Servers<br/>(via Direct Connect / VPN)"]
    end

    subgraph EFSArch["Amazon EFS (Multi-AZ Elastic File System)"]
        AP["EFS Access Points<br/>(POSIX UID/GID Enforcement + Root Directory Jailing)"]
        MT1["Mount Target (AZ-a)"]
        MT2["Mount Target (AZ-b)"]
        MT3["Mount Target (AZ-c)"]
        
        subgraph EFSTiers["EFS Tiering (Intelligent-Tiering / Lifecycle)"]
            StandardTier[("EFS Standard<br/>⚡ Low Latency SSD")]
            IATier[("EFS Infrequent Access (IA)<br/>💰 92% Lower Storage Cost")]
            ArchiveTier[("EFS Archive<br/>📦 Cold Compliance Data")]
        end
    end

    subgraph FSxArch["AWS FSx for Lustre (HPC & ML Staging)"]
        LustreCluster[("FSx for Lustre Parallel FS<br/>⚡ Hundreds of GB/s Throughput<br/>⚡ Sub-millisecond Latency")]
        S3Bucket[("Amazon S3 Data Lake<br/>📦 Automated Hydration & Export<br/>(Data Repository Association)")]
    end

    EC2Node -->|"NFSv4 (Port 2049) + TLS"| AP
    EKSContainers -->|"NFSv4 + TLS"| AP
    Serverless -->|"NFSv4 + TLS"| AP
    OnPrem -->|"Direct Connect / VPN"| AP
    AP --> MT1
    AP --> MT2
    AP --> MT3
    MT1 --> StandardTier
    MT2 --> StandardTier
    MT3 --> StandardTier
    StandardTier <-->|"Lifecycle Policy"| IATier
    IATier <-->|"Cold Policy"| ArchiveTier

    EC2Node <-->|"POSIX Lustre Protocol"| LustreCluster
    EKSContainers <-->|"POSIX Lustre Protocol"| LustreCluster
    LustreCluster <-->|"Bi-directional Sync (DRA)"| S3Bucket

    classDef compute fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef fsx fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef s3 fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class EC2Node,EKSContainers,Serverless,OnPrem compute;
    class AP,MT1,MT2,MT3,StandardTier,IATier,ArchiveTier efs;
    class LustreCluster fsx;
    class S3Bucket s3;
```

---

## 2. Amazon EFS Architecture & Core Components

Amazon EFS provides elastic, serverless file storage that grows and shrinks automatically as files are added and removed, requiring zero storage provisioning or management.

```mermaid
graph LR
    subgraph VPC["Customer Amazon VPC"]
        subgraph SubnetA["Subnet AZ-a (10.0.1.0/24)"]
            EC2_A["EC2 Instance A"]
            MT_A["Mount Target A<br/>IP: 10.0.1.50"]
            EC2_A <-->|"NFSv4.1"| MT_A
        end
        subgraph SubnetB["Subnet AZ-b (10.0.2.0/24)"]
            EC2_B["EC2 Instance B"]
            MT_B["Mount Target B<br/>IP: 10.0.2.50"]
            EC2_B <-->|"NFSv4.1"| MT_B
        end
        subgraph SubnetC["Subnet AZ-c (10.0.3.0/24)"]
            LambdaC["AWS Lambda / ECS"]
            MT_C["Mount Target C<br/>IP: 10.0.3.50"]
            LambdaC <-->|"NFSv4.1"| MT_C
        end
    end

    subgraph EFSService["Amazon EFS Regional Storage Layer"]
        StorageEngine[("EFS Distributed Storage<br/>11 9's Durability across 3+ AZs")]
    end

    MT_A & MT_B & MT_C --- StorageEngine

    classDef vpc fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef target fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class EC2_A,EC2_B,LambdaC vpc;
    class MT_A,MT_B,MT_C target;
    class StorageEngine efs;
```

### Key Architectural Elements

1. **Mount Targets**:
   - To mount an EFS file system from an EC2 instance, container, or Lambda function, you create a **Mount Target** in each Availability Zone where compute resources reside.
   - Each Mount Target provides an IP address and a DNS name (e.g., `fs-12345678.efs.us-east-1.amazonaws.com`).
   - Clients in AZ-a communicate with the Mount Target in AZ-a to avoid cross-AZ data transfer fees and minimize latency.
   - **Security Group**: Attached to the Mount Target. Must allow inbound **TCP Port 2049 (NFS)** from the compute security group or subnet CIDR.

2. **EFS Access Points (Crucial for Lambda & Containers)**:
   - Application-specific entry points into an EFS file system that enforce fine-grained access control, identity masking, and directory isolation.
   - **POSIX Identity Enforcement**: Overrides client-provided identity and forces all requests through the access point to use a specific POSIX user ID (`UID`), group ID (`GID`), and secondary GIDs.
   - **Root Directory Jailing**: Enforces a specific sub-directory path as the virtual root (e.g., `/export/app1`), preventing clients from accessing parent directories or files owned by other applications.
   - **Automatic Directory Creation**: Automatically creates the designated root directory with specified owner permissions if it does not exist when the client mounts.
   - **Exam Significance**: EFS Access Points are **mandatory** when mounting EFS to **AWS Lambda** and recommended for multi-tenant **Amazon ECS / EKS** deployments.

3. **EFS Mount Helper (`amazon-efs-utils`)**:
   - An open-source package providing the `mount.efs` command.
   - Automates mounting by file system ID, enforces **TLS in-transit encryption** (via `stunnel`), and supports IAM authentication tokens.

---

## 3. EFS Storage Classes & Automated Lifecycle Tiering

EFS offers multiple storage classes to balance performance and cost. Files can automatically migrate across tiers using **EFS Lifecycle Management** and **EFS Intelligent-Tiering**.

```mermaid
graph TD
    Write["File Created / Written"] --> Standard["EFS Standard Tier<br/>(High Frequency Access / Millisecond Latency)"]
    
    Standard -->|"No access for X days<br/>(e.g., 7, 14, 30, 60, 90 days)"| IA["EFS Infrequent Access (IA) Tier<br/>(Up to 92% cheaper storage + read/write access fee)"]
    
    IA -->|"No access for Y days<br/>(e.g., 90, 180, 270 days)"| Archive["EFS Archive Tier<br/>(Lowest cost storage for cold compliance)"]
    
    IA -->|"File Read / Modified<br/>(EFS Intelligent-Tiering Enabled)"| Standard
    Archive -->|"File Read / Modified<br/>(EFS Intelligent-Tiering Enabled)"| Standard

    classDef std fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef ia fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef arch fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;

    class Standard std;
    class IA ia;
    class Archive arch;
```

### Storage Classes Comparison Matrix

| Storage Class | Availability / Durability | Redundancy Scope | Storage Cost (Approx.) | Access Fee | Optimal Workload |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EFS Standard** | 99.99% / 11 9's | **Multi-AZ** (3+ AZs) | ~$0.30 / GB-mo | None | Active data, web serving, ETL staging, container root volumes |
| **EFS Infrequent Access (IA)** | 99.99% / 11 9's | **Multi-AZ** (3+ AZs) | ~$0.025 / GB-mo (92% savings) | ~$0.01 / GB read | Files accessed a few times per month |
| **EFS Archive** | 99.99% / 11 9's | **Multi-AZ** (3+ AZs) | ~$0.008 / GB-mo (Lowest Multi-AZ) | ~$0.03 / GB read | Cold historical data, regulatory archives accessed < few times/year |
| **EFS One Zone** | 99.9% / 11 9's (Single AZ) | **Single AZ** | ~$0.16 / GB-mo (47% savings vs Standard) | None | Non-critical dev/test, replicated build artifacts, single-AZ apps |
| **EFS One Zone-IA** | 99.9% / 11 9's (Single AZ) | **Single AZ** | ~$0.0133 / GB-mo | ~$0.01 / GB read | Infrequently accessed single-AZ dev/test datasets |

### Lifecycle Policies & Intelligent-Tiering

1. **Transition into IA / Archive**:
   - Moves files that have not been read or modified for a configured period: `1, 7, 14, 30, 60, 90, 180, 270, or 365 days`.
2. **Transition out of IA / Archive (Intelligent-Tiering)**:
   - **Without Intelligent-Tiering**: Reading a file in IA leaves it in IA (incurring repeated access charges on subsequent reads).
   - **With Intelligent-Tiering (Recommended)**: Reading a file in IA or Archive **automatically restores it to EFS Standard**, protecting against runaway access charges during unexpected burst read patterns.

---

## 4. EFS Performance Modes & Throughput Modes

Choosing the correct combination of **Performance Mode** and **Throughput Mode** is critical for both pipeline performance and cost optimization on the DEA-C01 exam.

```mermaid
graph TD
    subgraph PerfMode["(1) Performance Modes (Set at Creation - Immutable)"]
        GP["General Purpose (Default)<br/>⚡ Lowest per-operation latency (< 1ms)<br/>⚡ Best for web serving, dev notebooks, containers"]
        MaxIO["Max I/O<br/>⚡ Scale to tens of thousands of IOPS<br/>⚡ Higher metadata latency (multi-ms)<br/>⚡ Best for massive parallel scale-out big data"]
    end

    subgraph ThroughputMode["(2) Throughput Modes (Dynamic - Modifiable Live)"]
        Elastic["Elastic (Recommended Default)<br/>📈 Automatically scales up/down with demand<br/>📈 Up to 3 GB/s read, 1 GB/s write (Multi-AZ)<br/>📈 Pay only for data read/written"]
        Bursting["Bursting Throughput<br/>📊 Throughput scales linearly with storage (50 KB/s per GB)<br/>📊 Accumulates burst credits (up to 100 MB/s+)<br/>⚠️ Small file systems deplete burst credits quickly!"]
        Provisioned["Provisioned Throughput<br/>🎯 Dedicated fixed throughput (e.g., 500 MB/s)<br/>🎯 Independent of stored capacity<br/>🎯 Extra hourly charge for provisioned MB/s"]
    end

    classDef pmode fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef tmode fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class GP,MaxIO pmode;
    class Elastic,Bursting,Provisioned tmode;
```

### Performance Modes

- **General Purpose (Recommended Default)**:
  - Delivers the lowest latency per file operation (sub-millisecond for metadata and read operations).
  - Recommended for almost all standard data workloads, container shared disks, and interactive web servers.
- **Max I/O**:
  - Scales to virtually unlimited aggregate throughput and tens of thousands of IOPS.
  - Incurs a slight latency penalty (multi-millisecond) for individual metadata operations (`ls`, `stat`, `mkdir`).
  - Recommended only for massive parallel scale-out compute clusters (hundreds of parallel Spark / MapReduce nodes simultaneously querying the file system).

### Throughput Modes

| Throughput Mode | Scaling Model | Max Throughput Limits | Cost Structure | Best Data Engineering Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Elastic (Default)** | Auto-scales instantly based on read/write I/O | **3 GB/s Read, 1 GB/s Write** (Multi-AZ)<br/>(Up to 10 GB/s in select regions) | Pay per GB transferred ($0.03/GB read, $0.06/GB write) + base storage | **Spiky, unpredictable ETL pipelines, periodic batch jobs, serverless functions.** |
| **Bursting** | Baseline scales at $50 \text{ KB/s per GB}$; bursts to $100 \text{ MB/s}$ using burst credits | Dependent on total stored volume size | Included in base storage price | Steady workloads with large storage footprints (> 1 TiB) where baseline throughput suffices. |
| **Provisioned** | Fixed throughput provisioned manually (e.g. 200 MB/s) | Up to 3,000 MB/s | Charged for provisioned MB/s above baseline | Small storage footprint (< 50 GB) requiring sustained high throughput (e.g., streaming ingest buffer). |

> [!WARNING]
> **Bursting Credit Exhaustion Trap**:
> If a file system is small (e.g., 10 GB), its baseline throughput is only $500 \text{ KB/s}$. If a heavy ETL job runs against it, the file system will exhaust its burst credits within minutes, throttling the pipeline down to $500 \text{ KB/s}$. **Solution**: Switch to **Elastic Throughput** or **Provisioned Throughput**.

---

## 5. EFS Security, Encryption & Access Control

EFS provides defense-in-depth security across network boundaries, IAM permissions, and POSIX file access.

```mermaid
graph TD
    subgraph Layer1["(1) Network Layer (VPC & Mount Targets)"]
        SG["Mount Target Security Group<br/>(Inbound: TCP Port 2049 from Client SG)"]
    end

    subgraph Layer2["(2) IAM Authorization Layer (EFS File System Policy)"]
        FSPolicy["File System Policy<br/>(ClientMount / ClientWrite / ClientRootAccess)"]
    end

    subgraph Layer3["(3) Application Access Point Layer"]
        AccessPoint["EFS Access Point<br/>(POSIX UID/GID Masking & Root Path Jailing)"]
    end

    subgraph Layer4["(4) Operating System Layer"]
        POSIX["POSIX File System Permissions<br/>(User / Group / Others rwx)"]
    end

    subgraph Layer5["(5) Cryptographic Layer"]
        KMS["AWS KMS Encryption at Rest (AES-256)"]
        TLS["TLS 1.2 In-Transit Encryption (stunnel)"]
    end

    SG --> FSPolicy --> AccessPoint --> POSIX
    POSIX -.-> KMS
    POSIX -.-> TLS

    classDef sec fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef crypto fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class SG,FSPolicy,AccessPoint,POSIX sec;
    class KMS,TLS crypto;
```

### 1. Encryption
- **Encryption at Rest**: Enabled during creation using [[kms-and-secrets]] (AWS KMS CMK or AWS-managed key `aws/elasticfilesystem`). All metadata and file contents are encrypted transparently with zero performance impact.
- **Encryption in Transit**: Uses industry-standard **TLS 1.2** managed automatically when mounting via `amazon-efs-utils` (using the `-o tls` mount flag).

### 2. IAM Policies for NFS Clients
EFS supports IAM file system resource policies to grant or restrict specific actions:
- `elasticfilesystem:ClientMount`: Allows read-only mounting of the file system.
- `elasticfilesystem:ClientWrite`: Allows writing to the file system.
- `elasticfilesystem:ClientRootAccess`: Controls whether the client can access the file system as `root` (UID 0) or is squashed to anonymous user.

### Example EFS IAM File System Policy (Enforcing Read-Only and In-Transit Encryption)

```json
{
  "Version": "2012-10-17",
  "Id": "EFSReadOnlyAndSecurePolicy",
  "Statement": [
    {
      "Sid": "EnforceTLS",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "*",
      "Resource": "arn:aws:elasticfilesystem:us-east-1:123456789012:file-system/fs-12345678",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    },
    {
      "Sid": "AllowMountAndWriteForRole",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/DataEngineeringETLRole"
      },
      "Action": [
        "elasticfilesystem:ClientMount",
        "elasticfilesystem:ClientWrite"
      ],
      "Resource": "arn:aws:elasticfilesystem:us-east-1:123456789012:file-system/fs-12345678"
    }
  ]
}
```

---

## 6. AWS FSx File Systems Family Deep Dive

AWS FSx provides fully managed, purpose-built, high-performance third-party and open-source file systems.

```mermaid
graph TD
    Root["AWS FSx Family"] --> Lustre["AWS FSx for Lustre<br/>⚡ High Performance Compute (HPC)<br/>⚡ Machine Learning & AI Training<br/>⚡ Native S3 Hydration / Data Lake"]
    Root --> ONTAP["AWS FSx for NetApp ONTAP<br/>🏢 Enterprise Multi-Protocol (NFS, SMB, iSCSI)<br/>🏢 NetApp SnapMirror / Deduplication"]
    Root --> Win["AWS FSx for Windows File Server<br/>🪟 Native Windows SMB / NTFS<br/>🪟 Active Directory Integration"]
    Root --> OpenZFS["AWS FSx for OpenZFS<br/>🐧 Linux POSIX with ZFS snapshots<br/>⚡ Microsecond latencies & high IOPS"]

    classDef fsx fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;
    class Lustre,ONTAP,Win,OpenZFS fsx;
```

### 1. AWS FSx for Lustre (Top Exam Focus for DEA-C01)

Lustre is an open-source parallel file system designed for compute-intensive workloads that require sub-millisecond latencies, hundreds of gigabytes per second of throughput, and millions of IOPS.

```mermaid
sequenceDiagram
    autonumber
    participant S3 as Amazon S3 (Data Lake)
    participant FSx as AWS FSx for Lustre
    participant Compute as Distributed GPU / Compute Nodes (EC2 / EMR)

    Note over S3,FSx: Data Repository Association (DRA) configured
    Compute->>FSx: 1. Request file access (POSIX open / read)
    FSx->>S3: 2. Lazy load / Hydrate objects on-demand (or pre-load metadata)
    FSx-->>Compute: 3. Stream data at Hundreds of GB/s (sub-ms latency)
    Compute->>FSx: 4. Write processed output / checkpoint files to Lustre
    FSx->>S3: 5. Auto-export / Data Repository Task exports results back to S3
```

#### Key FSx for Lustre Features

1. **Native Amazon S3 Integration (Data Repository Association - DRA)**:
   - FSx for Lustre can link directly to an Amazon S3 bucket.
   - When created, Lustre imports S3 metadata (object keys appear as POSIX files/folders).
   - **Lazy Loading**: When compute nodes read a file, FSx transparently loads the bytes from S3 on first access.
   - **Data Repository Tasks (DRT)**: Can export modified or new files from FSx back to S3 (either automatically via export policies or explicitly via API/CLI).
2. **Deployment Options**:
   - **Scratch File Systems**: Designed for temporary, ephemeral compute workloads. No data replication across disks (if a storage server fails, uncommitted data is lost). Highest raw burst throughput at lowest cost.
   - **Persistent File Systems**: Designed for long-running workloads. Data is replicated within the same AZ; failed file servers are replaced transparently. Available with SSD storage or HDD storage (with optional SSD read caches).

### 2. AWS FSx for NetApp ONTAP
- Fully managed shared storage built on NetApp's popular ONTAP file system.
- Supports **multi-protocol access** (NFS, SMB, and iSCSI) to the same data volume simultaneously.
- Offers enterprise storage features: instant snapshotting, deduplication, compression, thin provisioning, and replication with on-premises NetApp clusters via **SnapMirror**.
- Automatically tiers cold data from fast SSDs to a low-cost capacity pool.

### 3. AWS FSx for Windows File Server
- Fully managed native Microsoft Windows file system accessed over the **SMB (Server Message Block)** protocol.
- Integrates natively with Microsoft Active Directory (AD), DFS Namespaces, and Windows Access Control Lists (ACLs).
- Available in Single-AZ or Multi-AZ deployments with automatic failover.

### 4. AWS FSx for OpenZFS
- Managed OpenZFS file system providing POSIX-compliant shared storage for Linux applications.
- Delivers up to 1 million IOPS and latencies under 0.5 milliseconds.
- Features instant point-in-time ZFS snapshots, data cloning, and on-the-fly compression.

---

## 7. Storage Decision Matrix: S3 vs. EBS vs. EFS vs. FSx for Lustre

Understanding the architectural boundaries between AWS storage solutions is tested heavily in **Domain 2 (Data Store Management)**.

```mermaid
graph TD
    Start["Storage Decision Needed"] --> Q1{"Shared across multiple<br/>compute nodes / containers?"}

    Q1 -- "No (Dedicated Single Node)" --> Q2{"Persistence across<br/>instance stop required?"}
    Q2 -- "No (Ephemeral)" --> InstStore[["EC2 Instance Store (NVMe)<br/>⚡ Spark Shuffle / Spill Disks / Temp Cache"]]
    Q2 -- "Yes (Persistent)" --> EBS[["Amazon EBS (gp3 / io2 / st1)<br/>💾 Block storage for databases / broker logs"]]

    Q1 -- "Yes (Shared Storage)" --> Q3{"Access Protocol & Interface?"}
    Q3 -- "REST API / Object Store" --> S3[["Amazon S3 / S3 Express One Zone<br/>📦 Central Data Lake / Bronze-Silver-Gold"]]
    Q3 -- "POSIX File System" --> Q4{"Workload Type & Throughput SLA?"}
    
    Q4 -- "General Linux / Multi-AZ / Serverless" --> EFS[["Amazon EFS (NFSv4.1)<br/>📁 Elastic Multi-AZ / Lambda / ECS / EKS"]]
    Q4 -- "HPC / ML Training / Massive Parallel S3" --> Lustre[["AWS FSx for Lustre<br/>⚡ Sub-ms / Hundreds of GB/s / S3 Linked"]]
    Q4 -- "Windows SMB / Active Directory" --> Win[["AWS FSx for Windows<br/>🪟 Native Windows / SMB / DFS"]]
    Q4 -- "Multi-Protocol / NetApp Migration" --> ONTAP[["AWS FSx for NetApp ONTAP<br/>🏢 NFS + SMB + iSCSI / SnapMirror"]]

    classDef s3 fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;
    classDef ebs fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef fsx fill:#0f172a,stroke:#f59e0b,stroke-width:2px,color:#fff;

    class S3 s3;
    class EBS,InstStore ebs;
    class EFS efs;
    class Lustre,Win,ONTAP fsx;
```

### Comprehensive Storage Comparison Matrix

| Dimension | Amazon S3 | Amazon EBS | Amazon EFS | AWS FSx for Lustre | EC2 Instance Store |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Storage Type** | Object Storage | Block Storage | Distributed File System | Parallel File System | Ephemeral Host Block |
| **Protocol** | HTTPS (REST API) | Block device (PCIe/NVMe over fabric) | **NFSv4.0 / NFSv4.1** | **Lustre POSIX** | Direct PCIe / NVMe |
| **Multi-Node Concurrency** | Millions of clients | Single instance (`io2` Multi-Attach up to 16 in same AZ) | **Thousands of clients** | **Thousands of clients** | Single instance only |
| **Multi-AZ Availability** | Multi-AZ (Standard) or Single-AZ (Express) | **Single AZ strictly** | **Multi-AZ (Standard)** or Single-AZ (One Zone) | **Single AZ** (Linked to Multi-AZ S3) | **Physical Host only** |
| **Latency** | ~10–50 ms (Single-digit ms on Express One Zone) | Low ms down to sub-ms (`io2`) | Low ms (< 1ms metadata on GP) | **Sub-millisecond** | **Sub-millisecond (Fastest)** |
| **Throughput Capacity** | Virtually unlimited (3,500 PUT / 5,500 GET per prefix) | Up to 4,000 MB/s (`io2 Block Express`) | **Up to 3+ GB/s (Elastic)** | **Hundreds of GB/s** | Highest raw physical bus throughput |
| **Capacity Sizing** | Infinite auto-scaling | Pre-provisioned volume size (up to 64 TiB) | **Elastic auto-scaling** (PBs) | Provisioned cluster size | Fixed by EC2 instance type |
| **S3 Direct Integration** | Native | Snapshot backup to S3 | AWS DataSync / AWS Backup | **Native Lazy-Loading & Auto-Export** | Custom replication scripts |
| **Primary DEA-C01 Role** | Central Data Lake, Bronze/Silver/Gold tiers | Databases, Kafka broker logs, stateful compute | Shared web/notebook dirs, Lambda state, container PVs | **HPC, ML model training, EMR high-speed staging** | Spark shuffle space, MapReduce spills, temp cache |

---

## 8. Data Engineering Architecture Patterns

### Pattern A: Serverless Machine Learning Inference with AWS Lambda & Amazon EFS

- **Challenge**: Machine learning inference models (e.g., PyTorch, Hugging Face NLP transformers) exceed the 250 MB Lambda deployment package limit and the 10 GB ephemeral `/tmp` storage limit.
- **Solution**: Mount an **Amazon EFS** file system to the AWS Lambda function via an **EFS Access Point**.
- **Architecture**:
  - The EFS Access Point enforces UID/GID and maps to `/models`.
  - The Lambda execution environment mounts the EFS directory at cold start.
  - Large pre-trained model weights (e.g., 20 GB) are loaded directly into Lambda memory on initialization.

```mermaid
graph LR
    Lambda["AWS Lambda Function<br/>(Serverless ETL / Inference)"] -->|"Mounts via EFS Access Point<br/>(VPC Inbound TCP 2049)"| AP["EFS Access Point<br/>(/models path)"]
    AP --> MT["EFS Mount Target"]
    MT --> EFS[("Amazon EFS<br/>(20 GB PyTorch Model Weights)")]

    classDef lambda fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef efs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    class Lambda lambda;
    class AP,MT,EFS efs;
```

### Pattern B: Ultra-Fast Distributed ML Training & EMR Staging with FSx for Lustre + S3

- **Challenge**: Training distributed deep learning models or running heavy geospatial analytics directly against S3 causes bottlenecked GET requests and high network latencies.
- **Solution**: Spin up an **AWS FSx for Lustre** cluster with a Data Repository Association pointing to the S3 Data Lake.
- **Architecture**:
  - Compute worker nodes read training images/tensors at sub-millisecond latencies across hundreds of gigabytes per second.
  - Model checkpoints and evaluation metrics are written directly to Lustre.
  - An **FSx Data Repository Task** automatically syncs output files back to Amazon S3.
  - Once training completes, the FSx for Lustre cluster is deleted (saving cost) while persistent data remains safely in S3.

### Pattern C: Multi-Tenant Analytics & JupyterHub on Amazon EKS

- **Challenge**: Hundreds of data scientists require isolated home directories and shared dataset folders with persistent storage across pod restarts.
- **Solution**: Deploy the **Amazon EFS CSI Driver** on Amazon EKS using dynamic volume provisioning with **EFS Access Points**.
- **Architecture**:
  - Each data scientist pod gets a dedicated Access Point root directory (`/users/user-123`) with enforced POSIX permissions.
  - Common read-only datasets are mounted from a shared path (`/data/curated-features`).

---

## 9. DEA-C01 Exam Tips, Pitfalls & Scenarios

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
>
> - **"Shared POSIX file system across multiple Linux EC2 instances, Lambda functions, or ECS/EKS containers"** $\rightarrow$ **Amazon EFS**.
> - **"Serverless file system that automatically grows and shrinks without provisioning"** $\rightarrow$ **Amazon EFS with Elastic Throughput**.
> - **"High Performance Computing (HPC), distributed ML model training, or sub-millisecond parallel file system linked to Amazon S3"** $\rightarrow$ **AWS FSx for Lustre**.
> - **"Enforce POSIX identity, directory isolation, or mount shared file system to AWS Lambda"** $\rightarrow$ **EFS Access Points**.
> - **"Migrate Windows file share using SMB, NTFS, and Active Directory integration"** $\rightarrow$ **AWS FSx for Windows File Server**.
> - **"Multi-protocol (NFS + SMB + iSCSI) with NetApp SnapMirror migration"** $\rightarrow$ **AWS FSx for NetApp ONTAP**.

> [!WARNING]
> **Common Exam Traps & Pitfalls**:
>
> 1. **EFS vs. EBS Multi-Attach**:
>    - EBS Multi-Attach (`io1`/`io2`) is strictly **Single-AZ** and limited to up to 16 Nitro instances, requiring a cluster-aware file system (like GFS2).
>    - If multi-AZ sharing or thousands of concurrent Linux clients are required, the answer is **Amazon EFS**, not EBS Multi-Attach.
> 2. **EFS Network Mounting Trap**:
>    - Clients cannot connect to EFS directly over the public Internet. On-premises servers must connect via **AWS Direct Connect** or **AWS Site-to-Site VPN** through the VPC Mount Target.
>    - The Mount Target security group must allow inbound **TCP Port 2049** from client security groups.
> 3. **Bursting Mode Exhaustion**:
>    - Small EFS file systems on **Bursting Throughput** will throttle once burst credits are exhausted. If an exam scenario describes unexpected I/O bottlenecks on small datasets, recommend switching to **Elastic Throughput** or **Provisioned Throughput**.
> 4. **FSx for Lustre Scratch vs. Persistent**:
>    - **Scratch**: Best for temporary/batch compute where S3 holds the durable data.
>    - **Persistent**: Best for longer-running jobs requiring intra-AZ disk replication and automated high availability.
> 5. **EFS File Deletion & Resizing**:
>    - Unlike EBS (which only grows), EFS automatically shrinks when files are deleted, reducing your monthly storage bill automatically.

---

## 📌 Related Notes

- [[s3]] — Persistent object storage and Data Lake architecture
- [[ebs-and-instance-store]] — Amazon EBS volume types and EC2 Instance Store
- [[ecr-ecs-eks]] — Containerized compute and persistent volume mounting
- [[lambda]] — Serverless data processing and EFS integration
- [[emr]] — Big data processing clusters and storage options
- [[datasync-and-snow]] — AWS DataSync for NFS/EFS automated migrations
- [[kms-and-secrets]] — AWS KMS keys and file system encryption
- [[service-comparisons]] — Service decision matrix (S3 vs EBS vs EFS vs FSx)
- [[ebs-vs-efs-vs-instance-store]] — Deep Dive: Amazon EFS vs. EBS vs. EC2 Instance Store
- [[domain-2-data-store-management]] — DEA-C01 Domain 2 Study Guide
