# Project ideas and data sources

This is part two of the [projects guide](../README.md). Read that first so you know which role you're building for and which layer of the stack it owns.

Here: how to pick a data source, then project ideas for each role.

**A warning before the ideas.** Every idea on this page is an illustration. If 50 of my mentees build "the Steam reviews pipeline" because it's on this list, it becomes the new Titanic. Use these to see the *shape* of a good project, then swap in a question, a source or a community that's yours. That's the [only-me test](../../mentality/4-competitive-advantage/README.md).

---

## Picking a data source

The data source decides more about your project than any tool does. It decides whether your project is original, whether there's real engineering in it, and whether you'll care enough to finish it.

Think of it as a ladder. Each step up is harder, more original and more like a real job.

| Level | Source | Effort | Originality | Good for |
|---|---|---|---|---|
| 1 | **Static files:** Kaggle, Maven Analytics, course datasets | Low | Low | Learning a tool. Rarely a portfolio project on its own |
| 2 | **Public open data:** government portals, open data bulk downloads | Low to medium | Medium | Analyst and AE projects with real, messy data |
| 3 | **APIs:** public REST APIs that keep updating | Medium | Medium to high | DE projects (incremental loads), AE projects with fresh data |
| 4 | **Web crawling:** sites with no API | High | High | DE projects. A dataset nobody else has |
| 5 | **Your own data:** your club, a family business, an app you built, something you log | Varies | Highest | Any role. Real stakeholders, real story |

### Level 1: static files (Kaggle CSVs)

Fine for learning dbt or Power BI for the first time. Weak as a portfolio piece, because the hiring manager has seen the same file from other candidates, sometimes the same week.

If you must use one:

- **Avoid the classics:** Titanic, Iris, house prices, Superstore, AdventureWorks, Netflix, Spotify, COVID.
- **Pick a dataset with fewer than a few hundred downloads,** or combine two that nobody has joined before.
- **Treat the CSV as a source system, not a finished table.** Load it raw into a warehouse, then model it. That at least turns a Kaggle file into an AE exercise.

### Level 2: public open data

Government and public bodies publish real, messy, regularly updated data, often with bulk downloads and an API. Messy is good: cleaning it is the work.

- Look at national and city open data portals, central banks, statistics offices, transport agencies, consumer protection agencies.
- **Read the data dictionary before you start.** If there isn't one, that's a project in itself.

**In my projects:** [local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline) uses the CFPB (US Consumer Financial Protection Bureau) consumer complaint database, filtered to the companies and start date I choose in a config file. Public, but few candidates use it, and it updates every day, so an incremental pipeline makes sense.

### Level 3: APIs

An API that updates is the first source that forces real data engineering: auth, pagination, rate limits, retries and incremental loads.

What to check before you commit:

- **Does it keep updating?** A live source gives your pipeline a reason to run on a schedule.
- **Free tier and rate limits.** Can you backfill the history you need without getting blocked or billed?
- **Can you load incrementally?** Look for an `updated_at` field, a cursor or a date filter. Without one, you'll be reloading everything every time.
- **Terms of use.** Read them. Some APIs don't allow storing or republishing the data.

Places to look: finance and crypto price APIs, weather, public transport and flight data, sports stats, game platforms, GitHub's own API, and any app you already use every day.

