import csv
from datetime import datetime
from pathlib import Path


SOURCE = Path("data/raw/events.csv")
DESTINATION = Path("data/clean/events.csv")
COLUMNS = ("user_id", "timestamp", "event_type", "duration_seconds")
EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}


def parse_timestamp(value):
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%m/%d/%Y %H:%M:%S")


def clean_events():
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with (
        SOURCE.open(encoding="utf-8", newline="") as source,
        DESTINATION.open("w", encoding="utf-8", newline="") as destination,
    ):
        reader = csv.DictReader(source)
        writer = csv.writer(destination)
        writer.writerow(COLUMNS)

        for row in reader:
            user_id, timestamp, event_type, duration = (
                (row.get(column) or "").strip() for column in COLUMNS
            )
            if not user_id or event_type not in EVENT_TYPES:
                continue

            try:
                seconds = int(duration)
                timestamp = parse_timestamp(timestamp)
            except ValueError:
                continue

            if seconds > 0:
                normalized = timestamp.replace(tzinfo=None).isoformat(timespec="seconds")
                writer.writerow((user_id, normalized, event_type, seconds))


if __name__ == "__main__":
    clean_events()
