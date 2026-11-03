# The data stack

Before you build a project, you need to know what you're building on. Every data platform, from a laptop project to a company with 500 engineers, has the same layers. This guide covers each one: what it does, the options, what each role should know about it, and how my own projects use it. It's the shared foundation for every role in the [projects guide](../projects/README.md).

Start with the overview, then read the layers in order. They follow the data from where it's born to where people use it.

| | Page | What it covers |
|---|---|---|
| 0 | [Overview](0-the-data-stack/README.md) | The whole stack in one diagram, and the question an interviewer asks about each layer |
| 1 | [Sources](1-sources/README.md) | Where data comes from, and how to pick one: Kaggle CSVs, public data, APIs, crawling, your own data |
| 2 | [Ingestion](2-ingestion/README.md) | Getting data in: batch, CDC and streaming; incremental and idempotent loads; build or buy |
| 3 | [Landing](3-landing/README.md) | Keeping the raw data untouched: object storage, Parquet, partitions |
| 4 | [Warehouse](4-warehouse/README.md) | OLTP vs OLAP, warehouse vs lake vs lakehouse, and which to pick |
| 5 | [Transformation](5-transformation/README.md) | Staging, intermediate and marts; grain and star schemas; tests and CI |
| 6 | [Serving](6-serving/README.md) | Dashboards and BI tools, and why "Power BI or Tableau?" is the wrong question |
| 7 | [Orchestration](7-orchestration/README.md) | Running it all on a schedule, with retries and backfills |

— Mark Pham
