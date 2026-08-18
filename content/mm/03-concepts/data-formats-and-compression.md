---
title: Data Formats & Compression Codecs (မြန်မာဘာသာ)
type: concept
tags:
  - concept/data-engineering
  - dea-c01
  - data-formats
  - compression
  - storage-optimization
  - burmese
date: 2026-08-15
---

# 📄 Data Formats & Compression Codecs (ဒေတာဖော်မတ်များနှင့် ဖိသိပ်မှုစနစ်များ)

- **Category**: Fundamentals / Storage & Query Optimization
- **Language / ဘာသာစကား**: [English Version](/en/03-concepts/data-formats-and-compression) | **မြန်မာဘာသာ (Burmese)**
- **Slide Reference**: Pages 38–48 in `[[AWSCertifiedDataEngineerSlides.pdf]]`
- **Hub Links**: `[[index]]` | `[[service-catalog]]` | `[[athena]]` | `[[glue]]` | `[[redshift]]` | `[[emr]]` | `[[s3]]`

---

## ၁။ Row-Based vs. Columnar Storage Formats (အတန်းလိုက် vs ကော်လံလိုက် သိမ်းဆည်းမှု ပုံစံများ)

Big Data Analytics တွင် သိုလှောင်မှု ကုန်ကျစရိတ်၊ I/O Bandwidth နှင့် Query တွက်ချက်မှု အမြန်နှုန်းတို့သည် ဒေတာဖော်မတ် ရွေးချယ်မှုအပေါ် များစွာ မူတည်ပါသည်-

```mermaid
graph TD
    subgraph RowLayout["(1) Row-Based Storage (CSV / JSON / Avro)"]
        R1["Row 1: ID=1, Name=Alice, Age=25, Country=US"]
        R2["Row 2: ID=2, Name=Bob,   Age=30, Country=UK"]
        R3["Row 3: ID=3, Name=Carol, Age=28, Country=CA"]
    end

    subgraph ColumnarLayout["(2) Columnar Storage (Apache Parquet / ORC)"]
        C1["IDs Block: [1, 2, 3...]"]
        C2["Names Block: ['Alice', 'Bob', 'Carol'...]"]
        C3["Ages Block: [25, 30, 28...] (Stats: Min=25, Max=30)"]
        C4["Countries Block: ['US', 'UK', 'CA'...]"]
    end

    classDef r fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef c fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class RowLayout,R1,R2,R3 r;
    class ColumnarLayout,C1,C2,C3,C4 c;
```

### အဓိက ကွာခြားချက်များနှင့် သဘောတရားများ:
1. **Row-Based Storage (အတန်းလိုက် သိမ်းဆည်းခြင်း - CSV, JSON, Avro)**:
   - ဒေတာ Record တစ်ခုလုံးကို Memory / Disk ပေါ်တွင် ဆက်တိုက်သိမ်းဆည်းသည်။
   - **အားသာချက်**: Record အသစ်များ အဆက်မပြတ် ထည့်သွင်းခြင်း (High-write transaction / Append-heavy OLTP) အတွက် မြန်ဆန်သည်။
   - **အားနည်းချက်**: ကော်လံ ၁ ခုတည်းကို ခွဲခြမ်းစိတ်ဖြာ တွက်ချက်ရန် (ဥပမာ `SELECT AVG(Age)`) ဒေတာဖိုင်တစ်ခုလုံးရှိ ကော်လံအားလုံးကို ဖတ်ရှုရသဖြင့် I/O ကုန်ကျစရိတ် မြင့်မားသည်။
2. **Columnar Storage (ကော်လံလိုက် သိမ်းဆည်းခြင်း - Apache Parquet, Apache ORC)**:
   - တူညီသော Column မှ Data များကို Disk ပေါ်တွင် အတူတကွ စုစည်းသိမ်းဆည်းသည်။
   - **အားသာချက်များ**:
     - **Column Projection**: မေးမြန်းထားသော ကော်လံများကိုသာ ရွေးချယ်ဖတ်ရှုနိုင်သည် (Selective reading)။
     - **Superior Compression**: တူညီသော ဒေတာအမျိုးအစား (Data types) များ စုစည်းနေသဖြင့် Compression ပိုမိုကောင်းမွန်ပြီး သိုလှောင်မှု ၇၅% မှ ၉၀% အထိ သက်သာစေသည်။
     - **Predicate Pushdown & Statistics**: Data Block တစ်ခုချင်းစီတွင် Min/Max တန်ဖိုးများ ပါရှိသဖြင့် `WHERE` clause နှင့် မသက်ဆိုင်သော Block များကို ကျော်ဖတ်နိုင်သည်။

---

## ၂။ Data Formats နှိုင်းယှဉ်ချက် ဇယား (Complete Format Matrix)

| Data Format | Storage Layout | Schema Type | Splittable? (ခွဲခြမ်းနိုင်မှု) | အဓိက အသုံးပြုသည့်နေရာ (Best AWS Fit) |
| :--- | :--- | :--- | :--- | :--- |
| **CSV / TSV** | Row-based (Plain Text) | Schema-on-Read | ✅ Yes (Uncompressed ဖြစ်ပါက) | Raw Data Landing၊ လူကိုယ်တိုင် စစ်ဆေးရန်ဖိုင်များ |
| **JSON** | Row-based (Plain Text) | Semi-Structured | ⚠️ Multiline (No) / JSON Lines (Yes) | API Payload များ၊ Web Logs၊ Event Streaming |
| **Apache Avro** | Row-based (Binary) | Schema In-File Header | ✅ **Yes** | **Amazon MSK (Kafka)** Streaming၊ Schema Evolution၊ High-write Row Ops |
| **Apache Parquet** | **Columnar** (Binary) | Self-describing schema | ✅ **Yes** | **Amazon Athena, AWS Glue, EMR Spark, Redshift Spectrum (Default Analytical Choice)** |
| **Apache ORC** | **Columnar** (Binary) | Self-describing schema | ✅ **Yes** | Apache Hive၊ Presto on Amazon EMR၊ အဆင့်မြင့် Indexing |

