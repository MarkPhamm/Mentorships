# Transformation: from raw to trusted

← Back to the [data stack guide](../README.md)

Transformation is the **T** in ELT: turning raw data into tables people can use and trust. It happens inside the warehouse, in SQL, and today that almost always means **dbt**. It's the analytics engineer's layer. If you're new to it, read [Why is dbt so popular?](https://vutr.substack.com/p/why-is-dbt-so-popular) first.

## The layers

| Layer | Prefix | What it does | What it doesn't do |
|---|---|---|---|
| **Staging** | `stg_` | One model per source table: rename, cast types, light cleaning | Joins, business logic |
| **Intermediate** | `int_` | Joins, deduplication, business logic, reusable building blocks | Serve dashboards directly |
| **Marts** | `fct_`, `dim_` | Final tables the business reads: facts and dimensions | Raw column names, messy types |

Every model has one job. If a model is 400 lines long, it's three models.

## Data modelling

- **Grain first.** Before you write a fact table, write down what one row is: "one row per review", "one row per order line per day". Most wrong numbers come from a grain nobody stated.
- **Star schema** (Kimball) is the safe default: fact tables of events and measures, dimension tables of who, what, where and when. BI tools and analysts understand it.
- **Surrogate keys.** Generate stable keys (e.g. a hash of the natural key) instead of relying on source IDs.
- **Slowly changing dimensions.** When an attribute changes over time (a customer's city, a product's price), decide whether you keep history. dbt snapshots do this.
- **Incremental models.** For large, append-only data, process only new rows. Know how you handle late-arriving data and deletes.

## Data quality

- **Generic tests:** `unique` and `not_null` on every primary key, `relationships` between facts and dimensions, `accepted_values` on status columns.
- **Source freshness:** fail or warn when the raw data stops updating.
- **Custom tests** for a business rule only your data has ("a review's rating is between 1 and 10").
- **CI:** run SQLFluff and `dbt build` on every pull request, so a broken model never reaches the dashboard.
- **Docs:** descriptions on models and columns, and generated dbt docs.

## By role

- **Analytics engineer:** this is your layer. Go deep: layers, grain, star schema, tests, docs, CI.
- **Data engineer:** a staging layer and a few tests are enough, but know how dbt runs in your pipeline.
- **Data analyst:** write clean SQL with CTEs, and know the grain of every table you query.

## In my projects

- **[skytrax_reviews_transformation](https://github.com/MarkPhamm/skytrax_reviews_transformation):** a Kimball star schema with 5 dimensions and 1 fact table, deterministic surrogate keys, an incremental fact, slim CI on pull requests, and [hosted dbt docs](https://d38l3fc9bckvbz.cloudfront.net/#!/overview/ba_transformation?g_v=1).
- **[fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo):** I changed five rows in Postgres and followed them to the reporting tables, and found out why revenue came out wrong: soft deletes and hash-based row identity. The story is in [part 3 of the series](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with-85c).

## Common mistakes

- One giant model with all the logic.
- No stated grain, so joins quietly duplicate rows.
- Tests on only one column.
- A "dbt project" that's a folder of views with no layers.
- Business logic in the BI tool instead of in a model.

— Mark Pham
