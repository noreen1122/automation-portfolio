# Learning Log

## Week 1 Day 1 (2026-11-22)
Did: Installed Python, VS Code, Git; created automation-portfolio repo and week01-weather-alerts with .venv
Problem:
Fixed by: me
Learned:

## Week 1 Day 2 (2026-11-23)
Did: Completed Day 2 Python exercises (lists, dicts, comprehensions, JSON read/write, PK phone normalization, settings merge, PKR formatting, and assertions) in day2_exercises.py
Problem:
Fixed by:
Learned: Working with lists/dicts, comprehensions, JSON parsing/saving, normalizing Pakistani mobile numbers, and verifying code with assert

## Week 1 Day 3 (2026-11-24)

Did: Built day3_first_call.py for 3-day daily forecasts and row conversion via enumerate, tested Open-Meteo geocoding lookup, and built day3_forecast.py to write a 9-row forecast.csv for Lahore, Karachi, and Islamabad; added *.csv to .gitignore
Problem: Encountered a missing urllib3 dependency in .venv initially and tested city lookup edge cases
Fixed by: Reinstalled requests/dependencies in .venv and verified all 9 forecast rows in forecast.csv
Learned: HTTP requests, query params, status codes, JSON parsing, parallel lists to row dicts with enumerate, geocoding APIs, and writing CSVs with csv.DictWriter

## Week 1 Day 4 (2026-11-26)
Did: Built reusable http_client.py with timeouts, retryable status filtering, and exponential backoff; configured .env and .env.example with python-dotenv; created day4_weather_alerts.py with structured logging and missing-city ValueError handling; tested offline/Wi-Fi-off behavior
Problem: Verified that missing/unknown city names fail lookups and offline networks raise NameResolutionError/ConnectionError
Fixed by: Raised ValueError("City not found: ...") and caught it in the city loop so other cities continue, while retrying transient errors with 2s/4s back-off and logging clear errors
Learned: Timeout discipline, retrying only transient errors (429/5xx/network), exponential back-off, structured logging instead of print, and keeping secrets/settings in .env while committing .env.example

## Week 1 Day 5 (2026-11-26)
Did: Created feature/project-readme branch, wrote week01-weather-alerts/README.md, pushed branch, opened and reviewed a Pull Request on GitHub, merged it into main, and pulled changes locally
Problem: Needed a clean team workflow where main stays stable and documentation is easy for anyone to set up and run
Fixed by: Used feature branch + Pull Request review/merge flow and documented setup, run command, example output, architecture, and lessons learned in README.md
Learned: Feature branch workflow, pull request review, concise imperative commit messages, and writing clear project READMEs