---

## ၃။ Compression Codecs & Splittability Mechanics (ဖိသိပ်မှုနှင့် ခွဲခြမ်းနိုင်မှု သဘောတရား)

Distributed Computing (Hadoop, Spark, Athena) တွင် ဖိုင်ကြီးများကို Worker Node များစွာပေါ်သို့ ခွဲခြမ်းကာ **Parallel Computing** ဖြင့် တွက်ချက်ရသဖြင့် Compression Codec ၏ **Splittability** သည် အလွန်အရေးကြီးပါသည်-

```mermaid
graph LR
    subgraph NonSplittable["Non-Splittable (Gzip / Snappy on raw text)"]
        GZ["Single Large Compressed File (10 GB .gz)"] -->|"Single Stream"| Worker1["Worker Node 1<br/>(Bottleneck: Must process entire 10 GB alone)"]
    end

    subgraph Splittable["Splittable (Parquet Snappy / Bzip2 / Zstd)"]
        Split["Splittable File (10 GB Parquet)"] --> Block1["Block 0-2 GB"] --> W1["Worker Node 1"]
        Split --> Block2["Block 2-4 GB"] --> W2["Worker Node 2"]
        Split --> Block3["Block 4-6 GB"] --> W3["Worker Node 3"]
    end

    classDef s1 fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff;
    classDef s2 fill:#0f172a,stroke:#22c55e,stroke-width:2px,color:#fff;

    class NonSplittable,GZ,Worker1 s1;
    class Splittable,Split,Block1,Block2,Block3,W1,W2,W3 s2;
```

### Compression Codecs နှိုင်းယှဉ်ချက် ဇယား:

| Compression Codec | Splittable? | Compression Ratio | CPU Processing Speed | အကြံပြုထားသော AWS အသုံးချမှု |
| :--- | :--- | :--- | :--- | :--- |
| **Snappy** | ❌ No *(Parquet အတွင်း Row Group အလိုက် Split ရပါသည်)* | အသင့်အတင့် (Moderate) | ⚡ **Ultra Fast (အလွန်မြန်)** | **Parquet / Glue / Athena / Spark အတွက် Default ရွေးချယ်မှု** |
| **Gzip** | ❌ **No (လုံးဝ Splittable မဟုတ်ပါ)** | မြင့်မားသည် (High) | အသင့်အတင့် (Moderate) | Single-file Log Archiving၊ HTTP Payload များ |
| **Zstandard (Zstd)** | ✅ **Yes (Splittable)** | အလွန်မြင့်မားသည် (High) | 🚀 Fast (အလွန်မြန်) | ခေတ်မီ Parquet ဖိုင်များနှင့် S3 Cold Storage |
| **Bzip2** | ✅ **Yes (Splittable)** | အမြင့်ဆုံး (Maximum) | 🐢 Slow (နှေးကွေးသည်) | Raw Text ဖိုင်ကြီးများကို Split လုပ်ရန် မဖြစ်မနေ လိုအပ်သည့်နေရာများ |

---

## ၄။ DEA-C01 စာမေးပွဲ အဓိက မေးခွန်းပုံစံများနှင့် ထောင်ချောက်များ (Exam Tips & Traps)

> [!IMPORTANT]
> **စာမေးပွဲတွင် မဖြစ်မနေ မှတ်သားရမည့် အချက်များ (Top Exam Triggers)**:
> - **"Convert S3 data to optimize Athena query performance and reduce S3 scan costs"** $\rightarrow$ **Apache Parquet + Snappy compression**.
> - **"Streaming ingestion format for Kafka / Amazon MSK with evolving schema"** $\rightarrow$ **Apache Avro**.
> - **"Parallel processing of large compressed text datasets"** $\rightarrow$ **Bzip2** (သို့မဟုတ် Parquet with Snappy/Zstd သို့ ပြောင်းလဲခြင်း)။

> [!WARNING]
> **Exam Traps (သတိထားရမည့် ထောင်ချောက်များ)**:
> - **The Gzip Splittability Trap**: Raw CSV/JSON ဖိုင်ကြီးများကို **Gzip** ဖြင့် Compress လုပ်ထားပါက Spark နှင့် Athena တို့သည် ဖိုင်ကို Worker Node များစွာသို့ ခွဲခြမ်းမဖတ်နိုင်ဘဲ Core ၁ ခုတည်းကသာ Sequential ဖတ်ရသဖြင့် အလွန်နှေးကွေးစေသည်။
> - **Snappy on Raw Text Trap**: Snappy ကို Raw Text ပေါ်တွင် အသုံးပြုပါက Splittable မဖြစ်ပါ။ Parquet/ORC Block Container အတွင်း ထည့်သွင်းမှသာ Splittable ဖြစ်သည်။

---

## 📌 ဆက်စပ် မှတ်စုများ (Related Notes)

- `[[big-data-fundamentals]]` — Big Data 5 V's နှင့် Data Lake Architecture
- `[[data-modeling-and-partitioning]]` — S3 Partition Prefix များနှင့် Data Modeling
- `[[athena]]` — Amazon Athena ဖြင့် Parquet ဒေတာများကို Query ပြုလုပ်ခြင်း
- `[[glue]]` — AWS Glue ETL ဖြင့် ဖော်မတ်ပြောင်းလဲခြင်း (CSV $\rightarrow$ Parquet)
- `[[msk-kafka]]` — Amazon MSK Avro Serialization နှင့် Schema Registry
