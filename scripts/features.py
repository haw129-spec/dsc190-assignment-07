import csv
from datetime import date
from pathlib import Path


SOURCE = Path("data/transformed/events.csv")
DESTINATION = Path("data/features/events.csv")
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def add_features():
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with (
        SOURCE.open(encoding="utf-8", newline="") as source,
        DESTINATION.open("w", encoding="utf-8", newline="") as destination,
    ):
        reader = csv.DictReader(source)
        writer = csv.DictWriter(
            destination, fieldnames=[*reader.fieldnames, "duration_minutes", "weekday"]
        )
        writer.writeheader()

        for row in reader:
            row["duration_minutes"] = int(row["duration_seconds"]) / 60
            row["weekday"] = WEEKDAYS[date.fromisoformat(row["date"]).weekday()]
            writer.writerow(row)


if __name__ == "__main__":
    add_features()
