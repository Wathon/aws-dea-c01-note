---
title: Amazon QuickSight Security, Row/Column-Level Security (RLS/CLS) & VPC Governance
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/quicksight
  - row-level-security
  - column-level-security
  - vpc-connections
  - iam-identity-center
date: 2026-08-19
---

# 🛡️ Amazon QuickSight Security, Row/Column-Level Security (RLS/CLS) & VPC Governance

- **Category**: Analytics / Governance, Multi-Tenant Security & Network Isolation
- **Language / ဘာသာစကား**: **English (Original)** | [မြန်မာဘာသာ (Burmese)](/mm/02-services/analytics-streaming/quicksight/quicksight-security-rls-and-governance)
- **Primary Use Case**: Restricting dashboard rows and columns based on user identity (RLS & CLS), connecting to private databases via QuickSight VPC connections, and managing enterprise SSO with IAM Identity Center.
- **Slide Reference**: Pages 479–498 in `[AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)`
- **Hub Links**: `[[en/index|index]]` | `[[en/02-services/analytics-streaming/quicksight/quicksight|quicksight]]` | `[[en/02-services/database/redshift|redshift]]` | `[[en/02-services/database/rds-and-aurora|rds-and-aurora]]` | `[[en/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]]`

---

## 1. High-Level Summary

Enterprise business intelligence requires strict data governance to ensure users only access the exact subset of records and attributes authorized for their role.

Amazon QuickSight provides multi-layered governance through **User-Based Row-Level Security (RLS)**, **Tag-Based RLS for Multi-Tenant Embedding**, **Column-Level Security (CLS)** to mask PII, and **Amazon QuickSight VPC Connections** to query private databases without internet exposure.

```mermaid
graph TD
    subgraph GovernanceLayers["QuickSight Multi-Layer Security Architecture"]
        subgraph NetSec["(1) Network Isolation"]
            VPC_Conn["QuickSight VPC Connection<br/>• Managed ENIs in Private Subnets<br/>• Zero Public Internet Exposure"]
        end

        subgraph DataSec["(2) Data Access Governance"]
            RLS["Row-Level Security (RLS)<br/>• User-Based: Permissions Dataset<br/>• Tag-Based: Session Tags for Multi-Tenant"]
            CLS["Column-Level Security (CLS)<br/>• Masks sensitive fields (Salary, SSN)"]
        end

        subgraph IdSec["(3) Identity & Access Management"]
            SSO["AWS IAM Identity Center / SAML 2.0<br/>(Corporate Active Directory / Okta / Entra ID)"]
        end
    end

    classDef net fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef dat fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#0f172a;
    classDef id fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class VPC_Conn net;
    class RLS,CLS dat;
    class SSO id;
```

---

## 2. Row-Level Security (RLS) Deep Dive

Row-Level Security restricts the rows of data visible to a user or group when viewing an analysis or dashboard:

```mermaid
graph LR
    UserLogin["(1) User Logs In (e.g. 'alice@company.com')"] --> RLS_Rules["(2) QuickSight Evaluates RLS Permissions Dataset"]
    RLS_Rules --> Filter["(3) Applies Filter: Region = 'NorthAmerica'"]
    Filter --> Render["(4) Renders Dashboard with Alice's Regional Rows Only"]

    classDef step fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef eval fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef out fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class UserLogin step;
    class RLS_Rules,Filter eval;
    class Render out;
```

### 1. User-Based RLS (Permissions Dataset)
You create a dedicated permissions dataset containing `UserName` or `GroupName` columns alongside data filter columns:

| UserName | GroupName | Region | Segment |
| :--- | :--- | :--- | :--- |
| `alice` | | `NorthAmerica` | `Enterprise` |
| `bob` | | `EMEA` | |
| | `SalesLeadership` | | |

- **Alice**: Sees only records where `Region = 'NorthAmerica'` AND `Segment = 'Enterprise'`.
- **Bob**: Sees all segments for `Region = 'EMEA'` (leaving `Segment` blank matches all segments).
- **SalesLeadership Group**: Sees all regions and all segments (unrestricted access).

---

### 2. Tag-Based RLS (for Multi-Tenant Embedded Analytics)
When embedding dashboards into customer-facing SaaS applications:
- Avoid creating thousands of individual QuickSight user accounts.
- Use **AWS STS Session Tags** (e.g. `TenantId: Customer_A`) passed during `GenerateEmbedUrlForRegisteredUser` or `GenerateEmbedUrlForAnonymousUser` API calls.
- QuickSight dynamically filters dataset rows matching the session tag.

