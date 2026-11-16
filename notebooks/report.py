import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import csv

    import marimo as mo
    import matplotlib.pyplot as plt

    return csv, mo, plt


@app.cell
def _(csv, mo):
    features_path = mo.notebook_dir().parent / "data" / "features" / "events.csv"
    mo.stop(
        not features_path.is_file(),
        mo.md("Run `uv run dvc repro` from the repository to generate the features CSV."),
    )
    with features_path.open(encoding="utf-8", newline="") as features_file:
        durations = [float(row["duration_minutes"]) for row in csv.DictReader(features_file)]
    return (durations,)


@app.cell
def _(durations, plt):
    figure, axes = plt.subplots(figsize=(8, 4.5), layout="constrained")
    axes.hist(durations, bins=25, color="#236C78", edgecolor="white")
    axes.set(
        title="Event duration distribution",
        xlabel="Duration (minutes)",
        ylabel="Number of events",
    )
    figure
    return


if __name__ == "__main__":
    app.run()
