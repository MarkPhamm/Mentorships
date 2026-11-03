# Orchestration: run it without you

← Back to the [data stack guide](../README.md)

Orchestration runs every step of the pipeline in the right order, on a schedule, with retries, and tells you when something fails. It's the difference between a pipeline and a set of scripts you run by hand.

## What an orchestrator does

- **Dependencies:** ingestion finishes before dbt starts; dbt finishes before the dashboard refreshes. The steps form a DAG (directed acyclic graph).
- **Scheduling:** daily at 6am, every hour, or when new data arrives.
- **Retries:** a flaky API call retries three times with backoff before failing the run.
- **Backfills:** re-run last March for one source without touching the rest.
- **Alerts and history:** you know what ran, how long it took, and what broke.
- **Parallelism:** independent tasks run at the same time.

## The options

| Tool | Style | Good for |
|---|---|---|
| **cron / GitHub Actions** | A schedule that runs a script | Small projects with one or two steps. Honest and simple |
| **Airflow** | Tasks in a Python DAG; the most common in job posts | DE roles; the tool you're most likely to meet at work |
| **Dagster** | Built around data assets (tables), not tasks | Asset-aware pipelines, dbt integration, local development |
| **Prefect** | Python functions turned into flows with decorators | Quick, Pythonic pipelines with little setup |
| **The vendor's scheduler** | Fivetran, dbt Cloud or your warehouse runs it | When you don't want to run an orchestrator at all |

Airflow is the safe bet for job posts. Dagster and Prefect are nicer to learn on. Whichever you pick, be able to say why. For what happens under the hood, read [Where does your task run in Apache Airflow?](https://vutr.substack.com/p/where-does-your-task-run-in-apache)

## Design rules

- **Small tasks.** One task per step, so a failure tells you where it broke and you can re-run only that step.
- **Idempotent tasks.** Running a task twice for the same date gives the same result. Without this, retries and backfills create duplicates.
- **Parameterise by date.** Each run processes "its" date, not "now". That's what makes backfills possible.
- **No logic in the DAG file.** The DAG wires steps together; the work lives in your ingestion code and dbt models.

## By role

- **Data engineer:** go deep: a real DAG with retries, backfills, parallel tasks and alerts.
- **Analytics engineer:** know how dbt gets triggered in production and how a failed test stops the run.
- **Data analyst:** a scheduled refresh in your BI tool is enough.

## In my projects

- **Airflow:** [Skytrax](https://github.com/MarkPhamm/skytrax_reviews_extract_load) runs the scraper as 26 parallel tasks.
- **Prefect:** [local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline) orchestrates the incremental load.
- **Dagster:** [local_lakehouse_pipeline](https://github.com/MarkPhamm/local_lakehouse_pipeline).
- **No orchestrator:** in [fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo), Fivetran runs the dbt project itself. No dbt Cloud, no Airflow, no server ([part 2 of the series](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with-02e)).
- **Comparison:** [airflow_vs_dagster](https://github.com/MarkPhamm/airflow_vs_dagster), my notes on the main differences between the two.

## Common mistakes

- An Airflow DAG with a single task that runs one giant script.
- Tasks that use "now" instead of the run's date, so backfills are impossible.
- No retries, no alerts: you find out it broke when someone opens the dashboard.
- Kubernetes and Airflow to run one Python script once a day.

— Mark Pham
