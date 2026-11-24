import requests


def get_current_weather(latitude: float, longitude: float) -> dict:
    """Fetch current weather data from Open-Meteo."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "Asia/Karachi",
    }
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_current_weather(31.2781, 72.3317)
    current = data.get("current", {})

    print("Temperature (C):", current.get("temperature_2m"))
    print("Humidity (%):", current.get("relative_humidity_2m"))
    print("Wind Speed (km/h):", current.get("wind_speed_10m"))
    print("Weather Code:", current.get("weather_code"))

    import requests

WEATHER_DESCRIPTIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    80: "Slight rain showers",
    95: "Thunderstorm",
}


def describe_weather_code(code: int | None) -> str:
    """Convert an Open-Meteo WMO weather code into a readable label."""
    if code is None:
        return "Unknown"
    return WEATHER_DESCRIPTIONS.get(code, f"Other (code {code})")


def get_current_weather(latitude: float, longitude: float) -> dict:
    """Fetch current weather data from Open-Meteo."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "Asia/Karachi",
    }
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    try:
        data = get_current_weather(31.2781, 72.3317)
        current = data.get("current", {})
        code = current.get("weather_code")

        print("Temperature (C):", current.get("temperature_2m"))
        print("Humidity (%):", current.get("relative_humidity_2m"))
        print("Wind Speed (km/h):", current.get("wind_speed_10m"))
        print("Condition:", describe_weather_code(code))
    except requests.RequestException as exc:
        print("Weather request failed:", exc)