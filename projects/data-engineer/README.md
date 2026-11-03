# Data engineer: ingestion, reliability, infrastructure

← Back to the [projects guide](../README.md)

A data engineer gets data from where it lives to where it's needed, every day, without anyone babysitting it. Your project should prove it keeps running when you're not watching.

- **Real ingestion.** Pull from an API or a website, not a CSV you downloaded once. Handle pagination, rate limits, retries and auth. See [picking a data source](../../data-stack/1-sources/README.md).
- **Incremental and idempotent loads.** Load only new or changed data (by date, ID or CDC). Running the same job twice must not create duplicates. This is the most common interview question about a DE project; have a good answer.
- **A landing zone.** Raw data in S3 or Parquet files, partitioned by load date, never overwritten.
- **Orchestration.** A DAG with clear tasks, retries, and backfills. Parallelise where it helps and explain why.
- **Infrastructure as code.** Docker Compose so anyone can run it locally. Terraform for cloud resources, IAM roles and warehouse permissions. No clicking around in a console that nobody can reproduce.
- **Secrets and auth done properly.** Env vars or a secrets manager, never keys in the repo. OIDC or key-pair auth for CI if you go to the cloud.
- **Depth on one hard thing.** Streaming (Kafka, Spark, Flink), CDC, a lakehouse (Iceberg, Trino), performance on a big dataset. One hard thing done well beats five tools name-dropped.

**Where data engineers go wrong:** a "pipeline" that's one Python script run by hand, full reloads of everything every time, an Airflow DAG with a single task, a Kafka setup with nothing actually streaming, and the same YouTube Spotify/Reddit pipeline everyone else built.

**In my projects:** I split Skytrax into separate repos so each one goes deep on one role, tied together by a [project site](https://markphamm.github.io/skytrax_reviews/). [skytrax_reviews_extract_load](https://github.com/MarkPhamm/skytrax_reviews_extract_load) is the DE half: scraping 160K+ reviews with 26 parallel Airflow tasks, S3 staging, Snowflake and Terraform. [skytrax_reviews_transformation](https://github.com/MarkPhamm/skytrax_reviews_transformation) is the AE half: a Kimball star schema with 5 dimensions and 1 fact table, deterministic surrogate keys, slim CI on pull requests, `--defer --favor-state` deploys, OIDC so GitHub Actions never holds an AWS key, and dbt docs hosted on CloudFront ([live dbt docs](https://d38l3fc9bckvbz.cloudfront.net/#!/overview/ba_transformation?g_v=1)). The analyst layer on top is a Mode report, and one of my mentees landed an internship offer with a Mode project on the same airline reviews. For streaming, [local_streaming_pipeline](https://github.com/MarkPhamm/local_streaming_pipeline) takes live Coinbase crypto prices through Kafka, Spark or Flink, into ClickHouse and a live dashboard, all with one `./run.sh`.

## Project ideas

Each idea below is an **illustration of a shape**, not a project to copy. If 50 of my mentees build the same idea because it's on this list, it becomes the new Titanic. Change at least one of the source, the question or the audience (better, all three), so it passes the [only-me test](../../mentality/4-competitive-advantage/README.md).

What matters: real ingestion, incremental and idempotent loads, orchestration, infrastructure as code, and depth on one hard thing.

- **A scraper that runs every day.** Crawl a site with no API, land raw pages in object storage partitioned by date, parse into a warehouse, and schedule it. Show what happens when the site's layout changes.
- **An incremental API pipeline.** An API with history: backfill once, then load only new records daily. Prove idempotency: run the same day twice and show the row count doesn't change.
- **CDC from an app database.** Run Postgres with a small app (or a script simulating one) writing inserts, updates and deletes, replicate it into a warehouse, and handle soft deletes properly.
- **Streaming with a reason.** Live data that genuinely changes by the second (prices, transit vehicle positions, game events) through Kafka into a real-time store and a live dashboard. If the data updates once a day, it's not a streaming project.
- **A lakehouse on a laptop.** Object storage (MinIO), Iceberg tables, a query engine (Trino), dbt and an orchestrator, all in Docker Compose. My [local_lakehouse_pipeline](https://github.com/MarkPhamm/local_lakehouse_pipeline) does this with NYC taxi data. That data is a classic, so if you build one, pick a source nobody else uses.

**Level up:** Terraform for every cloud resource, OIDC or key-pair auth instead of static keys, alerts when a run fails or returns zero rows, and a README section on cost.

— Mark Pham
