---
title: SQL Review & Version Control (Git)
type: concept
tags:
  - concept/data-engineering
  - dea-c01
  - sql
date: 2026-07-28
---

# 📊 SQL Review & Version Control (Git)

- **Category**: Fundamentals
- **Slide Reference**: Pages 51–75 in [[AWSCertifiedDataEngineerSlides.pdf]]
- **Hub Links**: [[index]] | [[service-catalog]]

---

## 1. SQL Window Functions Review

Window functions perform calculations across a set of table rows related to the current row without collapsing rows like `GROUP BY`:

```sql
SELECT 
    employee_id,
    department_id,
    salary,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank,
    AVG(salary) OVER (PARTITION BY department_id) as dept_avg_salary
FROM employees;
```

- `ROW_NUMBER()`: Unique sequential integer assigned to each row within a partition.
- `RANK()`: Rank with gaps for ties (1, 2, 2, 4).
- `DENSE_RANK()`: Rank without gaps for ties (1, 2, 2, 3).
- `LAG(col, offset)` / `LEAD(col, offset)`: Access row data from prior or subsequent rows in partition.

---

## 2. SQL Join Types Matrix

| Join Type | Description |
| --- | --- |
| **INNER JOIN** | Returns only rows where key matches in both tables. |
| **LEFT OUTER JOIN** | Returns all rows from left table + matched rows from right table (NULLs if missing). |
| **RIGHT OUTER JOIN**| Returns all rows from right table + matched rows from left table. |
| **FULL OUTER JOIN** | Returns all rows when there is a match in either left or right table. |
| **CROSS JOIN** | Cartesian product of both tables (combination of every row). |

---

## 3. Git Version Control Fundamentals

- **Data Pipeline Versioning**: Storing DDLs, Glue scripts, Lambda functions, and Airflow DAGs in Git repositories.
- **Commands**: `git commit`, `git push`, `git branch`, `git merge`, `git rebase`, `git fsck` (verify integrity of database object store).

---

## 📌 Related Notes
- [[athena]] — Executing ANSI SQL queries in Athena
- [[redshift]] — Redshift SQL functions & join optimization
