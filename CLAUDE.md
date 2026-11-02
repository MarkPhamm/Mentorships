# CLAUDE.md

Guidance for Claude (and anyone else) working in this repo.

## What this repo is

Mentorship guidelines that Mark Pham (Senior / L6 Analytics Engineer at Infinite Lambda) shares with his mentees, mostly students and early-career people going into data roles (analytics, analytics engineering, data engineering). Each guide teaches one part of a job search, using Mark's own profiles as the worked example.

```
README.md              index of guides + "the one rule"
CLAUDE.md              this file
linkedin/README.md     LinkedIn profile guide
linkedin/images/       screenshots used by that guide
github/README.md       GitHub profile guide
github/images/
portfolio/README.md    portfolio site guide
portfolio/images/
resume/README.md       resume guide (LaTeX, junior-year case study)
resume/images/
readings/README.md     links to Mark's Facebook and Substack posts, grouped by topic
```

## The thesis: don't be a minion

Everything in this repo serves one idea: **if you do what everyone else does, you will not get hired.** Generic, interchangeable profiles ("Aspiring Data Analyst | SQL · Python · Power BI", Titanic notebooks, untouched portfolio templates) are what Mark calls *minion profiles*. Best practices only get a mentee to the starting line; differentiation gets them the interview.

Every guide and every edit should reinforce two tests:

1. **Copy-paste test:** could 1,000 other candidates paste this line, project or page unchanged? If yes, it's not good enough.
2. **Only-me test:** what is true about this person that isn't true about the rest of the pile? A number they produced, a tool people use, a community they run, data nobody else has, an unusual path, an obsession.

Never write advice that produces sameness, such as a fill-in-the-blanks formula or a "strong" example that is itself generic. If you add an example, ask whether it passes the copy-paste test. If it's invented, label it as an illustration and tell readers not to copy it.

## Voice and style

- Written **as Mark, in the first person** ("I", "my profile"), talking directly to a mentee ("you").
- Direct and opinionated. Plain English, short sentences, no corporate tone.
- Use the same words as the platform's UI ("Featured", "Open to Work", "Pinned").
- Don't use these words except when quoting them as bad examples: aspiring, passionate, results-driven, detail-oriented, motivated, enthusiast, team player, "turning data into insights".
- Bold lead-ins for list items (`- **Photo:** ...`). Tables for comparisons.
- A little humour is on-brand (Mark's own profiles use ¯\\\_(ツ)\_/¯); don't overdo it.

## Structure of a guide

Every guide follows the same shape:

1. **Intro:** what the platform is for, and why most people's version is a minion version.
2. **Before you start:** the foundation that comes before presentation (target role and only-me facts; projects nobody else has; whether you need a portfolio at all).
3. **Numbered sections in the order a visitor sees them on the real platform, top to bottom.** On LinkedIn: banner and photo → headline → location and links → Open to Work → About → Featured → Experience → Education → Certifications → Projects → Skills → Recommendations → Courses → Activity. GitHub and the portfolio guide follow their own page order.
4. In each section: the advice, then **"On my profile:"** (or "On my site:") with a screenshot of that section of Mark's real profile and what to notice about it.
5. **Common mistakes**, starting with the minion version.
6. **Self-review checklist**, grouped, including the copy-paste test.

Guides link to each other with relative links (`../github/README.md#anchor`). If you rename a heading, search all guides for links to its anchor.

## Facts about Mark

- **Only state facts you can verify** from Mark's real profiles: LinkedIn (linkedin.com/in/minhbphamm), GitHub (github.com/MarkPhamm), portfolio (minhbpham.com), or his local repos. Don't infer achievements, motivations or backstories.
- Profiles change. When you update an example, check the live page and add the month and year (e.g. "November 2026") in the guide intro.
- Mark's profiles don't always agree with each other (titles and start dates differ between LinkedIn, the GitHub README and the portfolio). The guides tell mentees to keep these consistent, so flag any mismatch to Mark rather than copying one version into a guide as if it were the truth.
- The portfolio's `VERSION.md` can describe work that isn't deployed yet. Describe what's live on minhbpham.com, not what the changelog says.
- Mark's resume source is a private repo (`~/Downloads/Minh_Pham_Resume` on his Mac: LaTeX source, achievements file, long-form experience doc, junior-year PDF). Only the PDF is public, at github.com/MarkPhamm/resume. Quote from it, but never publish the source files, the achievements file or job descriptions.
- The resume guide is the one exception to "differentiate everywhere": on a resume, the **layout** should be familiar and single-column; differentiation comes from the content.
- Mark's stance on resume claims is **poker, not a sworn statement**: you can say whatever you want as long as you can back it up; don't bluff too little or too much; find the sweet spot. Keep that framing (don't rewrite it into "never inflate"). The one hard line is "face-up cards": employers, titles, dates, degrees, GPA and certifications are never bluffed.

## Images

- Each guide keeps its screenshots in its own `images/` folder, named `NN-section-name.png` in page order (e.g. `07-experience.png`), and references them relatively: `![Alt text](images/07-experience.png)`.
- Crop each screenshot to the one section it illustrates. Leave out browser chrome, sidebars and the mouse cursor.
- **Privacy, because this repo is public:**
  - Never include private data: LinkedIn Analytics, profile viewers, phone numbers, personal email addresses (blur them on resume images too), or "People you may know" style sidebars.
  - Blur other people's faces (recommenders, contributors, testimonial avatars). Their names and public recommendation text can stay.
  - Tell Mark what third-party content an image contains before it's pushed.
- Prefer screenshots taken from the public view of a profile, so edit buttons don't show.
- Alt text describes what the image shows ("My Featured section"), not "screenshot".

## Adding a new guide

1. Create `<topic>/README.md` (and `<topic>/images/` if needed), following the structure above.
2. Add a row to the table in the root `README.md`.
3. Link to it from related guides where it helps.

## Git

- Mark reviews everything before it's published. Don't push without his go-ahead.
- Commit messages say what changed: `Add Recommendations section to LinkedIn guide`, not `update`.
