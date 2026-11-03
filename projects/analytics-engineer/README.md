# Analytics engineer: the model, the tests, the docs

← Back to the [projects guide](../README.md)

An analytics engineer turns raw data into tables the business can trust. Your project should show you can design that model, not only write `SELECT`s.

- **Layered dbt models.** Staging (one model per source table: rename, cast, nothing clever) → intermediate (joins, business logic) → marts (what BI reads). Every layer has one job. Name them consistently (`stg_`, `int_`, `fct_`, `dim_`).
- **A deliberate data model.** Kimball star schema with facts and dimensions is the safe default. Know and write down the **grain** of every fact table ("one row per review"). Surrogate keys, slowly changing dimensions if your data needs them. Draw the ER diagram.
- **Data quality checks.** `unique` and `not_null` on every primary key is the floor, not the ceiling. Add `relationships` between facts and dimensions, `accepted_values`, freshness checks on sources, and at least one custom test for a business rule only your data has. Show what happens when a test fails.
- **Incremental models** where the data is large or append-only, and an explanation of why.
- **Docs.** Descriptions on models and columns, generated dbt docs, ideally hosted somewhere a reviewer can click.
- **CI.** A GitHub Actions workflow that runs SQLFluff and `dbt build` on pull requests. Slim CI (`state:modified+`) if you want to go one level deeper.
- **A thin serving layer.** One dashboard or a semantic layer (MetricFlow) on top of your marts, to prove the model answers real questions.

**Where analytics engineers go wrong:** one giant model with 400 lines of SQL, tests only on one column, no stated grain, "dbt project" that's really a folder of views with no layers, and the jaffle shop sample with a new name.

## Project ideas

Each idea below is an **illustration of a shape**, not a project to copy. If 50 of my mentees build the same idea because it's on this list, it becomes the new Titanic. Change at least one of the source, the question or the audience (better, all three), so it passes the [only-me test](../../mentality/4-competitive-advantage/README.md).

What matters: a layered dbt project, a deliberate model with a stated grain, data quality tests, docs and CI.

- **Model a public source into a star schema.** Take a messy public dataset (complaints, inspections, transport, procurement), load it raw, and build staging → intermediate → marts with facts, dimensions, a written grain, and tests that catch real problems you found in the data.
- **Two sources, one model.** Join data that wasn't designed to fit: an API plus a public dataset, two countries' versions of the same statistic. Conforming dimensions across sources is daily AE work and almost nobody shows it.
- **Slowly changing dimensions.** Pick data where attributes change over time (product prices, company names, player teams), snapshot it daily with dbt snapshots, and build a fact table that joins to the right version at the right time.
- **A semantic layer.** Define metrics once in MetricFlow (or your BI tool's semantic layer) on top of your marts, and show two dashboards agreeing on the same number.
- **CI/CD for dbt.** Slim CI on pull requests, SQLFluff, deferred builds against production state, docs deployed on merge. This is the infrastructure side of AE, and it's what my [skytrax_reviews_transformation](https://github.com/MarkPhamm/skytrax_reviews_transformation) repo is about ([live dbt docs](https://d38l3fc9bckvbz.cloudfront.net/#!/overview/ba_transformation?g_v=1)).

**Level up:** add source freshness checks, a custom generic test for a business rule only your data has, an ER diagram of your marts, and hosted dbt docs.

— Mark Pham
