---
title: AWS CDK, CloudFormation & SAM
type: aws-service
category: Developer Tools
tags:
  - aws/service
  - dea-c01
  - dev/iac
date: 2026-07-28
---

# 🏗️ AWS CDK, CloudFormation & SAM (Infrastructure as Code)

- **Category**: Developer Tools
- **Primary Use Case**: Infrastructure as Code (IaC), automated deployment of data pipelines, reproducible stack creation.
- **Slide Reference**: Pages 742–755 in [AWSCertifiedDataEngineerSlides.pdf](/docs/AWSCertifiedDataEngineerSlides.pdf)
- **Hub Links**: [[en/index|index]] | [[en/00-hub/service-catalog|service-catalog]] | [[en/01-domains/domain-3-data-operations-and-support|domain-3-data-operations-and-support]]

---

## 1. High-Level Summary
Deploying production data engineering pipelines requires Infrastructure as Code (IaC) to ensure consistent, repeatable, and version-controlled infrastructure across Development, Staging, and Production environments.

---

## 2. Tool Breakdown

| Tool | Format | Ideal Use Case |
| --- | --- | --- |
| **AWS CloudFormation** | Declarative JSON / YAML templates | Native AWS IaC stack deployment & rollback safety. |
| **AWS CDK (Cloud Development Kit)** | Imperative code (Python, TypeScript, Java) | Define data pipelines using familiar programming languages; compiles into CloudFormation templates. |
| **AWS SAM (Serverless Application Model)** | Shorthand YAML extending CloudFormation | Specialized framework for defining serverless Lambda, API Gateway, and DynamoDB resources. |

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Deploying standard pipeline resources across multiple regions programmatically**: Use **AWS CloudFormation StackSets**.
> - **Defining complex Glue / Step Functions pipelines in Python code**: Use **AWS CDK**.

---

## 📌 Related Notes
- [[en/02-services/compute-containers/lambda|lambda]] — SAM deployment target
- [[en/02-services/integration/step-functions/step-functions|step-functions]] — CDK workflow deployment
