# Reproducible Data Pipelines

This project cleans the course event log, derives event-level features, and
plots the distribution of event durations in a Marimo notebook.

## Run from a fresh clone

Install [uv](https://docs.astral.sh/uv/) and run these commands from the
repository root.

```sh
uv sync --locked
uv run dvc repro
uv run marimo run notebooks/report.py
```

## Pipeline

| DVC stage | What it does | Output |
| --- | --- | --- |
| `clean` | Drops incomplete records, invalid event types, unparseable timestamps, and non-positive durations. Normalizes timestamps to ISO 8601 at second precision. | `data/clean/events.csv` |
| `transform` | Adds the event date in `YYYY-MM-DD` format. | `data/transformed/events.csv` |
| `features` | Divides duration in seconds by 60 and adds the full English weekday name. | `data/features/events.csv` |

The accepted event types are `click`, `login`, `purchase`, `scroll`, and
`view`. The original [course dataset](https://github.com/dsc-courses/dsc190-tools-2026-fa/blob/main/assignments/07-reproducibility/data/raw/events.csv)
is tracked in Git at `data/raw/events.csv`. DVC regenerates the three derived
CSV files using its local cache.
