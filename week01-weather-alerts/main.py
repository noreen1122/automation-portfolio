"""City Weather & Alert Script – Week 1 project."""

import argparse
from datetime import datetime
import logging
import os

from dotenv import load_dotenv

from report import find_alerts, write_csv
from weather import find_city, get_forecast

log = logging.getLogger("weather_alerts")


def parse_args() -> argparse.Namespace:
    """Parse command-line options for the weather alert script."""
    parser = argparse.ArgumentParser(
        description="Weather report and alerts for Pakistani cities"
    )
    parser.add_argument(
        "--cities",
        nargs="+",
        default=None,
        help="City names (e.g. Lahore Karachi Islamabad)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=3,
        help="Number of forecast days (default: 3)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output CSV path (default: weather_YYYYMMDD.csv)",
    )
    return parser.parse_args()


def get_cities_from_env() -> list[str]:
    """Read comma-separated CITIES from environment variables."""
    raw = os.getenv("CITIES", "Lahore,Karachi,Islamabad")
    return [c.strip() for c in raw.split(",") if c.strip()]


def main() -> None:
    """Run weather fetch, CSV export, and alert reporting."""
    load_dotenv()

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    args = parse_args()

    cities = args.cities if args.cities else get_cities_from_env()
    heat_threshold = float(os.getenv("HEAT_THRESHOLD_C", "40"))
    rain_threshold = float(os.getenv("RAIN_CHANCE_THRESHOLD", "60"))

    all_rows: list[dict] = []
    all_alerts: list[str] = []

    for city_query in cities:
        try:
            resolved_name, lat, lon = find_city(city_query)
            rows = get_forecast(lat, lon, days=args.days)

            for row in rows:
                row["city"] = resolved_name

            all_rows.extend(rows)
            city_alerts = find_alerts(
                resolved_name,
                rows,
                heat_c=heat_threshold,
                rain_chance=rain_threshold,
            )
            all_alerts.extend(city_alerts)
            log.info("%s: %d days fetched", resolved_name, len(rows))
        except ValueError as err:
            log.error("Skipping %s: %s", city_query, err)
        except Exception as err:
            log.error("Failed %s: %s", city_query, err)

    default_filename = f"weather_{datetime.now().strftime('%Y%m%d')}.csv"
    out_path = write_csv(args.out if args.out else default_filename, all_rows)
    print(f"Saved {len(all_rows)} rows to {out_path}")

    if all_alerts:
        for alert in all_alerts:
            print(alert)
    else:
        print("No alerts")


if __name__ == "__main__":
    main()