**In my projects:** [local_streaming_pipeline](https://github.com/MarkPhamm/local_streaming_pipeline) streams live crypto prices from Coinbase. Prices that change every second are the reason the project needs Kafka at all.

### Level 4: web crawling

When a site has the data but no API, you build the scraper. This is where you get a dataset nobody else has, and the most engineering to talk about in an interview.

- **Check `robots.txt` and the site's terms first.** Don't scrape behind a login, don't collect personal data, and don't publish anything you're not allowed to.
- **Be polite:** rate-limit your requests, add retries with backoff, set a real user agent, and cache pages so you don't hit the site twice for the same page.
- **Store the raw HTML or JSON before you parse it.** When your parser breaks (it will), you re-parse instead of re-scraping.
- **Plan for change.** Sites change their layout. Tests on your parser, and an alert when a run returns zero rows, are the difference between a script and a pipeline.
- **Parallelise once it works.** One page at a time is fine for 100 pages, not for 100,000.

**In my projects:** for [Skytrax reviews](https://github.com/MarkPhamm/skytrax_reviews) I scraped 160K+ airline, seat, lounge and airport reviews from AirlineQuality.com with BeautifulSoup and 26 parallel Airflow tasks. The site has since shut down permanently, so nobody can recreate this dataset. That's an only-me fact, and it came from picking a hard source.

### Level 5: your own data

The best source is one only you have access to: your university club's membership and event data, a family shop's sales, a nonprofit's donors, your own fitness or spending logs, a community you run, an app you built.

- **You get real stakeholders.** Someone will actually use your dashboard and tell you it's wrong. That's the best interview story there is.
- **Get permission and anonymise.** Never publish personal data. Hash IDs, drop names and emails, and publish a sample or synthetic copy if the raw data can't go public.
- **You can go one level further with a real database.** Put the data in Postgres and replicate it into a warehouse with CDC, the way production systems work.

**In my projects:** for [fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo) I rebuilt my ingestion as a real app database: Neon Postgres, replicated into Snowflake by Fivetran CDC, then dbt. Changing five rows in Postgres and following them to the reporting tables is how I found out why revenue came out wrong. The full story is in [my three-part Substack series](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with).

---

## Project ideas by role

Each idea below is an **illustration of a shape**, not a project to copy. Change at least one of: the source, the question, or the audience. Better, change all three.

### Data analyst

What matters: a sharp question, clean SQL, a dashboard someone could use, and a takeaway.

- **Your city, by public data.** Pick one question about where you live (which districts get the slowest response to complaints? which bus routes are always late?) from the city's open data. End with a recommendation addressed to someone real, like the transport authority.
- **A market you actually shop in.** Track prices of 50 products you buy on an e-commerce site for a month (with an API or a polite scraper) and answer: do discounts actually save money, or are prices raised first?
- **A community you're part of.** Your club's event attendance, your Discord server's activity, a sports league's stats. Build the dashboard the organisers would actually open every week, then ask them for feedback and put it in the README.
- **Reviews and text.** Ratings plus review text from a public source in an industry you want to work in. Which complaints drive the lowest scores? Industry matters: an analyst project in insurance data helps when you apply to insurance companies.

**Level up:** put the SQL in versioned `.sql` files, build the dashboard on a warehouse (DuckDB or BigQuery) instead of a spreadsheet, and write a one-page memo of findings as if for a manager.

### Analytics engineer

What matters: a layered dbt project, a deliberate model with a stated grain, data quality tests, docs and CI.

- **Model a public source into a star schema.** Take a messy public dataset (complaints, inspections, transport, procurement), load it raw, and build staging → intermediate → marts with facts, dimensions, a written grain, and tests that catch real problems you found in the data.
- **Two sources, one model.** Join data that wasn't designed to fit: an API plus a public dataset, two countries' versions of the same statistic. Conforming dimensions across sources is daily AE work and almost nobody shows it.
- **Slowly changing dimensions.** Pick data where attributes change over time (product prices, company names, player teams), snapshot it daily with dbt snapshots, and build a fact table that joins to the right version at the right time.
- **A semantic layer.** Define metrics once in MetricFlow (or your BI tool's semantic layer) on top of your marts, and show two dashboards agreeing on the same number.
- **CI/CD for dbt.** Slim CI on pull requests, SQLFluff, deferred builds against production state, docs deployed on merge. This is the infrastructure side of AE, and it's what my [skytrax_reviews_transformation](https://github.com/MarkPhamm/skytrax_reviews_transformation) repo is about.

**Level up:** add source freshness checks, a custom generic test for a business rule only your data has, an ER diagram of your marts, and hosted dbt docs.

### Data engineer

What matters: real ingestion, incremental and idempotent loads, orchestration, infrastructure as code, and depth on one hard thing.

- **A scraper that runs every day.** Crawl a site with no API, land raw pages in object storage partitioned by date, parse into a warehouse, and schedule it. Show what happens when the site's layout changes.
- **An incremental API pipeline.** An API with history: backfill once, then load only new records daily. Prove idempotency: run the same day twice and show the row count doesn't change.
- **CDC from an app database.** Run Postgres with a small app (or a script simulating one) writing inserts, updates and deletes, replicate it into a warehouse, and handle soft deletes properly.
- **Streaming with a reason.** Live data that genuinely changes by the second (prices, transit vehicle positions, game events) through Kafka into a real-time store and a live dashboard. If the data updates once a day, it's not a streaming project.
- **A lakehouse on a laptop.** Object storage (MinIO), Iceberg tables, a query engine (Trino), dbt and an orchestrator, all in Docker Compose. My [local_lakehouse_pipeline](https://github.com/MarkPhamm/local_lakehouse_pipeline) does this with NYC taxi data. That data is a classic, so if you build one, pick a source nobody else uses.

**Level up:** Terraform for every cloud resource, OIDC or key-pair auth instead of static keys, alerts when a run fails or returns zero rows, and a README section on cost.

---

## From idea to finished project

1. **Write the one-sentence question or goal** before you write any code.
2. **Find the source** and check it: does it update, can you load it incrementally, are you allowed to use it?
3. **Build the thinnest version end to end first:** source to a single table to a single chart. Then go deep on the layer your role owns.
4. **Write the README as you go,** not at the end. Use the [template in the GitHub guide](../../github/README.md#5-inside-a-project-the-readme).
5. **Ship it, then run the [self-review checklist](../README.md#self-review-checklist),** including the copy-paste test.

— Mark Pham
