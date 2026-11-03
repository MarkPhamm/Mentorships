# Sources: where the data comes from

← Back to the [data stack guide](../README.md)

The data source decides more about your project than any tool does. It decides whether your project is original, whether there's real engineering in it, and whether you'll care enough to finish it.

Think of it as a ladder. Each step up is harder, more original and more like a real job.

| Level | Source | Effort | Originality | Good for |
|---|---|---|---|---|
| 1 | **Static files:** Kaggle, Maven Analytics, course datasets | Low | Low | Learning a tool. Rarely a portfolio project on its own |
| 2 | **Public open data:** government portals, open data bulk downloads | Low to medium | Medium | Analyst and AE projects with real, messy data |
| 3 | **APIs:** public REST APIs that keep updating | Medium | Medium to high | DE projects (incremental loads), AE projects with fresh data |
| 4 | **Web crawling:** sites with no API | High | High | DE projects. A dataset nobody else has |
| 5 | **Your own data:** your club, a family business, an app you built, something you log | Varies | Highest | Any role. Real stakeholders, real story |

## Level 1: static files (Kaggle CSVs)

Fine for learning dbt or Power BI for the first time. Weak as a portfolio piece, because the hiring manager has seen the same file from other candidates, sometimes the same week.

If you must use one:

- **Avoid the classics:** Titanic, Iris, house prices, Superstore, AdventureWorks, Netflix, Spotify, COVID.
- **Pick a dataset with fewer than a few hundred downloads,** or combine two that nobody has joined before.
- **Treat the CSV as a source system, not a finished table.** Load it raw into a warehouse, then model it. That at least turns a Kaggle file into an AE exercise.

## Level 2: public open data

Government and public bodies publish real, messy, regularly updated data, often with bulk downloads and an API. Messy is good: cleaning it is the work.

- Look at national and city open data portals, central banks, statistics offices, transport agencies, consumer protection agencies.
- **Read the data dictionary before you start.** If there isn't one, that's a project in itself.

**In my projects:** [local_warehouse_pipeline](https://github.com/MarkPhamm/local_warehouse_pipeline) uses the CFPB (US Consumer Financial Protection Bureau) consumer complaint database, filtered to the companies and start date I choose in a config file. Public, but few candidates use it, and it updates every day, so an incremental pipeline makes sense. I wrote up how it works [on Substack](https://substack.com/home/post/p-178105495).

## Level 3: APIs

An API that updates is the first source that forces real data engineering: auth, pagination, rate limits, retries and incremental loads.

What to check before you commit:

- **Does it keep updating?** A live source gives your pipeline a reason to run on a schedule.
- **Free tier and rate limits.** Can you backfill the history you need without getting blocked or billed?
- **Can you load incrementally?** Look for an `updated_at` field, a cursor or a date filter. Without one, you'll be reloading everything every time.
- **Terms of use.** Read them. Some APIs don't allow storing or republishing the data.

Places to look: finance and crypto price APIs, weather, public transport and flight data, sports stats, game platforms, GitHub's own API, and any app you already use every day.

**In my projects:** [local_streaming_pipeline](https://github.com/MarkPhamm/local_streaming_pipeline) streams live crypto prices from Coinbase. Prices that change every second are the reason the project needs Kafka at all.

## Level 4: web crawling

When a site has the data but no API, you build the scraper. This is where you get a dataset nobody else has, and the most engineering to talk about in an interview.

- **Check `robots.txt` and the site's terms first.** Don't scrape behind a login, don't collect personal data, and don't publish anything you're not allowed to.
- **Be polite:** rate-limit your requests, add retries with backoff, set a real user agent, and cache pages so you don't hit the site twice for the same page.
- **Store the raw HTML or JSON before you parse it.** When your parser breaks (it will), you re-parse instead of re-scraping.
- **Plan for change.** Sites change their layout. Tests on your parser, and an alert when a run returns zero rows, are the difference between a script and a pipeline.
- **Parallelise once it works.** One page at a time is fine for 100 pages, not for 100,000.

**In my projects:** for [Skytrax reviews](https://github.com/MarkPhamm/skytrax_reviews) I scraped 160K+ airline, seat, lounge and airport reviews from AirlineQuality.com with BeautifulSoup and 26 parallel Airflow tasks. The site has since shut down permanently, so nobody can recreate this dataset. That's an only-me fact, and it came from picking a hard source.

## Level 5: your own data

The best source is one only you have access to: your university club's membership and event data, a family shop's sales, a nonprofit's donors, your own fitness or spending logs, a community you run, an app you built.

- **You get real stakeholders.** Someone will actually use your dashboard and tell you it's wrong. That's the best interview story there is.
- **Get permission and anonymise.** Never publish personal data. Hash IDs, drop names and emails, and publish a sample or synthetic copy if the raw data can't go public.
- **You can go one level further with a real database.** Put the data in Postgres and replicate it into a warehouse with CDC, the way production systems work.

**In my projects:** for [fivetran_snowflake_dbt_demo](https://github.com/MarkPhamm/fivetran_snowflake_dbt_demo) I rebuilt my ingestion as a real app database: Neon Postgres, replicated into Snowflake by Fivetran CDC, then dbt. Changing five rows in Postgres and following them to the reporting tables is how I found out why revenue came out wrong. The full story is in [my three-part Substack series](https://markphammm.substack.com/p/i-rebuilt-my-ingestion-pipeline-with).

— Mark Pham
