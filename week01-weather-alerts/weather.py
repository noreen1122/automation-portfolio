"""Talks to Open-Meteo geocoding and forecast APIs."""

from http_client import get_json

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def find_city(name: str) -> tuple[str, float, float]:
    """Return (resolved_name, latitude, longitude) for a Pakistani city."""
    data = get_json(
        GEO_URL,
        params={"name": name, "count": 1, "country_code": "PK"},
    )
    results = data.get("results")
    if not results:
        raise ValueError(f"City not found: {name}")
    top = results[0]
    return top["name"], top["latitude"], top["longitude"]


def get_forecast(lat: float, lon: float, days: int = 3) -> list[dict]:
    """Fetch daily forecast and return rows matching CSV columns."""
    data = get_json(
        FORECAST_URL,
        params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max",
            "timezone": "Asia/Karachi",
            "forecast_days": days,
        },
    )
    daily = data["daily"]
    rows = []
    for i, date_str in enumerate(daily["time"]):
        rows.append(
            {
                "date": date_str,
                "max_c": daily["temperature_2m_max"][i],
                "min_c": daily["temperature_2m_min"][i],
                "rain_mm": daily["precipitation_sum"][i],
                "rain_chance": daily["precipitation_probability_max"][i],
            }
        )
    return rows
