import csv
import requests

CITIES = ["Lahore", "Karachi", "Islamabad"]
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city_name: str) -> tuple[str, float, float]:
    """Look up a city in Pakistan and return (name, latitude, longitude)."""
    resp = requests.get(
        GEO_URL,
        params={"name": city_name, "count": 1, "country_code": "PK"},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    top = data["results"][0]
    return top["name"], top["latitude"], top["longitude"]


def get_three_day_rows(city_label: str, lat: float, lon: float) -> list[dict]:
    """Fetch 3-day daily forecast and convert parallel lists into row dicts."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max",
        "timezone": "Asia/Karachi",
        "forecast_days": 3,
    }
    resp = requests.get(FORECAST_URL, params=params, timeout=10)
    resp.raise_for_status()
    daily = resp.json()["daily"]

    rows = []
    for i, day in enumerate(daily["time"]):
        rows.append({
            "city": city_label,
            "date": day,
            "max_c": daily["temperature_2m_max"][i],
            "min_c": daily["temperature_2m_min"][i],
            "rain_mm": daily["precipitation_sum"][i],
            "rain_chance": daily["precipitation_probability_max"][i],
        })
    return rows


def write_forecast_csv(filename: str, all_rows: list[dict]) -> None:
    """Write list of forecast row dictionaries to a CSV file."""
    fieldnames = ["city", "date", "max_c", "min_c", "rain_mm", "rain_chance"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)


if __name__ == "__main__":
    all_rows = []
    for city in CITIES:
        name, lat, lon = get_city_coordinates(city)
        city_rows = get_three_day_rows(name, lat, lon)
        all_rows.extend(city_rows)

    write_forecast_csv("forecast.csv", all_rows)
    print(f"Saved {len(all_rows)} rows to forecast.csv")