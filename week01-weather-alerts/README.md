# City Weather & Alert Script

Fetches the 3-day forecast for Pakistani cities from the free Open-Meteo API,
saves a CSV report and prints alerts for heat (>= 40 °C) and rain (>= 60% chance).

## Setup

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env

## Run

python main.py --cities Lahore Karachi Islamabad

## Example output

2026-11-26 10:50:42,494 INFO __main__: Lahore (31.56, 74.35) -> max_temps=[23.9, 23.9, 23.7], rain_chances=[0, 0, 0]
2026-11-26 10:50:44,478 INFO __main__: Karachi (24.86, 67.01) -> max_temps=[28.2, 27.7, 31.2], rain_chances=[0, 0, 0]
2026-11-26 10:50:46,531 INFO __main__: Islamabad (33.72, 73.04) -> max_temps=[21.3, 20.5, 21.0], rain_chances=[0, 0, 0]

## How it works

- weather.py – talks to the Open-Meteo geocoding and forecast APIs
- http_client.py – timeouts, retries with back-off, logging
- report.py – alert rules and CSV writing
- main.py – command-line interface

## What I learned

- How to separate configuration/secrets into `.env` while keeping `.env.example` and ignoring `.env` in Git
- How to handle transient network/server errors with timeouts, retries, and exponential back-off (`2s`, `4s`, `8s`)
- How to use structured `logging` and handle missing/invalid inputs cleanly without crashing the loop
## Example output

2026-11-26 12:33:44,967 INFO weather_alerts: Lahore: 3 days fetched
2026-11-26 12:33:46,815 INFO weather_alerts: Karachi: 3 days fetched
2026-11-26 12:33:49,022 INFO weather_alerts: Islamabad: 3 days fetched
2026-11-26 12:33:50,742 INFO weather_alerts: Atlantis: 3 days fetched
Saved 12 rows to weather_20261126.csv
RAIN Atlantis 2026-11-28: 65% chance, 0.9 mm
