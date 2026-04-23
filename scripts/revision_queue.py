from __future__ import annotations

import csv
from datetime import date
from pathlib import Path


def main() -> None:
    tracker_path = Path(__file__).resolve().parents[1] / "problem_tracker.csv"
    today = date.today()

    if not tracker_path.exists():
        raise FileNotFoundError(f"Tracker not found: {tracker_path}")

    due_rows = []
    with tracker_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            revision_value = row.get("next_revision_date", "").strip()
            if not revision_value:
                continue
            revision_date = date.fromisoformat(revision_value)
            if revision_date <= today and row.get("status", "").strip().lower() == "solved":
                due_rows.append(row)

    if not due_rows:
        print("No revisions due today.")
        return

    print("Problems due for revision:")
    for row in due_rows:
        print(
            f"- {row['problem_id']}: {row['pattern']} / {row['platform']} / "
            f"{row['difficulty']} / next={row['next_revision_date']}"
        )


if __name__ == "__main__":
    main()
