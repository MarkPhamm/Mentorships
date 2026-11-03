# Serving: dashboards and BI tools

← Back to the [data stack guide](../README.md)

"Power BI or Tableau?" is the question I get asked most, and it's the wrong question. Companies migrate BI tools every few years. The dashboard principles (one question per page, the most important number first, no 3D charts, a takeaway at the end) survive every migration. Learn those first; the tool is the easy part. The long version is [Power BI or Tableau? Wrong question.](https://markphammm.substack.com/p/power-bi-or-tableau-wrong-question)

That said, you have to pick something for your project. Here's how I'd choose.

## Start from the job, not the tool

- **Read 20 job posts for the role you want, in the country you want.** Count which BI tools they name. If it's Power BI 15 times out of 20, your project uses Power BI. Done.
- **Then check who can see it.** A dashboard a recruiter can't open is a screenshot. Prefer a tool with a public link, or record a short video.
- **Then check your laptop.** Power BI Desktop only runs on Windows. On a Mac, that decides for you.

## The options

| Tool | Good for | Watch out for |
|---|---|---|
| **Power BI** | The most common tool in job posts at many companies, especially ones that run on Microsoft | Desktop is Windows-only; publishing a public link needs the web service |
| **Tableau** | Strong visuals; Tableau Public gives you a free public link | Free version makes your data public |
| **Looker Studio** | Free, in the browser, easy to share, connects to BigQuery and Google Sheets | Limited modelling; slow on big data |
| **Mode** | SQL-native: write the query, chart the result, add a Python notebook on top. Nothing to install, works on a Mac | Less common in job posts than Power BI or Tableau |
| **Metabase / Superset** | Open source, runs in Docker next to your pipeline, good for DE and AE projects | You host it yourself |
| **Streamlit** | A Python app instead of a dashboard: interactive, deployable, fully custom | You write the UI code; it's not what most analyst roles use day to day |
| **Omni, Hex, Looker** | Modern tools with a semantic layer or notebooks; worth knowing for AE roles | Free tiers are limited or trial-only |

## How I'd choose by role

- **Data analyst:** the tool the job posts ask for. The dashboard *is* your project, so the tool matters most here. If your posts are split, pick the one you can share publicly.
- **Analytics engineer:** something SQL-first that sits on your marts (Mode, Metabase, or a semantic layer like MetricFlow). The model is the project; the BI tool only proves the model answers questions.
- **Data engineer:** whatever is fastest to run next to your pipeline (Metabase or Superset in Docker, Streamlit, or a simple web dashboard). One chart is enough.

**My take:** I moved from Power BI to Mode because it's SQL-native, lets me run Python on top of the query results, needs nothing installed, and works on a Mac. The reasons are in my [Mode Analytics post](https://www.facebook.com/share/p/19ycyUhoyQ/) (Vietnamese). My mentees built their Skytrax dashboards in Mode (see the [data analyst page](../../projects/data-analyst/README.md)), and one of them landed an internship offer with a Mode project on airline reviews.

## Common mistakes

- **Learning three BI tools at a surface level** instead of one well, plus SQL.
- **A tool nobody can open:** a `.pbix` file in a repo with no screenshots, video or link.
- **Business logic in the BI tool:** calculated fields that should be a dbt model or a SQL query. If the dashboard breaks, the logic is gone with it.
- **Choosing by what looks prettiest** instead of what the job posts ask for.

— Mark Pham
