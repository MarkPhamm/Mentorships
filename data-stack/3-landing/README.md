# Landing: keep the raw data

← Back to the [data stack guide](../README.md)

The landing zone (also called raw, bronze or staging storage) holds data **exactly as it arrived**, before anyone touches it. It's the cheapest insurance in the whole stack. When a model is wrong, a parser breaks or the business changes a definition, you rebuild from here instead of re-pulling from the source. Sometimes the source is gone and re-pulling isn't an option.

## The rules

- **Never overwrite, never edit.** Append new files or rows. If raw is mutable, it isn't raw.
- **Partition by load date.** `raw/reviews/load_date=2026-11-03/` makes backfills, reprocessing and deleting a bad day easy.
- **Store it in an open, columnar format when you can.** Parquet is smaller and faster to query than CSV or JSON. Keep the original JSON or HTML too if you'll need to re-parse it.
- **Record metadata.** When it was loaded, from where, by which run. You'll need it the first time two numbers disagree.
- **Keep it out of Git.** Raw data goes in object storage or a local folder in `.gitignore`. Commit a small sample at most.

## Where it lives

| Option | What it is | Good for |
|---|---|---|
| **Local folder of Parquet files** | A `landing/` directory on your laptop | Local projects; free, and DuckDB reads Parquet directly |
| **Object storage** (S3, GCS, Azure Blob) | Cheap, unlimited file storage in the cloud | Cloud projects; the standard at most companies |
| **MinIO** | S3-compatible storage you run in Docker | Learning S3 without a cloud account |
| **A `raw` schema in the warehouse** | Tables loaded as-is, before any modelling | When a connector (Fivetran, dlt) loads straight to the warehouse |

Many teams use both: files in object storage, then `COPY INTO` a raw schema in the warehouse.

## By role

- **Data engineer:** design it properly: partitioning, file format, retention, and how a bad load gets fixed.
- **Analytics engineer:** treat the raw schema as read-only and build staging models on top of it.
- **Data analyst:** you rarely need one, but loading your CSV raw into a warehouse before modelling it is a cheap level-up.

## In my projects

- **[Skytrax](https://github.com/MarkPhamm/skytrax_reviews_extract_load):** scraped reviews land in S3 under `raw/` and `processed/`, then `COPY INTO` Snowflake. The source site has since shut down permanently, so that raw data is the only copy left. That's exactly why the landing layer exists.
- **[local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline):** Parquet files in a local `landing/` folder, read by DuckDB.
- **[local_lakehouse_pipeline](https://github.com/MarkPhamm/local_lakehouse_pipeline):** monthly NYC taxi Parquet files uploaded to MinIO under `s3://warehouse/raw_data/yellow_trips/`.

## Common mistakes

- No landing layer: the script cleans data in memory and writes only the result.
- Overwriting raw files on every run.
- One giant file instead of date partitions.
- Raw data committed to the Git repo.

— Mark Pham
