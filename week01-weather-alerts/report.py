"""Alert rules and CSV output for weather forecasts."""

import csv
from pathlib import Path

CSV_COLUMNS = ["city", "date", "max_c", "min_c", "rain_mm", "rain_chance"]


def find_alerts(
    city: str,
    rows: list[dict],
    heat_c: float = 40.0,
    rain_chance: float = 60.0,
) -> list[str]:
    """Return alert strings for days meeting heat or rain thresholds."""
    alerts: list[str] = []
    for row in rows:
        date_str = row["date"]
        max_c = row["max_c"]
        rain_mm = row["rain_mm"]
        prob = row["rain_chance"]

        if max_c is not None and max_c >= heat_c:
            alerts.append(f"HEAT {city} {date_str}: {max_c} °C")

        if prob is not None and prob >= rain_chance:
            alerts.append(f"RAIN {city} {date_str}: {prob}% chance, {rain_mm} mm")

    return alerts


def write_csv(path: str | Path, rows: list[dict]) -> Path:
    """Write forecast rows to a CSV file with standard columns."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    return out_path
