# Readings

Posts I've written that I send mentees most often. The short ones are on Facebook in [Xóm Data](https://www.facebook.com/groups/xomdata), Vietnam's largest data learning community, where I'm a moderator; most of those are in **Vietnamese**. The longer ones are on my [Substack](https://substack.com/@markphammm), in **English**.

They're grouped in the order I'd read them. New to data? Start at the top.

## 1. Start with the fundamentals

- **[Always start with the Fundamentals (Part 1)](https://www.facebook.com/share/p/1DzVipPaQ1/)** · Facebook, Vietnamese
  Why first- and second-year students should learn SQL before chasing buzzwords like CI/CD, MLOps or lakehouses, and the order to learn it in: one table, the big 6, joins, CTEs, then window functions.
- **[Tips for anyone thinking about a career in data](https://www.facebook.com/share/p/1BzzdsFHvP/)** · Facebook, Vietnamese
  Quick-fire rules for SQL, coding, BI tools and learning in general. CTEs over subqueries, no `t1, t2, t3` aliases, no 3D charts, no stock-prediction projects, and nobody cares about your 100 Coursera certificates.
- **[SQL roadmap](https://www.facebook.com/share/p/1CVB5P864e/)** · Facebook, Vietnamese
  A complete checklist for learning SQL querying in four levels: beginner (the big 6, joins), intermediate (CTEs, `CASE WHEN`, pivots, NULLs), advanced (window functions, dates, strings) and proficient (recursive CTEs, regex, semi-structured data, Jinja in dbt, query optimisation). My most shared post.

## 2. Build projects that get you hired

- **[Data Project Guide & Advice 101](https://www.facebook.com/share/p/1HfUQWpDzo/)** · Facebook, Vietnamese
  What a good project looks like for each role. It uses a simple mental model: data **producers** (data engineers, analytics engineers) put data into the warehouse; **consumers** (analysts, data scientists) take it out. Includes example project shapes and the criteria I review them against, plus links to my own projects. Pairs with the [GitHub guide](../github/README.md).
- **[Component of a Technical Data Project, Part 1: The prerequisite](https://markphammm.substack.com/p/component-of-a-technical-data-project)** · Substack, English
  The software engineering basics every data side project needs: repo structure, Git, dependency and virtual-environment management, environment variables, and OOP/DRY. How to go from messy notebooks to projects recruiters take seriously.
- **[Component of a Technical Data Project, Part 2: Building blocks](https://markphammm.substack.com/p/component-of-a-technical-data-project-59e)** · Substack, English
  A tour of a local ELT setup: ingestion, warehouse, transformation, BI and orchestration, plus version control and CI/CD. How the tools fit together.

## 3. Dashboards and BI

- **[How to design a dashboard](https://www.facebook.com/share/p/1CWqrpxXHC/)** · Facebook, Vietnamese
  My notes on the 70-page book *How to Design a Dashboard*: the **DPBD** process (Define, Prototype, Build, Deploy) and the **ACES** criteria (Accurate, Clear, Empowering, Succinct). I used these in a lot of internship and full-time interviews.
- **[Power BI or Tableau? Wrong question.](https://markphammm.substack.com/p/power-bi-or-tableau-wrong-question)** · Substack, English
  The dashboard principles that survive every tool migration. The longer English version of the post above.
- **[Mode Analytics](https://www.facebook.com/share/p/19ycyUhoyQ/)** · Facebook, Vietnamese
  Why I moved from Power BI to Mode (SQL-native, Python notebooks on top of query results, nothing to install, works on a Mac) and how to connect it to the Xóm Data SQL Server. One of my mentees landed an internship offer with a Mode project on airline reviews.

## 4. Analytics engineering

- **[I tell people I'm an AE, but wtf does that mean?](https://markphammm.substack.com/p/i-tell-people-im-an-ae-so-wtf-does)** · Substack, English
  What an analytics engineer does, explained with a kitchen analogy: how the role differs from data engineers, analysts and data scientists, and why the shift from ETL to ELT created it. Good to send to family, too.
- **I rebuilt my ingestion pipeline with zero infrastructure** · Substack, English. A three-part series; read in order.
  1. **[Neon Postgres WAL, Snowflake credentials and Fivetran CDC](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with)**: replacing a custom scraper, Airflow and Terraform with a managed connector. Postgres logical replication, key-pair auth for service accounts, and the trade-offs of managed CDC.
  2. **[dbt, run by Fivetran](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with-02e)**: using the ingestion vendor as your dbt orchestrator. No dbt Cloud, no Airflow, no server.
  3. **[CDC, and the two numbers that came out wrong](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with-85c)**: changing five rows in Postgres, following them to the reporting tables, and finding out why the revenue was off (soft deletes and hash-based row identity).

## 5. Job search

- **[Resume 101](https://www.facebook.com/share/p/19LZiZWfUK/)** · Facebook, Vietnamese
  The most common resume mistakes I see, including in real applicant pipelines: photo templates instead of a clean (Jake's) resume, uneven margins, links that don't click, empty GitHub links, and bullets that aren't *what you did, how, and the result* in two lines or fewer. A resume is like a dating profile: you get 3–5 seconds. The full version is the [resume guide](../resume/README.md).

## 6. Set up your machine

- **[Some productivity hacks for VS Code / Cursor on macOS](https://www.facebook.com/share/p/1FrnEAvqwm/)** · Facebook, mostly English
  My `keybindings.json` (format-and-save in one shortcut with Black and SQLFluff), my `.zshrc` aliases for dbt, git and Docker, CLI tools I use every day (zoxide, eza, lazygit, Warp) and the keyboard shortcuts worth learning.
- **[I got a new Mac and refused to set it up by hand again](https://markphammm.substack.com/p/i-got-a-new-mac-and-refused-to-set)** · Substack, English
  One repo, four scripts (bootstrap, link, configure, verify) and about twenty minutes from a factory-fresh laptop to a working analytics engineering machine.
- **[Understanding pip, Poetry and uv](https://markphammm.substack.com/p/understanding-pip-poetry-and-uv)** · Substack, English
  The three Python dependency managers compared on a small pandas + DuckDB + pytest app: lock files, virtual environments, and when to use which.

## 7. Go deeper: free articles from vutr

[vutr](https://vutr.substack.com) is Vu Trinh's data engineering newsletter, read by 19,000+ engineers. I'm a technical writer there. These are the free articles I'd read first, all in English. They're for when you're ready to understand what happens *under* the tools.

**Want more?** [vutr.md](vutr.md) lists **every free article** (131, plus 44 GroupBy roundups) by topic, including my two guest posts on rebuilding my junior-year project.

**Warehouses, file formats and dbt**

- **[Why is dbt so popular?](https://vutr.substack.com/p/why-is-dbt-so-popular)**: the problem dbt solves and why it's becoming the standard for transformation. Read this before your first dbt project.
- **[The internals of BigQuery, Snowflake, Databricks and Redshift](https://vutr.substack.com/p/the-internal-of-bigquery-snowflake)**: four cloud data warehouses compared in one article.
- **[I spent 8 hours learning Parquet. Here's what I discovered](https://vutr.substack.com/p/the-overview-of-parquet-file-format)**: how the file format behind most data lakes actually stores data.

**Spark**

- **[The overview of Apache Spark](https://vutr.substack.com/p/the-overview-of-apache-spark)**: how "the infamous data processing engine" works.
- **[How is Databricks' Spark different from open-source Spark?](https://vutr.substack.com/p/how-is-databricks-spark-different)**: and why Databricks doesn't just use the open-source version.

**Kafka and streaming**

- **[If you're learning Kafka, this article is for you](https://vutr.substack.com/p/if-youre-learning-kafka-this-article)**: a baseline for learning Kafka. The newsletter's most popular post.
- **[The company that created Kafka is replacing it with a new solution](https://vutr.substack.com/p/the-company-that-created-kafka-is)**: how LinkedIn built Northguard, its new scalable log storage.

**Orchestration and Python**

- **[Where does your task run in Apache Airflow?](https://vutr.substack.com/p/where-does-your-task-run-in-apache)**: everything about Airflow executors.
- **[I spent 10 hours learning multithreading and multiprocessing](https://vutr.substack.com/p/free-i-spent-10-hours-learning-multithreading)**: a mental model for concurrency, in a Python context.

**Real-world systems and projects**

- **[I spent 5 hours understanding how Uber built their ETL pipelines](https://vutr.substack.com/p/i-spent-5-hours-understanding-how)**: spoiler, they don't use batch or stream pipelines.
- **[Build a lakehouse on a laptop with dbt, Airflow, Trino, Iceberg and MinIO](https://vutr.substack.com/p/build-a-lakehouse-on-a-laptop-with)**: a pet project for learning data engineering, entirely on your own machine.