---

## 3. Column-Level Security (CLS)

**Column-Level Security (CLS)** restricts access to specific sensitive columns within a dataset:

```mermaid
graph TD
    Dataset["Enterprise HR Dataset (Employees, Department, Salary, SSN)"]

    Dataset --> UserA["Standard HR Reader (Alice)"]
    Dataset --> UserB["Executive HR Admin (Bob)"]

    UserA --> VisualA["Dashboard Visual:<br/>• Employee Name ✅<br/>• Department ✅<br/>• Salary: [Excluded / Unavailable] 🚫"]
    UserB --> VisualB["Dashboard Visual:<br/>• Employee Name ✅<br/>• Department ✅<br/>• Salary: $145,000 ✅"]

    classDef ds fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef u fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef v fill:#dcfce7,stroke:#16a34a,stroke-width:1px,color:#0f172a;

    class Dataset ds;
    class UserA,UserB u;
    class VisualA,VisualB v;
```

- You configure CLS on the dataset edit screen by selecting sensitive fields (e.g. `Salary`, `SocialSecurityNumber`) and assigning them to an authorized IAM / QuickSight group (`ExecutiveLeadership`).
- Unauthorized users can still view the dashboard, but protected columns are omitted from queries and visual calculations without breaking dashboard rendering.

---

## 4. Private VPC Connections for Database Ingestion

By default, Amazon QuickSight runs inside an AWS-managed service VPC. If your Amazon RDS, Aurora, or Redshift clusters are located in **private subnets with no public internet access**, QuickSight cannot connect over public IPs.

```mermaid
graph LR
    subgraph QS_Managed["AWS-Managed QuickSight VPC"]
        QS_Engine["QuickSight Engine"]
    end

    subgraph Cust_VPC["Customer VPC (10.0.0.0/16)"]
        subgraph PrivSubnet["Private Subnet (10.0.1.0/24)"]
            ENI["QuickSight Elastic Network Interface (ENI)"]
            DB[("Amazon RDS / Redshift Cluster<br/>(Port 5432 / 5439)")]
        end
    end

    QS_Engine -->|"QuickSight VPC Connection"| ENI
    ENI -->|"VPC Security Group Rules"| DB

    classDef qs fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#0f172a;
    classDef vpc fill:#e0f2fe,stroke:#0284c7,stroke-width:1px,color:#0f172a;
    classDef db fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#0f172a;

    class QS_Engine qs;
    class ENI,PrivSubnet vpc;
    class DB db;
```

### Configuration Steps:
1. Create a **QuickSight VPC Connection** specifying the VPC ID, Subnet IDs, and Security Group.
2. QuickSight provisions dedicated **Elastic Network Interfaces (ENIs)** in your private subnets.
3. Configure the database Security Group to allow inbound traffic from the QuickSight Security Group on the database port.

---

## 5. DEA-C01 Exam Essentials

> [!IMPORTANT]
> **Key Exam Decision Triggers for QuickSight Security**:
>
> - **"Ensure sales managers can only view sales data for their specific region on a shared enterprise dashboard"** $\rightarrow$ Configure **User-Based Row-Level Security (RLS)** with a permissions dataset.
> - **"Embed dashboards into a multi-tenant SaaS portal where external tenants must only see their own company data without individual IAM logins"** $\rightarrow$ Implement **Tag-Based Row-Level Security (RLS)** using STS session tags.
> - **"Prevent unauthorized financial analysts from seeing employee salary figures in a shared dataset"** $\rightarrow$ Enable **Column-Level Security (CLS)** on the `Salary` field.
> - **"QuickSight fails to connect to an Amazon RDS PostgreSQL instance in a private subnet"** $\rightarrow$ Create an **Amazon QuickSight VPC Connection** and verify security group ingress rules on port 5432.

---

## 📌 Related Notes
- `[[en/02-services/analytics-streaming/quicksight/quicksight|quicksight]]` — QuickSight Master Hub
- `[[en/02-services/analytics-streaming/quicksight/quicksight-spice-engine|quicksight-spice-engine]]` — SPICE In-Memory Engine
- `[[en/02-services/database/redshift|redshift]]` — Securing Amazon Redshift Clusters
- `[[en/02-services/database/rds-and-aurora|rds-and-aurora]]` — Private VPC Database Connectivity
