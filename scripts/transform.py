import csv
from datetime import datetime
from pathlib import Path


SOURCE = Path("data/clean/events.csv")
DESTINATION = Path("data/transformed/events.csv")


def transform_events():
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with (
        SOURCE.open(encoding="utf-8", newline="") as source,
        DESTINATION.open("w", encoding="utf-8", newline="") as destination,
    ):
        reader = csv.DictReader(source)
        writer = csv.DictWriter(destination, fieldnames=[*reader.fieldnames, "date"])
        writer.writeheader()

        for row in reader:
            row["date"] = datetime.fromisoformat(row["timestamp"]).date().isoformat()
            writer.writerow(row)


if __name__ == "__main__":
    transform_events()
