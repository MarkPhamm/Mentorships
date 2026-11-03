# Ingestion: getting data in

← Back to the [data stack guide](../README.md)

Ingestion is the **E** and the **L** in ELT: extract data from the source, load it into your platform. It sounds like the boring part. It's where most pipelines break, and it's where most "end-to-end" student projects cheat, with a CSV downloaded once by hand.

## What good ingestion does

- **Loads only what's new.** A full reload works for 5,000 rows. It doesn't for 50 million. Load by date, by an increasing ID, by an `updated_at` cursor, or with CDC.
- **Is idempotent.** Running the same job twice gives the same result, not duplicates. This is the most common interview question about a DE project. Have an answer: upsert on a key, overwrite a date partition, or deduplicate downstream.
- **Survives failure.** Retries with backoff, timeouts, and a clear failure when something is wrong. A job that silently loads zero rows is worse than one that crashes.
- **Doesn't transform.** Load the data as it arrived. Renaming, cleaning and joining belong in [transformation](../5-transformation/README.md). If you clean in your ingestion script, you can never get the original back.
- **Keeps secrets out of the code.** API keys in env vars or a secrets manager, never in the repo.

## Batch, CDC or streaming

| Pattern | How it works | Use it when | Example tools |
|---|---|---|---|
| **Batch** | Pull a chunk on a schedule (hourly, daily) | Almost always. Most business questions don't need fresher data than yesterday | Python + `requests`, dlt, Airbyte |
| **CDC (change data capture)** | Read the source database's change log and copy every insert, update and delete | The source is an app database and you need updates and deletes, not only new rows | Fivetran, Debezium, Airbyte |
| **Streaming** | Events flow continuously, processed within seconds | The data changes by the second and someone acts on it by the second | Kafka, Kinesis, Pub/Sub, then Spark or Flink |

**Start with batch.** Streaming on data that updates once a day is tool soup, not engineering.

## Build or buy

- **Write it yourself** (Python, `requests`, BeautifulSoup) when there's no connector, like a website with no API. You learn the most this way: pagination, rate limits, auth, retries.
- **Use a framework** (dlt) to skip the boilerplate: schema inference, incremental state and loading are handled for you.
- **Use a managed connector** (Fivetran, Airbyte) for common sources like Postgres, Salesforce or Stripe. This is what most companies do. Knowing when *not* to write code is a senior skill too.

## By role

- **Data engineer:** this is your layer. Go deep: incremental loads, idempotency, parallelism, CDC or streaming.
- **Analytics engineer:** know the patterns well enough to model what lands. A managed connector or dlt is fine.
- **Data analyst:** a clean public dataset or a simple API script is enough. Spend your time on the analysis.

## In my projects

- **[Skytrax](https://github.com/MarkPhamm/skytrax_reviews_extract_load):** a BeautifulSoup scraper for 160K+ reviews, split across 26 parallel Airflow tasks. Write-it-yourself, because the site had no API.
- **[local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline):** dlt and PyArrow pull the CFPB complaints API incrementally from a start date I set.
- **[fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo):** Fivetran CDC from Neon Postgres into Snowflake. I replaced a scraper, Airflow and Terraform with one managed connector, and wrote up the trade-offs in [this series](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with).
- **[local_streaming_pipeline](https://github.com/MarkPhamm/local_streaming_pipeline):** live Coinbase crypto prices into Kafka, the one project where streaming has a reason.

## Common mistakes

- A "pipeline" that's a CSV downloaded once by hand.
- Full reloads of everything, every run.
- Duplicates when a job runs twice.
- Cleaning data inside the ingestion script.
- An API key committed to the repo.

— Mark Pham
