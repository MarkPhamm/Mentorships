# Every free article on vutr

[vutr](https://vutr.substack.com) is Vu Trinh's data engineering newsletter, read by 19,000+ engineers. I'm a technical writer there. This is **every free article** on it (131 as of November 2026), grouped by topic, plus the GroupBy weekly roundups at the end. All are in English.

Not sure where to start? Use [my picks](README.md#7-go-deeper-free-articles-from-vutr) first, then come back here for whatever you're working on.

**Contents:** [Guest posts by me](#guest-posts-by-me) · [Foundations and career](#foundations-and-career) · [Data modeling, dbt and analytics engineering](#data-modeling-dbt-and-analytics-engineering) · [Warehouses and query engines](#warehouses-and-query-engines) · [File formats, table formats and lakehouses](#file-formats-table-formats-and-lakehouses) · [Spark](#spark) · [Kafka, streaming and CDC](#kafka-streaming-and-cdc) · [Orchestration and pipelines](#orchestration-and-pipelines) · [How big companies build data platforms](#how-big-companies-build-data-platforms) · [GroupBy roundups](#groupby-weekly-roundups)

## Guest posts by me

- [I spent 12 hours rebuilding my junior-year project: Part 1 - The Extract Load](https://vutr.substack.com/p/i-spent-12-hours-rebuilding-my-junior): a weekend project to boost your data engineering career. *2026*
- [I spent 12 hours rebuilding my junior-year project: Part 2 - The Transformation Layer](https://vutr.substack.com/p/i-spent-12-hours-rebuilding-my-junior-26f): the dbt side of the same project. *2026*

## Foundations and career

- [The History of Data Engineering](https://vutr.substack.com/p/the-history-of-data-engineering): the most comprehensive one you'll find. *2025*
- [ETL and ELT](https://vutr.substack.com/p/etl-and-elt): it's not just about swapping the T and the L. *2024*
- [The Data Lake, Warehouse and Lakehouse](https://vutr.substack.com/p/the-data-lake-warehouse-and-lakehouse): the main types of data architecture. *2024*
- [Do we need the Lakehouse architecture?](https://vutr.substack.com/p/do-we-need-the-lakehouse-architecture): when data lakes and warehouses aren't enough. *2024*
- [9 technologies that changed data engineering forever](https://vutr.substack.com/p/free-9-technologies-that-changed): without them, we'd live in a very different world. *2026*
- [Solve higher-impact problems](https://vutr.substack.com/p/free-do-work-that-matters): the mindset to grow and get promoted. *2026*
- [If I could travel back 5 years, what would I tell myself about Docker?](https://vutr.substack.com/p/i-spent-3-hours-to-understand-more): a friendly start, plus a Docker cheat sheet. *2024*
- [Kubernetes for Data Engineers](https://vutr.substack.com/p/kubernetes-for-data-engineer): things that will help you start. *2024*
- [I spent 10 hours learning multithreading and multiprocessing](https://vutr.substack.com/p/free-i-spent-10-hours-learning-multithreading): a mental model, in a Python context. *2026*
- [How Rust and Python manage memory](https://vutr.substack.com/p/how-rust-and-python-manage-memory): ownership vs the garbage collector. *2024*

## Data modeling, dbt and analytics engineering

- [Why is dbt so popular?](https://vutr.substack.com/p/why-is-dbt-so-popular): the motivation behind dbt and why it's becoming the standard. *2025*
- [How to learn dbt cheap and fast](https://vutr.substack.com/p/how-to-learn-dbt-cheap-and-fast): right on your laptop, no internet needed. *2026*
- [Kimball Dimensional Modeling Overview](https://vutr.substack.com/p/dimensional-modeling-overview): is it still valid? *2025*
- [How did Airbnb build their semantic layer?](https://vutr.substack.com/p/how-did-airbnb-build-their-semantic): Minerva, Airbnb's metric platform. *2025*
- [Quick insights on materialized views](https://vutr.substack.com/p/quick-insights-on-materialized-views): working with materialized views more efficiently. *2026*
- [What is a data contract?](https://vutr.substack.com/p/what-is-a-data-contract): context, definition and implementation. *2026*
- [What is a data product?](https://vutr.substack.com/p/free-what-is-a-data-product): motivation and implementation. *2026*
- [Why is Text-to-SQL so hard?](https://vutr.substack.com/p/why-is-text-to-sql-so-hard): why we need it, its challenges, and how to make it easier. *2025*
- [How did YouTube engineers build CI/CD for data pipelines?](https://vutr.substack.com/p/how-did-youtube-engineers-build-cicd): CI/CD for data vs code, at scale. *2026*
- [How Meta solves data lineage at scale](https://vutr.substack.com/p/how-meta-solves-data-lineage-at-scale): their approach and what we can learn. *2025*
- [DataHub: the metadata platform developed at LinkedIn](https://vutr.substack.com/p/datahub-the-metadata-platform-developed): managing a data catalog at scale. *2024*
- [I spent 3 hours learning how Uber manages data quality](https://vutr.substack.com/p/i-spent-3-hours-learning-how-uber): from the standard to the data quality platform. *2024*
- [How does Netflix ensure data quality for thousands of Iceberg tables?](https://vutr.substack.com/p/how-does-netflix-ensure-the-data): the Write-Audit-Publish pattern with Iceberg branches. *2024*

## Warehouses and query engines

**Comparisons and cost**

- [The internals of BigQuery, Snowflake, Databricks and Redshift](https://vutr.substack.com/p/the-internal-of-bigquery-snowflake): four cloud data warehouses in one article. *2025*
- [I analyzed the pricing models of 5 cloud data warehouses (part 1)](https://vutr.substack.com/p/12-i-analyzed-the-pricing-models): Microsoft Fabric, Redshift and BigQuery. *2026*
- [My uncensored guide to saving on cloud data warehouse costs](https://vutr.substack.com/p/saving-cloud-data-warehouse-cost) *2025*
- [What makes OLTP databases so quick at finding your data?](https://vutr.substack.com/p/what-makes-oltp-databases-so-quick): the data structure behind query performance in OLTP databases. *2025*
- [We might not fully understand the column store!](https://vutr.substack.com/p/we-might-not-completely-understand): row, column and hybrid storage models. *2024*

**Snowflake**

- [I spent 8 hours diving deep into Snowflake (again)](https://vutr.substack.com/p/i-spent-8-hours-diving-deep-into): virtual warehouses, storage and caching. *2024*
- [The design principles of Snowflake](https://vutr.substack.com/p/i-spent-another-6-hours-understanding): insights from the 2016 Snowflake paper. *2024*
- [Snowflake's elastic query engine on disaggregated storage](https://vutr.substack.com/p/i-read-another-paper-to-understand): notes on another Snowflake paper. *2024*

**BigQuery and Google**

- [The design principles of BigQuery](https://vutr.substack.com/p/everything-you-need-to-know-about): insights from the BigQuery academic paper. *2024*
- [How BigQuery executes a SQL query internally](https://vutr.substack.com/p/i-spent-4-hours-figuring-out-how): what happens after you submit it. *2024*
- [How BigQuery inserts, deletes and updates data internally](https://vutr.substack.com/p/i-spent-3-hours-trying-to-figure) *2024*
- [How BigQuery stores semi-structured data](https://vutr.substack.com/p/lesson-learned-after-reading-bigquery): Parquet uses the same approach. *2024*
- [BigQuery's shuffle operation](https://vutr.substack.com/p/bigquery-processing-engine-shuffle): lessons from the BigQuery paper. *2024*
- [How Google manages terabytes of metadata for BigQuery](https://vutr.substack.com/p/i-spent-8-hours-learning-how-google) *2024*
- [The architecture of BigQuery's storage engine (Vortex, part 1)](https://vutr.substack.com/p/i-spent-4-hours-learning-the-architecture) *2024*
- [How Vortex, the BigQuery storage engine, works behind the scenes (part 2)](https://vutr.substack.com/p/how-does-vortex-the-bigquery-storage) *2024*
- [How Google serves analytics applications](https://vutr.substack.com/p/i-spent-6-hours-learn-how-google): 10 GB/s throughput and sub-millisecond latency. *2025*
- [Procella: the query engine at YouTube](https://vutr.substack.com/p/procella-the-query-engine-at-youtube) *2024*

**Redshift, Databricks and others**

- [The design of Amazon Redshift](https://vutr.substack.com/p/i-spent-another-8-hours-understanding): insights from *Amazon Redshift Re-invented* (2022). *2024*
- [Why did Databricks build the Photon engine?](https://vutr.substack.com/p/why-did-databricks-build-the-photon) *2024*
- [A closer look into Databricks's Photon engine](https://vutr.substack.com/p/a-closer-look-into-databrickss-photon): vectorization. *2024*
- [8 minutes to understand Presto](https://vutr.substack.com/p/8-minutes-to-understand-presto): the engine Uber, Netflix, Airbnb and LinkedIn use. *2025*
- [70% of analytical systems will adopt this open-source solution (?)](https://vutr.substack.com/p/free-70-of-analytical-systems-will): Apache Arrow DataFusion. *2026*
- [I made 1+1=0 in DuckDB](https://vutr.substack.com/p/i-made-110-in-duckdb): and other cool things about DuckDB. *2024*

**Real-time OLAP**

- [I spent 3 hours learning the overview of ClickHouse](https://vutr.substack.com/p/i-spent-3-hours-learning-the-overview) *2024*
- [The ClickHouse MergeTree table engine](https://vutr.substack.com/p/i-spent-8-hours-learning-the-clickhouse): writes, reads, mutations and replication. *2024*
- [How ClickHouse built their internal data warehouse](https://vutr.substack.com/p/how-clickhouse-built-their-internal): 19 sources, 470 TB compressed. *2024*
- [One ClickHouse query took down 20% of the internet for 5 hours and 38 minutes](https://vutr.substack.com/p/free-one-clickhouse-query-took-down): the Cloudflare outage of 18 November 2025. *2026*
- [ClickHouse → real-time insight in 15 minutes](https://vutr.substack.com/p/clickhouse-real-time-insight-in-15): Tinybird (sponsored). *2026*
- [The architecture of Apache Druid](https://vutr.substack.com/p/the-architecture-of-apache-druid) *2024*
- [A glimpse of Apache Pinot, LinkedIn's real-time OLAP system](https://vutr.substack.com/p/a-glimpse-of-apache-pinot-the-real) *2024*

## File formats, table formats and lakehouses

**File formats**

- [I spent 8 hours learning Parquet. Here's what I discovered](https://vutr.substack.com/p/the-overview-of-parquet-file-format) *2024*
- [I vibe-coded a tool to visualize any Parquet file's internals](https://vutr.substack.com/p/i-spent-10-hours-vibe-coding-a-tool): Petquar. *2026*
- [A file format claims to be 100x faster than Parquet](https://vutr.substack.com/p/free-a-file-format-claims-to-be-100x): for random access. *2026*
- [I spent 6 hours learning Apache Arrow](https://vutr.substack.com/p/i-spent-6-hours-learning-apache-arrow): why analytics needs a standard memory format. *2024*

**Table formats**

- [I spent 4 hours learning Apache Iceberg](https://vutr.substack.com/p/i-spent-8-hours-learning-apache-iceberg): overview and architecture. *2024*
- [I spent 7 hours diving deep into Apache Iceberg](https://vutr.substack.com/p/i-spent-7-hours-diving-deep-into): how everything works, in more detail. *2024*
- [I spent 8 hours relearning the Delta Lake table format](https://vutr.substack.com/p/i-spent-8-hours-relearning-the-delta): reads, writes, concurrency and mutation. *2024*
- [Understanding the Delta Lake table format](https://vutr.substack.com/p/i-spent-5-hours-to-understand-more): insights from the Delta Lake paper. *2024*
- [The story behind Apache Hudi](https://vutr.substack.com/p/i-spent-5-hours-exploring-the-story): why Uber created it and how it differs from Iceberg and Delta. *2024*
- [How do Iceberg, Delta Lake and Hudi ensure atomicity?](https://vutr.substack.com/p/how-do-iceberg-delta-lake-and-hudi): when you write 3 files, you don't want to see 1.5. *2025*
- [Why Walmart chose Apache Hudi for their lakehouse](https://vutr.substack.com/p/why-walmart-chose-apache-hudi-for) *2025*
- [How Netflix operates Apache Iceberg at scale](https://vutr.substack.com/p/i-spent-4-hours-learning-how-netflix) *2024*

**Lakehouses, catalogs and storage**

- [Build a lakehouse on a laptop with dbt, Airflow, Trino, Iceberg and MinIO](https://vutr.substack.com/p/build-a-lakehouse-on-a-laptop-with): a pet project for learning data engineering. *2025*
- [How did Meta modernize their lakehouse?](https://vutr.substack.com/p/how-did-meta-modernize-their-lakehouse) *2025*
- [I spent 5 hours learning Unity Catalog](https://vutr.substack.com/p/i-spent-5-hours-learning-unity-catalog): Databricks' open-sourced catalog. *2026*
- [Databricks introduced a new database that could change everything (?)](https://vutr.substack.com/p/databricks-introduced-a-new-database): Lakebase. *2026*
- [How Google lets us build a lakehouse](https://vutr.substack.com/p/i-spent-5-hours-learning-how-google): Google Cloud BigLake. *2024*
- [Bauplan: operate your lakehouse with zero infrastructure](https://vutr.substack.com/p/bauplan-operate-your-lakehouse-with): FaaS data pipelines on S3. *2025*
- [What is Apache Hive?](https://vutr.substack.com/p/what-is-apache-hive): why Meta created it, and why you don't see it anymore. *2025*
- [The Hadoop Distributed File System](https://vutr.substack.com/p/i-spent-8-hours-reading-the-paper-523): everything you need to know about HDFS. *2024*
- [All you need to know about the Google File System](https://vutr.substack.com/p/i-spent-8-hours-reading-the-paper) *2024*

## Spark

- [The overview of Apache Spark](https://vutr.substack.com/p/the-overview-of-apache-spark): start here. *2024*
- [The fastest way to learn Apache Spark](https://vutr.substack.com/p/the-fastest-way-to-learn-apache-spark): a CLI tool to dig into Spark on your laptop. *2026*
- [How Apache Spark plans the execution for us](https://vutr.substack.com/p/i-spent-6-hours-to-learn-how-apache): Catalyst, Adaptive Query Execution, and Spark 3 at Airbnb. *2024*
- [The Apache Spark scheduling process](https://vutr.substack.com/p/i-spent-8-hours-learning-apache-spark): anatomy of a Spark job. *2024*
- [Apache Spark resource allocation](https://vutr.substack.com/p/i-spent-4-hours-learning-apache-spark): and the two scheduling modes. *2024*
- [Why is the Apache Spark RDD immutable?](https://vutr.substack.com/p/why-apache-spark-rdd-is-immutable) *2024*
- [How is Databricks' Spark different from open-source Spark?](https://vutr.substack.com/p/how-is-databricks-spark-different) *2025*
- [Is this feature a revolution in Spark?](https://vutr.substack.com/p/is-this-feature-a-revolution-in-spark): processing data through an API request instead of submitting an application. *2025*
- [How Databricks improved Spark Structured Streaming throughput by up to 2.8x](https://vutr.substack.com/p/free-how-databricks-improved-spark): micro-batch pipelining. *2026*
- [How does Uber deal with Spark out-of-memory errors?](https://vutr.substack.com/p/free-how-does-uber-deal-with-spark): retrying, but smarter. *2026*
- [How does Uber handle petabytes of Spark shuffle data every day?](https://vutr.substack.com/p/how-does-uber-handle-petabytes-of): the Remote Shuffle Service. *2024*

## Kafka, streaming and CDC

**Kafka basics**

- [If you're learning Kafka, this article is for you](https://vutr.substack.com/p/if-youre-learning-kafka-this-article): a baseline for your Kafka learning. *2025*
- [Apache Kafka: overview](https://vutr.substack.com/p/apache-kafka-part-1-overview): terminology and architecture. *2024*
- [Apache Kafka: producer](https://vutr.substack.com/p/apache-kafka-producer) *2024*
- [Apache Kafka: consumer](https://vutr.substack.com/p/apache-kafka-consumer) *2024*
- [Apache Kafka: important designs](https://vutr.substack.com/p/apache-kafka-important-designs): filesystem, zero-copy and batching. *2024*

**Kafka at scale and the next generation**

- [How did LinkedIn handle 7 trillion messages daily with Kafka?](https://vutr.substack.com/p/how-did-linkedin-handle-7-trillion) *2024*
- [The company that created Kafka is replacing it with a new solution](https://vutr.substack.com/p/the-company-that-created-kafka-is): LinkedIn's Northguard. *2025*
- [How does Meta move terabytes of data per second?](https://vutr.substack.com/p/how-did-meta-move-terabytes-of-data): an internal message queue ingesting 15 TB/s. *2025*
- [How to choose the right diskless Kafka](https://vutr.substack.com/p/how-to-choose-the-right-diskless) *2025*
- [Deep dive into the challenges of building Kafka on top of S3](https://vutr.substack.com/p/deep-dive-into-the-challenges-of) *2025*
- [How do we run Kafka 100% on object storage?](https://vutr.substack.com/p/how-do-we-run-kafka-100-on-the-object): AutoMQ. *2024*
- [I spent 8 hours researching WarpStream](https://vutr.substack.com/p/i-spent-8-hours-researching-warpstream): the Kafka protocol in Go, 100% on object storage. *2024*
- [How AutoMQ reduces nearly 100% of Kafka cross-zone data transfer cost](https://vutr.substack.com/p/how-automq-reduces-nearly-100-of) *2024*
- [AutoMQ: auto partition reassignment in Kafka without Cruise Control](https://vutr.substack.com/p/automq-achieving-auto-partition-reassignment) *2024*
- [Kafka migration with zero downtime](https://vutr.substack.com/p/kafka-migration-with-zero-downtime): AutoMQ. *2025*
- [Stream Kafka topics to Iceberg tables with zero ETL](https://vutr.substack.com/p/stream-kafka-topic-to-the-iceberg): AutoMQ. *2025*
- [Bufstream: stream Kafka messages to Iceberg tables in minutes](https://vutr.substack.com/p/bufstream-stream-kafka-messages-to) *2025*
- [Is your data valid? Why Bufstream guarantees what Kafka can't](https://vutr.substack.com/p/is-your-data-valid-why-bufstream): semantic validation. *2025*

**Stream processing and CDC**

- [Apache Flink overview](https://vutr.substack.com/p/apache-flink-overview): architecture, event-time processing and state management. *2024*
- [Change Data Capture (CDC) for Data Engineers](https://vutr.substack.com/p/free-change-data-capture-cdc-for): motivation, implementation and challenges. *2026*
- [How does Figma improve insight freshness by 10x?](https://vutr.substack.com/p/free-how-does-figma-improve-insight): change data capture and more. *2026*
- [The stream processing model behind Google Cloud Dataflow](https://vutr.substack.com/p/the-stream-processing-model-behind): balancing correctness, latency and cost. *2024*
- [4 trillion events daily at LinkedIn](https://vutr.substack.com/p/4-trillion-events-daily-at-linkedin): real-time processing with Apache Beam. *2024*
- [How Twitter processes 4 billion events in real time daily](https://vutr.substack.com/p/how-twitter-processes-4-billion-events): from Lambda to Kappa. *2024*
- [How did Facebook design their real-time processing ecosystem?](https://vutr.substack.com/p/how-did-facebook-design-their-real): hundreds of GBs per second. *2024*
- [DoorDash's real-time processing system](https://vutr.substack.com/p/doordashs-real-time-processing-system): Kafka + Flink. *2024*
- [How does DoorDash evolve its real-time processing platform with Iceberg?](https://vutr.substack.com/p/how-do-doordash-evolve-realtime-processing): Flink + Iceberg. *2025*

## Orchestration and pipelines

- [Apache Airflow overview](https://vutr.substack.com/p/apache-airflow-overview): the most famous orchestration tool. *2024*
- [3 hours and you'll learn every Apache Airflow fundamental](https://vutr.substack.com/p/3-hours-and-you-will-learn-every): right on your laptop. *2026*
- [Where does your task run in Apache Airflow?](https://vutr.substack.com/p/where-does-your-task-run-in-apache): everything about executors. *2025*
- [Let's use Orchestra to build an end-to-end data pipeline in 10 minutes](https://vutr.substack.com/p/lets-use-orchestra-to-build-an-end) *2025*
- [I spent 6 hours learning AWS Glue](https://vutr.substack.com/p/i-spent-6-hours-learning-aws-glue) *2025*
- [Practical data engineering using AWS cloud technologies](https://vutr.substack.com/p/practical-data-engineering-using): an end-to-end project with S3, SNS, Lambda and more. *2024*

## How big companies build data platforms

- [How did Uber build their data infrastructure to serve 137 million monthly users?](https://vutr.substack.com/p/how-did-uber-build-their-data-infrastructure): Kafka, HDFS, Hudi, Spark, Flink, Pinot and Presto. *2025*
- [How does Uber build real-time infrastructure for petabytes of data a day?](https://vutr.substack.com/p/i-spent-7-hours-understanding-ubers) *2024*
- [Uber's big data revolution: from MySQL to Hadoop and beyond](https://vutr.substack.com/p/ubers-big-data-revolution-from-mysql) *2024*
- [I spent 5 hours understanding how Uber built their ETL pipelines](https://vutr.substack.com/p/i-spent-5-hours-understanding-how): they don't use batch or stream pipelines. *2025*
- [Let's build a data platform like Spotify!](https://vutr.substack.com/p/lets-build-a-data-platform-like-spotify) *2025*
- [Netflix Data Engineer Stack](https://vutr.substack.com/p/netflix-data-engineer-stack): Iceberg, Spark, Flink and more. *2024*
- [Netflix's trillions-scale real-time data infrastructure](https://vutr.substack.com/p/netflixs-trillions-scale-real-time): four phases and their lessons. *2024*
- [How does Notion handle 200 billion data entities?](https://vutr.substack.com/p/how-does-notion-handle-200-billion): from PostgreSQL to a data lake. *2024*
- [How did Discord evolve to handle trillions of data points?](https://vutr.substack.com/p/how-did-discord-evolve-to-handle) *2024*
- [Diving deep into LinkedIn's data infrastructure](https://vutr.substack.com/p/diving-deep-into-linkedins-data-infrastructure) *2024*

## GroupBy weekly roundups

Before the deep dives, vutr ran *GroupBy*, a weekly roundup of the best data engineering links. 44 free issues, September 2023 – July 2024.

<details>
<summary>Show all 44 issues</summary>

- [GroupBy #44: Meta / The Data Stack](https://vutr.substack.com/p/groupby-44-meta-the-data-stack)
- [GroupBy #43: Uber / Kafka tiered storage](https://vutr.substack.com/p/groupby-43-uber-kafka-the-tiered)
- [GroupBy #42: PayPal, scaling Kafka](https://vutr.substack.com/p/groupby-42-paypal-scaling-kafka)
- [GroupBy #41: Uber's batch data infrastructure with Google Cloud](https://vutr.substack.com/p/groupby-41-ubers-batch-data-infrastructure)
- [GroupBy #40: Data infrastructure at Airbnb](https://vutr.substack.com/p/groupby-40-data-infrastructure-at)
- [GroupBy #39: 2000+ dbt models in Airflow; serverless Jupyter notebooks at Meta](https://vutr.substack.com/p/groupby-39-how-stripes-document-databases)
- [GroupBy #38: Modernizing Uber's batch data infrastructure; Apache Iceberg](https://vutr.substack.com/p/groupby-38-modernizing-ubers-batch)
- [GroupBy #37: Composable data management at Meta; job counting at Uber](https://vutr.substack.com/p/groupby-37-composable-data-management)
- [GroupBy #36: Agoda's Kafka load balancing; reducing Snowflake cost](https://vutr.substack.com/p/groupby-36-agoda-how-we-solve-load)
- [GroupBy #35: The Netflix data engineering stack; Atlassian's data platform](https://vutr.substack.com/p/groupby-35-the-netflix-data-engineering)
- [GroupBy #34: Hybrid transactional/analytical storage; Uber's Michelangelo](https://vutr.substack.com/p/groupby-34-hybrid-transactionalanalytical)
- [GroupBy #33: Netflix's Data Gateway; the cloud storage triad](https://vutr.substack.com/p/groupby-33-data-gateway-a-platform)
- [GroupBy #32: Canva counting billions; Uber's accounting data testing](https://vutr.substack.com/p/groupby-32-canva-scaling-to-count)
- [GroupBy #31: Uber's trillion-entry ledger migration; Grab's experiment engine](https://vutr.substack.com/p/groupby-31-migrating-a-trillion-entries)
- [GroupBy #30: Uber's LedgerStore; lessons from Apache Calcite](https://vutr.substack.com/p/groupby-30-uber-how-ledgerstore-supports)
- [GroupBy #29: Scaling AI/ML infrastructure at Uber](https://vutr.substack.com/p/groupby-29-scaling-aiml-infrastructure)
- [GroupBy #28: Tableflow, the Kafka/Iceberg duality](https://vutr.substack.com/p/groupby-28-tableflow-the-streamtable)
- [GroupBy #27: Balancing HDFS DataNodes at Uber; scaling Figma's databases](https://vutr.substack.com/p/groupby-27-balancing-hdfs-datanodes)
- [GroupBy #26: GitHub's merge queue; "good enough" data models](https://vutr.substack.com/p/groupby-26-how-github-uses-merge)
- [GroupBy #25: From Samza to Flink; DoorDash's search engine](https://vutr.substack.com/p/groupby-25-from-samza-to-flink-a)
- [GroupBy #24: Near real-time analytics on Grab's data lake](https://vutr.substack.com/p/groupby-24-enabling-near-real-time)
- [GroupBy #23: Meta loves Python; Uber's 40M reads per second](https://vutr.substack.com/p/groupby-23-meta-loves-python-how)
- [GroupBy #22: The data engineering landscape in 2024](https://vutr.substack.com/p/groupby-22-navigating-the-data-engineering)
- [GroupBy #21: Designing resilient large-scale data systems](https://vutr.substack.com/p/groupby-21-how-to-design-resilient)
- [GroupBy #20: Google's code reviews; why senior engineering isn't about engineering](https://vutr.substack.com/p/groupby-20-how-google-takes-the-pain)
- [GroupBy #19: How Apple built iCloud; Uber's feature store](https://vutr.substack.com/p/groupby-19-how-apple-built-icloud)
- [GroupBy #18: GC tuning for Presto at Uber](https://vutr.substack.com/p/groupby-18-uber-gc-tuning-for-improved)
- [GroupBy #17: Pinterest's wide-column database; Kafka on Kubernetes at Grab](https://vutr.substack.com/p/groupby-17-pinterests-new-wide-column)
- [GroupBy #16: Uber's anomaly detection; layers of data lineage](https://vutr.substack.com/p/groupby-16-ubers-anomaly-detection)
- [GroupBy #15: Meta's infrastructure for Threads; Notion's data scale](https://vutr.substack.com/p/groupby-15-how-meta-built-the-infrastructure)
- [GroupBy #14: Being a senior IC at Meta; Netflix Data Engineering Summit](https://vutr.substack.com/p/groupby-14-what-it-takes-to-be-a)
- [GroupBy #13: Explaining Kubernetes to my Uber driver; data modelling](https://vutr.substack.com/p/groupby-13-explaining-kubernetes)
- [GroupBy #12: AWS re:Invent 2023; Druid and ClickHouse at Lyft](https://vutr.substack.com/p/groupby-12-aws-reinvent-2023-druid)
- [GroupBy #11: Python at Meta; Netflix incremental processing with Iceberg](https://vutr.substack.com/p/groupby-11-netflix-incremental-processing)
- [GroupBy #10: Netflix's Psyberg; the Parquet format](https://vutr.substack.com/p/groupby-10-netflixs-psyberg-parquet)
- [GroupBy #9: The FDAP stack; Iceberg and Hudi ACID guarantees](https://vutr.substack.com/p/groupby-9-iceberg-and-hudi-acid-guaranteesfdap)
- [GroupBy #8: Demystifying the Parquet file; intro to data modeling](https://vutr.substack.com/p/groupby-8-headline)
- [GroupBy #7: The rise of the data engineer; levels of abstraction](https://vutr.substack.com/p/groupby-7-headline)
- [GroupBy #6: Trillions of data points at Discord; Uber's data lifecycle](https://vutr.substack.com/p/groupby-6-meta-developer-tool-trillions)
- [GroupBy #5: The story of S3; Kafka at scale](https://vutr.substack.com/p/groupby-5-the-story-of-s3-kafka-at)
- [GroupBy #4: Polars and Pandas; 1.8 trillion events](https://vutr.substack.com/p/groupby-4-polars-and-pandas-18-trillion)
- [GroupBy #3: Docker cheat sheet; Spark vs Hadoop; HDFS vs S3](https://vutr.substack.com/p/groupby-3)
- [GroupBy #2: Lakehouse, Iceberg and Delta Lake](https://vutr.substack.com/p/groupby-2)
- [GroupBy #1: Kappa architecture; Presto at Facebook](https://vutr.substack.com/p/groupby-1)

</details>
