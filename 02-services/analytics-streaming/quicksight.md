---
title: Amazon QuickSight
type: aws-service
category: Analytics
tags:
  - aws/service
  - dea-c01
  - analytics/quicksight
date: 2026-07-28
---

# 📊 Amazon QuickSight (Business Intelligence & Dashboards)

- **Category**: Analytics / BI
- **Primary Use Case**: Cloud-scale business intelligence, interactive dashboards, ML Insights, paginated reporting.
- **Slide Reference**: Pages 479–498 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]] | [[domain-3-data-operations-and-support]]

---

## 1. High-Level Summary
Amazon QuickSight is a cloud-powered business intelligence (BI) service that delivers fast, interactive insights and visualizations to users across an organization.

---

## 2. Key Features & SPICE Engine

### SPICE (Superfast, Parallel, In-memory Calculation Engine)
- In-memory engine designed to achieve fast query performance on large datasets without hitting underlying database data stores. Automatically refreshed on schedule or via API.

### Row-Level Security (RLS) & Column-Level Security (CLS)
- Restricts dataset access based on user credentials (e.g. Regional managers can only see sales data for their own region).

### QuickSight Q & ML Insights
- Natural language query interface ("What were top sales in Q3?") and automated anomaly detection / forecasting.

---

## 3. DEA-C01 Exam Tips

> [!IMPORTANT]
> - **Fast Visualization Performance on Large Datasets**: Import data into **SPICE** in QuickSight.
> - **User-Based Access Control in Dashboards**: Enforce **Row-Level Security (RLS)** with User/Group mapping tables.

---

## 📌 Related Notes
- [[athena]] — Athena data source for QuickSight
- [[redshift]] — Redshift data warehouse source for QuickSight
