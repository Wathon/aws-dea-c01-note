---
title: Amazon ECR, Amazon ECS & Amazon EKS (Containerized Workloads) (မြန်မာဘာသာ)
type: aws-service
category: Containers
tags:
  - aws/service
  - dea-c01
  - containers
  - ecr
  - ecs
  - eks
  - fargate
  - emr-on-eks
  - karpenter
  - burmese
date: 2026-08-15
---

# 🐳 Amazon ECR, Amazon ECS & Amazon EKS (Containers & Kubernetes on AWS) (AWS ပေါ်ရှိ ကွန်တိန်နာနှင့် Kubernetes ဝန်ဆောင်မှုများ)

- **Category**: Compute & Containers (Container Registry, Serverless Containers & Kubernetes Orchestration)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/compute-containers/ecr-ecs-eks.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: Container Images များကို Amazon ECR တွင် သိမ်းဆည်းခြင်း၊ Containerized Microservices နှင့် Data Pipelines များကို Amazon ECS (EC2/Fargate) ဖြင့် မောင်းနှင်ခြင်း၊ နှင့် Apache Spark Big Data Engine များကို **Amazon EMR on EKS** ဖြင့် Kubernetes Cluster ပေါ်တွင် ပူးတွဲ run ခြင်း။
- **Slide Reference**: Pages 313–330 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[batch]]` | `[[lambda]]` | `[[emr]]` | `[[efs-and-fsx]]` | `[[s3]]` | `[[glue]]` | `[[step-functions]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

Container နည်းပညာသည် Application Code၊ Runtime Environment၊ System Libraries များနှင့် Dependencies အားလုံးကို မည်သည့် Environment (Development, Testing, Cloud Production) တွင်မဆို စိတ်ချယုံကြည်စွာ ပြေးနိုင်သော စံသတ်မှတ်ထားသည့် ပေါ့ပါးသော Unit တစ်ခုအဖြစ် ထုပ်ပိုးပေးသည်။

AWS Data Engineering စနစ်များတွင် အဓိက အသုံးပြုသော ဝန်ဆောင်မှုများမှာ-
1. **Amazon Elastic Container Registry (Amazon ECR)**: Custom ETL Code များနှင့် Machine Learning Model Scoring Containers များကို လုံခြုံစွာ သိမ်းဆည်းပေးသည့် OCI-compliant Private Docker Registry ဖြစ်သည်။
2. **Amazon Elastic Container Service (Amazon ECS)**: AWS-native Container Orchestrator ဖြစ်ပြီး **Amazon EC2 Launch Type** (User-managed) နှင့် ဆာဗာစီမံရန်မလိုသော **AWS Fargate** (Serverless) နှစ်မျိုးစလုံးကို ထောက်ပံ့ပေးသည်။
3. **Amazon Elastic Kubernetes Service (Amazon EKS)**: Managed Kubernetes စနစ်ဖြစ်ပြီး အထူးသဖြင့် **Amazon EMR on EKS** (Apache Spark) ကို အခြား Web/API Microservices များနှင့်အတူ Shared Cluster ပေါ်တွင် ပူးတွဲ run ရန် အသုံးများသည်။
4. **AWS Fargate**: ECS နှင့် EKS နှစ်မျိုးစလုံးအတွက် အောက်ခံ EC2 Virtual Machines များကို Patching၊ Scaling ပြုလုပ်စရာမလိုဘဲ Container Task အလိုက်သာ တွက်ချက်ခွင့်ပြုသည့် Serverless Compute Engine ဖြစ်သည်။

```mermaid
graph TB
    subgraph DevLayer["(1) Build & Packaging Layer"]
        Dockerfile["Dockerfile / Application Code"]
        DockerBuild["docker build & tag (Multi-stage)"]
    end

    subgraph RegistryLayer["(2) Amazon ECR (Container Registry)"]
        ECRRepo[("Amazon ECR Repository<br/>🔒 Image Tag Immutability<br/>🔍 Amazon Inspector Vulnerability Scan<br/>♻️ Automated Lifecycle Policies<br/>🌐 Cross-Region Replication")]
    end

    subgraph OrchestrationLayer["(3) Container Orchestration Platforms"]
        subgraph ECSCluster["Amazon ECS (AWS Native)"]
            TaskDef["ECS Task Definition<br/>(vCPU, RAM, Secrets, awslogs)"]
            
            subgraph ECSCompute["Compute Options"]
                ECSFargate["AWS Fargate / Fargate Spot<br/>⚡ Serverless Containers<br/>💰 Pay per vCPU/RAM second"]
                ECSEC2["EC2 Launch Type<br/>🖥️ User-managed EC2 Fleet<br/>📦 Capacity Providers & Binpack"]
            end
        end

        subgraph EKSCluster["Amazon EKS (Managed Kubernetes)"]
            K8sControlPlane["Managed K8s Control Plane<br/>(Multi-AZ etcd & API Server)"]
            
            subgraph EKSNodes["Data Plane & Worker Compute"]
                ManagedNodes["Managed Node Groups (EC2 / Karpenter)"]
                EMRonEKS["Amazon EMR on EKS<br/>⚡ Apache Spark Container Pods<br/>👥 Multi-tenant Shared Cluster"]
            end
        end
    end

    subgraph StorageLayer["(4) Persistent & Object Storage"]
        S3Bucket[("Amazon S3 Data Lake<br/>(Parquet / Iceberg / Delta Lake)")]
        EFSFS[("Amazon EFS File System<br/>(NFSv4.1 Multi-AZ Shared Volume)")]
        EBSCSI[("Amazon EBS Volumes<br/>(RWO High-IOPS Block Storage)")]
    end

    Dockerfile --> DockerBuild
    DockerBuild -->|"docker push"| ECRRepo

    ECRRepo -->|"Pull Image via Task Execution Role"| ECSFargate
    ECRRepo -->|"Pull Image"| ECSEC2
    ECRRepo -->|"Pull Spark Runtime Image"| EMRonEKS

    TaskDef -.-> ECSFargate
    TaskDef -.-> ECSEC2

    ECSFargate <-->|"Task IAM Role"| S3Bucket
    ECSFargate <-->|"Mount via EFS Access Point"| EFSFS
    ECSEC2 <--> EFSFS
    ECSEC2 <--> EBSCSI

    EMRonEKS <-->|"EFS CSI / S3 Mountpoint"| EFSFS
    EMRonEKS <-->|"Read / Write Parquet"| S3Bucket
    ManagedNodes <--> EBSCSI

    classDef dev fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef ecr fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef ecs fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef eks fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class Dockerfile,DockerBuild dev;
    class ECRRepo ecr;
    class ECSCluster,TaskDef,ECSCompute,ECSFargate,ECSEC2 ecs;
    class EKSCluster,K8sControlPlane,EKSNodes,ManagedNodes,EMRonEKS eks;
    class S3Bucket,EFSFS,EBSCSI store;
```

---

## ၂။ Amazon Elastic Container Registry (Amazon ECR)

Amazon ECR သည် Container Images များကို လုံခြုံစွာ စီမံခန့်ခွဲပေးသည့် Fully Managed Registry ဖြစ်သည်-

```mermaid
graph LR
    Dev["Developer / CI/CD Pipeline"] -->|"(1) Authenticate (aws ecr get-login-password)"| ECR[("Amazon ECR Repository")]
    Dev -->|"(2) docker push (image:v1.0)"| ECR
    ECR -->|"(3) Automated Vulnerability Scan"| Inspector["Amazon Inspector / Enhanced Scan"]
    ECR -->|"(4) Lifecycle Rule (Expire > 30 days)"| Cleaner["Automated Image Purge"]
    ECR -->|"(5) Cross-Region Replication"| DRRegion[("ECR Replica (us-west-2)")]
    ECR -->|"(6) Pull Image at Runtime"| ECS_EKS["Amazon ECS / EKS / AWS Batch"]

    classDef dev fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef ecr fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef proc fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class Dev dev;
    class ECR,DRRegion ecr;
    class Inspector,Cleaner,ECS_EKS proc;
```

### အဓိက စွမ်းဆောင်ချက်များ:
1. **Image Tag Immutability**: Tag များ (`:prod`, `:v1.0`) ကို အသစ်ထပ်မံ Push လုပ်ခြင်းဖြင့် မတော်တဆ Overwrite မဖြစ်စေရန် တားဆီးပေးသည်။ Pipeline များအတွက် Deterministic Reproducible Runs များကို အာမခံသည်။
2. **Vulnerability Scanning (Amazon Inspector)**: Image Push လုပ်ချိန်တွင်သာမက CVE အသစ်များ ထွက်ပေါ်လာချိန်တိုင်း Continuous Vulnerability Scanning ပြုလုပ်ပေးသည်။
3. **Lifecycle Policies**: Tag မရှိသော သို့မဟုတ် သက်တမ်း ၃၀ ရက်ကျော်လွန်သော Image အဟောင်းများကို အလိုအလျောက် ရှင်းလင်းပေးခြင်းဖြင့် Storage Cost ကို ထိန်းချုပ်သည်။
4. **Private VPC Endpoints (Exam Critical)**: Private Subnet အတွင်းရှိ Tasks များမှ Internet/NAT Gateway မသုံးဘဲ ECR မှ Image ဆွဲယူရန် **Interface Endpoints (`ecr.api`, `ecr.dkr`)** နှင့် **Gateway Endpoint for Amazon S3** (Image Layer Blobs များ S3 တွင် သိမ်းဆည်းထားသဖြင့်) မဖြစ်မနေ လိုအပ်သည်။

---

## ၃။ Amazon Elastic Container Service (Amazon ECS)

### ၁။ Launch Types: EC2 vs. AWS Fargate

| Architectural Feature | AWS Fargate (Serverless) | AWS Fargate Spot | EC2 Launch Type |
| :--- | :--- | :--- | :--- |
| **Server Management** | **Zero Server Management** (ဆာဗာလုံးဝ စီမံစရာမလို) | **Zero Server Management** | **အသုံးပြုသူမှ EC2 Cluster စီမံရသည်** (OS, Patching, ASG) |
| **Pricing Model** | သုံးစွဲသည့် vCPU & Memory အလိုက် per-second ပေးချေရသည် | ပုံမှန် Fargate ထက် **၇၀% အထိ သက်သာသည်** | EC2 Instances များ run နေသရွေ့ အပြည့်ပေးချေရသည် |
| **Storage Persistence** | **Amazon EFS** (via Access Points) | **Amazon EFS** (via Access Points) | **Amazon EBS** သို့မဟုတ် **Amazon EFS** |
| **အကောင်းဆုံး DEA-C01 Fit** | **ခန့်မှန်းရခက်သော Spiky ETL Pipelines, Microservices** | **Stateless, Fault-tolerant Batch ETL with Checkpointing** | **၂၄/၇ အမြဲလည်ပတ်နေသော Sustained Workloads, Custom GPU Training** |

---

### ၂။ ECS IAM Role ခွဲခြားသတ်မှတ်မှု (Task Execution Role vs. Task Role - Core Exam Focus)

```mermaid
graph LR
    subgraph ECSService["Amazon ECS Agent & Fargate Infrastructure"]
        Agent["ECS Container Agent"]
    end

    subgraph ContainerRuntime["Running Application Container"]
        App["Data Engineering Application Code<br/>(Python / Spark / PyArrow)"]
    end

    subgraph IAMRoles["IAM Roles"]
        ExecRole["(1) Task Execution IAM Role<br/>(Infra & Lifecycle Permissions)"]
        TaskRole["(2) Task IAM Role<br/>(Application Data Permissions)"]
    end

    subgraph AWSTargets["AWS Destinations"]
        ECR[("Amazon ECR (Pull Image)")]
        CW["Amazon CloudWatch Logs (Write Logs)"]
        Secrets["AWS Secrets Manager / SSM (Read DB Password)"]
        S3Lake[("Amazon S3 (Read / Write Parquet)")]
        RedshiftDW[("Amazon Redshift (Data API / COPY)")]
        Dynamo[("Amazon DynamoDB")]
    end

    Agent -->|"Assumes"| ExecRole
    ExecRole --> ECR
    ExecRole --> CW
    ExecRole --> Secrets

    App -->|"Assumes"| TaskRole
    TaskRole --> S3Lake
    TaskRole --> RedshiftDW
    TaskRole --> Dynamo

    classDef comp fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef role fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef tgt fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class Agent,App comp;
    class ExecRole,TaskRole role;
    class ECR,CW,Secrets,S3Lake,RedshiftDW,Dynamo tgt;
```

- **Task Execution Role (`executionRoleArn`)**: **ECS Container Agent** ကိုယ်တိုင် အသုံးပြုသည်။ ECR မှ Image ဆွဲယူခြင်း (`ecr:BatchGetImage`)၊ CloudWatch သို့ Logs ရေးသားခြင်း (`logs:PutLogEvents`) နှင့် Secrets Manager မှ Database Password ရယူခြင်းများအတွက် သုံးသည်။
- **Task Role (`taskRoleArn`)**: Container အတွင်းရှိ **Data Application Code** က အသုံးပြုသည်။ Amazon S3 သို့ Parquet ရေးသားခြင်း (`s3:PutObject`)၊ DynamoDB Query လုပ်ခြင်း၊ Redshift Data API ခေါ်ယူခြင်းတို့အတွက် Permissions ပေးရသည်။

---

## ၄။ Amazon EMR on EKS (Core Big Data Exam Focus)

**Amazon EMR on EKS** သည် Apache Spark Big Data Workload များကို Managed EKS Kubernetes Cluster ပေါ်တွင် ပူးတွဲ မောင်းနှင်ပေးသည့် စနစ်ဖြစ်သည်-

```mermaid
graph TB
    subgraph EKSCluster["Shared Amazon EKS Cluster"]
        subgraph ProdNamespace["Namespace: production-web"]
            WebPods["Microservices & Web APIs"]
        end

        subgraph AnalyticsNamespace["Namespace: analytics-spark"]
            EMRVirtualCluster["EMR Virtual Cluster"]
            DriverPod["Spark Driver Pod"]
            ExecPod1["Spark Executor Pod 1"]
            ExecPod2["Spark Executor Pod 2"]
            ExecPod3["Spark Executor Pod 3"]
        end
    end

    subgraph AWSDataServices["Central AWS Data Layer"]
        GlueCatalog[("AWS Glue Data Catalog")]
        S3DataLake[("Amazon S3 Data Lake")]
    end

    EMRVirtualCluster --> DriverPod
    DriverPod -->|"Spawns Dynamically"| ExecPod1
    DriverPod -->|"Spawns Dynamically"| ExecPod2
    DriverPod -->|"Spawns Dynamically"| ExecPod3

    DriverPod <--> GlueCatalog
    ExecPod1 <-->|"Parallel Read / Write"| S3DataLake
    ExecPod2 <-->|"Parallel Read / Write"| S3DataLake
    ExecPod3 <-->|"Parallel Read / Write"| S3DataLake

    classDef k8s fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef spark fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef data fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class EKSCluster,ProdNamespace,AnalyticsNamespace,WebPods,EMRVirtualCluster k8s;
    class DriverPod,ExecPod1,ExecPod2,ExecPod3 spark;
    class GlueCatalog,S3DataLake data;
```

### EMR on EKS ကို အဘယ်ကြောင့် ရွေးချယ်သင့်သနည်း?
1. **Infrastructure Consolidation**: ကုမ္ပဏီတွင် ရှိပြီးသား Kubernetes Cluster ပေါ်တွင် Web App များနှင့်အတူ Apache Spark Data Pipelines များကို အတူတကွ မျှဝေသုံးစွဲနိုင်သဖြင့် Idle EC2 Cluster Waste ကို လုံးဝ ပပျောက်စေသည်။
2. **Dynamic Pod Lifecycle**: Job စတင်ချိန်တွင် Spark Driver နှင့် Executor Pods များကို အလိုအလျောက် တည်ဆောက်ပြီး Job ပြီးဆုံးပါက ချက်ချင်း ဖျက်သိမ်းပေးသည်။
3. **Up to 3x Faster**: Open-source Spark on K8s ထက် ၃ ဆ ပိုမိုမြန်ဆန်ပြီး ၆၈% စျေးသက်သာသည့် **EMR Runtime for Apache Spark** ကို အသုံးပြုသည်။

---

## ၅။ Master Comparative Matrix

| Dimension | AWS Lambda | AWS Batch | Amazon ECS (Fargate) | Amazon EKS (EMR on EKS) | Amazon EMR (EC2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Packaging** | Zip archive သို့မဟုတ် Container (10 GB) | Docker Container | Docker Container | Docker Container / K8s Pods | EC2 AMIs / Bootstrap Actions |
| **Max Runtime** | ⏱️ **15 Minutes** | Unlimited | Unlimited | Unlimited | Unlimited |
| **Orchestration** | AWS Event Triggers | Job Queues & Dependencies | ECS Task Definitions | Kubernetes Manifests / Helm | YARN ResourceManager |
| **Big Data Engine** | Custom Python scripts | Non-Spark batch containers | Custom container pipelines | **EMR Spark on Kubernetes** | Native Spark, Hadoop, Presto |
| **Storage Persistence** | `/tmp` (10 GB) သို့မဟုတ် EFS | EBS, Spot scratch, EFS | **Amazon EFS / Amazon EBS** | **EBS, EFS, FSx for Lustre, S3 CSI** | HDFS, S3 (EMRFS) |
| **Spot Cost Savings** | ❌ Standard duration pricing | ✅ **Native Spot integration** (90% off) | ✅ **Fargate Spot** (70% off) | ✅ **EC2 Spot Node Groups** (90% off) | ✅ **Spot Task nodes** (90% off) |

---

## ၆။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Run containerized applications without managing underlying EC2 servers"** $\rightarrow$ **Amazon ECS with AWS Fargate launch type**.
> - **"Share Kubernetes cluster resources between microservices and Apache Spark data engineering jobs"** $\rightarrow$ **Amazon EMR on EKS**.
> - **"Grant containerized application in ECS permissions to access S3 or DynamoDB"** $\rightarrow$ **Attach IAM policy to the ECS Task IAM Role** (Task Execution Role မဟုတ်ပါ!).
> - **"Prevent overwriting container images in CI/CD pipelines"** $\rightarrow$ **Enable Image Tag Immutability on Amazon ECR**.
> - **"Persistent shared multi-task file storage for Fargate containers"** $\rightarrow$ **Mount Amazon EFS via EFS Access Points**.

> [!WARNING]
> **Exam Traps (သတိထားရမည့် အချက်များ)**:
> 1. **Task Role vs. Task Execution Role Trap**: Container အတွင်းရှိ App က S3 ဖတ်မရဘဲ `AccessDenied` ဖြစ်နေပါက Task Execution Role ကို ပြင်ဆင်ခြင်းဖြင့် မဖြေရှင်းနိုင်ပါ။ **Task IAM Role** တွင် `s3:GetObject` ပေးရမည်။
> 2. **EMR on EC2 vs. EMR on EKS**: ရှိပြီးသား K8s Cluster ကို မျှဝေသုံးလိုပါက **EMR on EKS** ကို ရွေးပါ။ Custom Hadoop/YARN ကန့်သတ်ချက်များ သို့မဟုတ် Dedicated Cluster လိုအပ်ပါက **EMR on EC2** ကို ရွေးပါ။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[batch]]` — AWS Batch (Managed Containerized Batch Computing)
- `[[lambda]]` — AWS Lambda (Serverless Functions)
- `[[emr]]` — Amazon EMR Distributed Big Data Clusters
- `[[efs-and-fsx]]` — Amazon EFS Storage Integration with Containers
- `[[s3]]` — Amazon S3 Data Lake Target
- `[[glue]]` — AWS Glue Serverless Spark ETL
