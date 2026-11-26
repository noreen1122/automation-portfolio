import logging
import os
from dotenv import load_dotenv
from http_client import get_json

load_dotenv()

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=log_level,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city_name: str) -> tuple[str, float, float]:
    """Look up a city in Pakistan; raise ValueError if not found."""
    data = get_json(
        GEO_URL,
        params={"name": city_name, "count": 1, "country_code": "PK"},
    )
    results = data.get("results")
    if not results:
        raise ValueError(f"City not found: {city_name}")
    top = results[0]
    return top["name"], top["latitude"], top["longitude"]


if __name__ == "__main__":
    cities = [c.strip() for c in os.getenv("CITIES", "Lahore").split(",") if c.strip()]
    heat_threshold = float(os.getenv("HEAT_THRESHOLD_C", "40"))
    rain_threshold = float(os.getenv("RAIN_CHANCE_THRESHOLD", "60"))

    log.info("Loaded cities=%s heat_threshold=%.1f rain_threshold=%.1f", cities, heat_threshold, rain_threshold)

    for city in cities:
        try:
            name, lat, lon = get_city_coordinates(city)
            forecast = get_json(
                FORECAST_URL,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "daily": "temperature_2m_max,precipitation_probability_max",
                    "timezone": "Asia/Karachi",
                    "forecast_days": 3,
                },
            )
            max_temps = forecast["daily"]["temperature_2m_max"]
            rain_chances = forecast["daily"]["precipitation_probability_max"]
            log.info(
                "%s (%.2f, %.2f) -> max_temps=%s, rain_chances=%s",
                name, lat, lon, max_temps, rain_chances,
            )
        except ValueError as err:
            log.warning("Skipping city: %s", err)
        except Exception as err:
            log.error("Failed processing %s: %s", city, err)
