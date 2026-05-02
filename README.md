# Mastering Shiny for Python

Personal learning repository following the [Mastering Shiny](https://posit-dev.github.io/py-shiny/docs/) book, with additional standalone app experiments.

## Structure

```
.
├── the-book/          # Chapter-by-chapter exercises from the book
│   ├── 01-Your_first_shiny_app/
│   ├── 02-Basic_ui/
│   ├── 03-Basic_reactivity/
│   ├── 04-Case_study/         # NEISS injury data dashboard
│   ├── 06-Layout_themes_HTML/
│   ├── 07-Graphics/
│   ├── 08-User_feedback/
│   └── 10-Dynamic_UI/
└── app01/             # Live clock demo (reactive.invalidate_later)
    app02/             # AI-powered diamond explorer (QueryChat + Claude)
    app03/             # Flight data explorer (DuckDB / MSSQL backend)
```

## Standalone Apps

### app01 — Live Clock
A minimal Shiny Express app that renders a greeting updated every second using `reactive.invalidate_later`.

```bash
shiny run app01/app.py
```

### app02 — Diamond Explorer (AI Chat)
Natural-language query interface over the seaborn `diamonds` dataset, powered by [`querychat`](https://github.com/posit-dev/querychat) and the Anthropic Claude API.

Requires an `.env` file with `ANTHROPIC_API_KEY`.

```bash
shiny run app02/app.py
```

### app03 — Flight Data Explorer
Large-scale flight analytics app (1M-row Parquet file) with a natural-language query interface via `querychat`. Includes an optional MSSQL backend and DuckDB integration.

See [`app03/README.md`](app03/README.md) for database setup instructions.

```bash
shiny run app03/flight-app.py   # Parquet / DuckDB backend
shiny run app03/flight-app2.py  # extended version
shiny run app03/app-to-mssql.py # MSSQL backend
```

## Book Chapters

| Chapter | Topic | Key concepts |
|---------|-------|--------------|
| 01 | Your first Shiny app | `App`, `ui`, `server`, Shiny Express |
| 02 | Basic UI | Input/output widgets, layouts |
| 03 | Basic reactivity | `reactive.calc`, `reactive.effect`, shared state |
| 04 | Case study | NEISS injury data, `plotnine`, data frames |
| 06 | Layout, themes & HTML | `page_sidebar`, `navset`, Bootstrap themes |
| 07 | Graphics | Interactive plots, click/hover events |
| 08 | User feedback | Notifications, progress bars, modals, validation |
| 10 | Dynamic UI | `ui.update_*`, `ui.insert_ui`, `renderUI` |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install shiny polars plotnine seaborn querychat python-dotenv duckdb pyodbc
```

Running any app:

```bash
shiny run <path/to/app.py> --reload
```
