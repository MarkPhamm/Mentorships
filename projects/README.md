# Building data projects that get you hired

A project is the only part of your application that isn't a claim. Your resume says you know SQL, dbt and Airflow. A project shows it. That's why it's the first thing I open when I review a mentee, and the first thing a good hiring manager opens too.

**When you're going for your first data role, projects are your main competitive advantage.** You don't have years of experience to compete on, and neither does anyone else in the pile. What you can control is what you build. On your resume, aim for **2 to 3 projects alongside 2 to 3 experiences** (non-US internships, part-time jobs, research, a club role). That's the best format for a one-page resume at this stage. More projects than that means each one gets a single shallow line; fewer means your resume rests on experience you don't have yet. More in the [resume guide](../resume/README.md#3-projects).

The problem: most data projects look the same. Download a Kaggle CSV, open a notebook, make a few bar charts, call it "Sales Analysis". Or follow a YouTube "end-to-end data engineering project" step by step and end up with the exact same repo as 10,000 other people. Those are **minion projects**. They prove you can follow instructions. Everyone can.

Start with the [data stack guide](../data-stack/README.md): the layers every project is built on, how to pick a data source and how to pick a BI tool. Then read the page for your role:

| Role | What your project should show |
|---|---|
| [Data analyst](data-analyst/README.md) | The question, the SQL, the dashboard and the takeaway, plus project ideas |
| [Analytics engineer](analytics-engineer/README.md) | The model, the tests and the docs, plus project ideas |
| [Data engineer](data-engineer/README.md) | Ingestion, reliability and infrastructure, plus project ideas |

Once the project exists, the [GitHub guide](../github/README.md) covers how to present it.

---

## Before you start: pick the role, then the project

Don't start with the tool ("I want to learn Kafka"). Start with the job you're applying for, then build the project that job would review.

I think about data people in two groups:

- **Producers** put data into the warehouse and make it trustworthy: data engineers and analytics engineers.
- **Consumers** take data out of the warehouse and turn it into decisions: data analysts and data scientists.

A data analyst project that spends 80% of its README on Terraform is aimed at the wrong reader. A data engineer project that's a notebook with charts is too. Know which side you're on, and make the part of the stack your role owns the deepest part of your project.

You don't need to build the whole stack every time. But you need to know where your work sits in it, because every interviewer will ask.

---

## Which part of the stack is yours

Same stack, different depth. Here's where each role should spend most of its effort, and what I look for when I review it.

| | Data analyst | Analytics engineer | Data engineer |
|---|---|---|---|
| **Owns** | Serving / BI | Transformation | Ingestion, warehouse, infra |
| **Main output** | A dashboard or analysis that answers a question | A tested, documented data model | A pipeline that runs reliably without you |
| **Can be light on** | Ingestion and infra (a clean dataset is fine) | Infra (a local DuckDB is fine) | The dashboard (one simple chart is fine) |
| **First thing I open** | The dashboard and the "so what" | The dbt lineage graph and the tests | The architecture diagram and the DAG |

---

## From idea to finished project

1. **Write the one-sentence question or goal** before you write any code.
2. **Find the source** and check it: does it update, can you load it incrementally, are you allowed to use it?
3. **Build the thinnest version end to end first:** source to a single table to a single chart. Then go deep on the layer your role owns.
4. **Write the README as you go,** not at the end. Use the [template in the GitHub guide](../github/README.md#5-inside-a-project-the-readme).
5. **Ship it, then run the [self-review checklist](#self-review-checklist),** including the copy-paste test.

---

## What every project needs, whatever the role

- **A README a stranger can follow:** the problem, an architecture diagram, the stack, results, how to run it, what you'd do next. Template in the [GitHub guide](../github/README.md#5-inside-a-project-the-readme).
- **It runs on someone else's machine.** One command, or a short list of exact commands. If a reviewer can't run it, assume they won't try.
- **Numbers.** Rows processed, run time, cost, test count, how much faster. "160K+ reviews" is a fact; "a large dataset" is filler.
- **A reason for every tool.** "I used Kafka because it's popular" is a red flag. "I used DuckDB because it's free, local and fast enough for 2 GB" is an answer.
- **Your own decisions.** The part of the project you'd defend in an interview. If you can't explain a line, it came from a tutorial.

---

## Common mistakes

- **The minion project:** a Kaggle classic or a tutorial, followed step by step, with your name on it.
- **Tool soup:** Kafka, Spark, Airflow, Kubernetes and dbt on 5,000 rows of static CSV. Use the tools the problem needs, then go deep.
- **Wrong depth for the role:** an analyst project that's all infrastructure, or an engineering project that's all charts.
- **No question, no takeaway:** a dashboard that shows data but doesn't say anything.
- **Not runnable:** hard-coded paths, missing `requirements.txt` or `pyproject.toml`, secrets in the code.
- **Ten half-finished projects instead of two finished ones.** Finish, document, then start the next.

---

## Self-review checklist

**The basics**

- [ ] I can say which role this project is for, and the deepest part of it is the part that role owns.
- [ ] I can draw the stack from source to dashboard and point to where each tool sits.
- [ ] Every tool has a reason I'd say out loud in an interview.
- [ ] My resume has 2 to 3 projects next to 2 to 3 experiences, and this one is good enough to be one of them.

**By role**

- [ ] *Analyst:* one clear question at the top, SQL in the repo, a dashboard that passes ACES, and 3 to 5 takeaways with a recommendation.
- [ ] *Analytics engineer:* staging → intermediate → marts, a stated grain for every fact, tests beyond `unique` and `not_null`, docs, and CI.
- [ ] *Data engineer:* real ingestion, incremental and idempotent loads, a raw landing zone, orchestration with retries, and IaC or Docker.

**Presentation**

- [ ] The README has a diagram, real numbers, run instructions and "what I'd do next".
- [ ] A stranger can clone it and run it.
- [ ] No secrets in the repo or its history.

**The copy-paste test**

- [ ] Could 1,000 other candidates have this exact repo? If yes, change the data, the question or the depth until the answer is no. Start with the project ideas in each role's page.

— Mark Pham
