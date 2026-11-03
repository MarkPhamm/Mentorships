# Warehouse: OLTP, OLAP and the lakehouse

← Back to the [data stack guide](../README.md)

The warehouse is where data is stored and queried for analysis. To pick one, and to answer the interview question "why not just use Postgres?", you need to know the difference between the two kinds of database.

## OLTP vs OLAP

| | OLTP (transactional) | OLAP (analytical) |
|---|---|---|
| **Built for** | Running the app: one order, one user, one payment at a time | Analysing the business: millions of rows at once |
| **Typical query** | `SELECT * FROM orders WHERE order_id = 123` | `SELECT month, SUM(revenue) FROM orders GROUP BY month` |
| **Storage** | Row-oriented: a whole row stored together | Column-oriented: each column stored together, so summing one column reads only that column |
| **Writes** | Many small inserts and updates per second | Big batch loads |
| **Examples** | Postgres, MySQL, SQL Server | Snowflake, BigQuery, Redshift, Databricks SQL, DuckDB, ClickHouse |

**The rule:** OLTP is where data is born (the [source](../1-sources/README.md)). OLAP is where you analyse it. You don't run heavy analytics on the app's production database, because you'd slow down the app. That's why [ingestion](../2-ingestion/README.md) copies it out.

Postgres is fine as a warehouse for a small project. Just know why it's not what companies use at scale, and say so in your README.

## Warehouse vs lake vs lakehouse

| | Warehouse | Data lake | Lakehouse |
|---|---|---|---|
| **What it is** | A managed database for analytics | Files (Parquet, JSON) in object storage | Files in object storage, with a table format that adds warehouse features |
| **Strength** | Fast SQL, easy, governed | Cheap, any format, any size | Cheap open storage, plus transactions, schema and time travel |
| **Weakness** | Cost; your data sits in a vendor's format | No transactions or schema: turns into a "data swamp" | More moving parts to run |
| **Examples** | Snowflake, BigQuery, Redshift | S3 + Parquet | Iceberg or Delta Lake on S3, queried by Trino, Spark or Databricks |

A lakehouse is a good DE project because it makes you assemble the pieces a warehouse hides: storage, a table format, a catalogue and a query engine. For more depth, read [The internals of BigQuery, Snowflake, Databricks and Redshift](https://vutr.substack.com/p/the-internal-of-bigquery-snowflake) and [Build a lakehouse on a laptop](https://vutr.substack.com/p/build-a-lakehouse-on-a-laptop-with).

## Which one for your project

| Situation | Pick |
|---|---|
| Local project, anyone can clone and run it | **DuckDB.** Free, one file, fast, reads Parquet directly |
| You want cloud experience on your resume | **Snowflake** (free trial) or **BigQuery** (free tier). Check which one your target job posts ask for |
| Real-time analytics on streaming data | **ClickHouse** |
| DE project on open table formats | **Lakehouse:** MinIO + Iceberg + Trino, in Docker |

Watch the bill. Set a budget alert or auto-suspend before you load anything into a cloud warehouse.

## By role

- **Data engineer:** know OLTP vs OLAP, columnar storage, partitioning and clustering, and cost. A lakehouse project shows depth.
- **Analytics engineer:** know your warehouse's SQL dialect, how it charges, and how materialisations (view, table, incremental) affect cost and speed.
- **Data analyst:** know why you query the warehouse, not the app database, and how to write SQL that doesn't scan the whole table.

## In my projects

- **Snowflake:** [Skytrax](https://github.com/MarkPhamm/skytrax_reviews_transformation), with users, roles, schemas and warehouses managed in Terraform.
- **DuckDB:** [local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline), zero cloud dependencies.
- **ClickHouse:** [local_streaming_pipeline](https://github.com/MarkPhamm/local_streaming_pipeline), for real-time crypto prices.
- **Lakehouse:** [local_lakehouse_pipeline](https://github.com/MarkPhamm/local_lakehouse_pipeline), MinIO + Iceberg + Trino + dbt, orchestrated by Dagster.
- **OLTP → OLAP:** [fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo), Neon Postgres as the app database, replicated into Snowflake.

## Common mistakes

- Running analytics on the app's production database.
- Picking a cloud warehouse without a budget alert.
- "Lakehouse" in the README, but really a folder of CSVs.
- Not being able to say why you chose this warehouse.

— Mark Pham
