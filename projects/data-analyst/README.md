# Data analyst: the question, the SQL, the dashboard, the takeaway

← Back to the [projects guide](../README.md)

An analyst gets paid to help someone make a better decision. Your project should look like that, not like a chart gallery.

- **A real question.** "Do flash sales on Shopee actually save you money?" beats "E-commerce sales analysis". Write the question at the top of the README. If you can't write it in one sentence, you don't have a project yet.
- **The SQL.** Analysts are hired on SQL. Put your queries in the repo as `.sql` files, not buried in a notebook or hidden behind a BI tool's drag-and-drop. CTEs over nested subqueries, readable aliases (no `t1, t2, t3`), window functions where they fit. A reviewer should be able to read your SQL and follow your thinking.
- **The dashboard UI.** Design for the person reading it, not for yourself:
  - The most important number top-left, big. Details below and to the right.
  - One question per page. If a page needs a paragraph to explain, split it.
  - No 3D charts, no pie charts with 12 slices, no rainbow colour schemes. Colour means something or it's grey.
  - Filters that a stakeholder would actually use (date, region, segment), not every column in the table.
  - Check it against **ACES**: Accurate, Clear, Empowering, Succinct. More in [How to design a dashboard](https://www.facebook.com/share/p/1CWqrpxXHC/) and [Power BI or Tableau? Wrong question.](https://markphammm.substack.com/p/power-bi-or-tableau-wrong-question) Which tool to use is in [picking a BI tool](../../data-stack/6-serving/README.md)
- **The takeaway.** This is what separates an analyst from someone who knows Power BI. End with 3 to 5 findings and what you'd recommend: *"Reviews mentioning delays score 2.1 points lower, and delays are 40% of 1-star reviews. If I ran this airline, I'd fix on-time performance before seat comfort."* (Illustration only, don't copy it.) Charts without a conclusion are homework.
- **Honest limits.** Sample size, bias in the data, what you couldn't answer. Interviewers love this.

**Where analysts go wrong:** the Superstore dashboard, 15 charts with no story, "insights" that restate the chart ("Sales were highest in Q4"), and no SQL anywhere.

**From my mentees:** three of them built analyst projects on top of my Skytrax warehouse. Same data, but each one picked one airline and one question, and ended with an answer:

- **[Delta](https://github.com/alyssaqle/airline_customer_exp_analysis):** what drives satisfaction in each cabin class. Mode dashboard.
- **[Frontier](https://github.com/gwenniehub/frontier-reviews-dashboard):** how Frontier compares with other ultra-low-cost airlines. Mode dashboard.
- **[Spirit](https://github.com/MiaTran1112/spirit_airlines_dashboard):** why Spirit's reviews stay low. Mode dashboard.

Another mentee built a [Next.js dashboard and review explorer](https://github.com/nguyentienTCU/Skytrax_Reviews_Dashboard) over the same data. Notice none of them is "Airline reviews analysis". Each is scoped to one airline and one question, and that's what makes them different from each other and from the rest of the pile.

## Project ideas

Each idea below is an **illustration of a shape**, not a project to copy. If 50 of my mentees build the same idea because it's on this list, it becomes the new Titanic. Change at least one of the source, the question or the audience (better, all three), so it passes the [only-me test](../../mentality/4-competitive-advantage/README.md).

What matters: a sharp question, clean SQL, a dashboard someone could use, and a takeaway.

- **Your city, by public data.** Pick one question about where you live (which districts get the slowest response to complaints? which bus routes are always late?) from the city's open data. End with a recommendation addressed to someone real, like the transport authority.
- **A market you actually shop in.** Track prices of 50 products you buy on an e-commerce site for a month (with an API or a polite scraper) and answer: do discounts actually save money, or are prices raised first?
- **A community you're part of.** Your club's event attendance, your Discord server's activity, a sports league's stats. Build the dashboard the organisers would actually open every week, then ask them for feedback and put it in the README.
- **Reviews and text.** Ratings plus review text from a public source in an industry you want to work in. Which complaints drive the lowest scores? Industry matters: an analyst project in insurance data helps when you apply to insurance companies.

**Level up:** put the SQL in versioned `.sql` files, build the dashboard on a warehouse (DuckDB or BigQuery) instead of a spreadsheet, and write a one-page memo of findings as if for a manager.

— Mark Pham
