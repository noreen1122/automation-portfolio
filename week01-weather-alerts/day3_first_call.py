import requests

params = {
    "latitude": 31.558,
    "longitude": 74.35071,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max",
    "timezone": "Asia/Karachi",
    "forecast_days": 3,
}

resp = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
print(resp.status_code)
print(resp.url)

data = resp.json()
print(data["daily"]["time"])
print(data["daily"]["temperature_2m_max"])

daily = data["daily"]
rows = []

for i, day in enumerate(daily["time"]):
    rows.append({
        "date": day,
        "max_c": daily["temperature_2m_max"][i],
        "min_c": daily["temperature_2m_min"][i],
        "rain_mm": daily["precipitation_sum"][i],
        "rain_chance": daily["precipitation_probability_max"][i],
    })

print(rows[0])

geo_resp = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Karachi", "count": 1, "country_code": "PK"},
    timeout=10,
)
geo_data = geo_resp.json()
city = geo_data["results"][0]
print(city["name"], city["latitude"], city["longitude"])

bad_resp = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Atlantis", "count": 1, "country_code": "PK"},
    timeout=10,
)
print(bad_resp.json())
bad_city = bad_resp.json()["results"][0]