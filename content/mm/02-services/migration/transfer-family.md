---
title: AWS Transfer Family (မြန်မာဘာသာ)
type: aws-service
category: Migration
tags:
  - aws/service
  - dea-c01
  - migration/transfer-family
  - sftp
  - ftps
  - ftp
  - as2
  - storage/file-transfer
  - burmese
date: 2026-08-15
---

# 📂 AWS Transfer Family (Managed SFTP, FTPS, FTP & AS2) (စီမံခန့်ခွဲပေးထားသော ဖိုင်လွှဲပြောင်းမှု ဝန်ဆောင်မှု)

- **Category**: Migration & Transfer (B2B Partner File Exchange & Managed File Transfer)
- **Language / ဘာသာစကား**: [English Version](file:///home/monetine/Workspace/Wathon/aws-dea-c01/content/en/02-services/migration/transfer-family.md) | **မြန်မာဘာသာ (Burmese)**
- **အဓိက အသုံးပြုမှု**: ပြင်ပ B2B Partners များနှင့် လုပ်ငန်းသုံး စနစ်ဟောင်းများမှ ဖိုင်များကို **SFTP, FTPS, FTP, AS2** စံသတ်မှတ်ချက်များဖြင့် `[[s3]]` Data Lakes နှင့် `[[efs-and-fsx]]` (Amazon EFS) ထဲသို့ ဆာဗာ စီမံခန့်ခွဲစရာမလိုဘဲ တိုက်ရိုက် လွှဲပြောင်းပေးပို့ခြင်း။
- **Slide Reference**: Pages 284–285 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[mm/index]]` | `[[en/index]]` | `[[s3]]` | `[[efs-and-fsx]]` | `[[datasync-and-snow]]`

---

## ၁။ အကျဉ်းချုပ် (High-Level Summary)

**AWS Transfer Family** သည် **SFTP** (SSH File Transfer Protocol)၊ **FTPS** (FTP over SSL)၊ **FTP** (VPC-only) နှင့် **AS2** (B2B Electronic Data Interchange) စသည့် လုပ်ငန်းသုံး ဖိုင်လွှဲပြောင်းမှု ပရိုတိုကောများကို အသုံးပြု၍ ဒေတာများကို **Amazon S3** နှင့် **Amazon EFS** ပေါ်သို့ တိုက်ရိုက် လွှဲပြောင်းပေးနိုင်သည့် Fully Managed, Multi-AZ ဝန်ဆောင်မှု ဖြစ်သည်။

```mermaid
graph TB
    subgraph ExternalClients["External Clients & Legacy Systems"]
        SFTPClient["External B2B Partners<br/>(SFTP Client / Port 22)"]
        FTPSClient["Enterprise Systems<br/>(FTPS Client / Port 21/990)"]
        InternalFTP["Internal Legacy Servers<br/>(Plain FTP / Port 21 - VPC Only)"]
    end

    subgraph AuthLayer["Identity & Authentication Providers"]
        AD["Microsoft Active Directory / LDAP"]
        CustomAuth["Custom Lambda Authorizer<br/>(Okta / Cognito / Secrets Manager)"]
        ServiceUsers["Service-Managed SSH Keys"]
    end

    subgraph TransferCluster["AWS Transfer Family (Multi-AZ Managed Fleet)"]
        Route53["Amazon Route 53<br/>(Custom Domain DNS: sftp.company.com)"]
        TransferEndpoint["Transfer Family Server Endpoint<br/>(Public IP / VPC Interface Endpoint)"]
        IAMRole["Assumed IAM Role<br/>(Scoped Down S3 / EFS Permissions)"]
    end

    subgraph StorageTargets["Storage Backends"]
        S3Bucket[("Amazon S3 Data Lake<br/>(Objects natively stored)")]
        EFSFS[("Amazon EFS File System<br/>(POSIX directory tree)")]
    end

    SFTPClient --> Route53
    FTPSClient --> Route53
    InternalFTP --> TransferEndpoint

    Route53 --> TransferEndpoint
    TransferEndpoint <--> AuthLayer
    TransferEndpoint --> IAMRole

    IAMRole --> S3Bucket
    IAMRole --> EFSFS

    classDef ext fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef auth fill:#0f172a,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef tf fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef store fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class ExternalClients,SFTPClient,FTPSClient,InternalFTP ext;
    class AuthLayer,AD,CustomAuth,ServiceUsers auth;
    class TransferCluster,Route53,TransferEndpoint,IAMRole tf;
    class StorageTargets,S3Bucket,EFSFS store;
```

---

## ၂။ Protocols & Security Architecture

1. **SFTP (SSH File Transfer Protocol - Port 22)**: Public Key Authentication သို့မဟုတ် Password ဖြင့် ချိတ်ဆက်သည်။ အသုံးအများဆုံး စံစနစ် ဖြစ်သည်။
2. **FTPS (FTP over TLS - Ports 21/990)**: TLS Certificate ဖြင့် Encrypted လုပ်ထားသော FTP ဖြစ်သည်။
3. **FTP (Plaintext FTP - Port 21)**: လုံခြုံရေးအရ **VPC Endpoints အတွင်းသာ အသုံးပြုခွင့် ကန့်သတ်ထားသည်** (Public Internet ပေါ်တွင် မရပါ)။
4. **AS2 (Applicability Statement 2 - Port 443)**: EDI စာရွက်စာတမ်းများ လဲလှယ်ရာတွင် သုံးပြီး MDN (Message Disposition Notification) ဖြင့် အရောက်ပို့ အတည်ပြုချက် ရရှိသည်။

---

## ၃။ DEA-C01 စာမေးပွဲ အဓိက အချက်အလက်များနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **Key Exam Trigger Keywords**:
> - **"Secure SFTP / FTPS file transfer directly into Amazon S3 data lake or Amazon EFS without managing servers"** $\rightarrow$ **AWS Transfer Family**.
> - **"Integrate external partners via SFTP using Active Directory or custom authentication (Okta/Cognito)"** $\rightarrow$ **AWS Transfer Family with custom Lambda authorizer or AWS Directory Service**.
> - **"Plaintext FTP support"** $\rightarrow$ **AWS Transfer Family with VPC-hosted endpoint** (Public FTP is not permitted).

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[s3]]` — Amazon S3 Data Lake Integration
- `[[efs-and-fsx]]` — Amazon EFS POSIX Storage
- `[[datasync-and-snow]]` — AWS DataSync (High-speed Network Transfer)
