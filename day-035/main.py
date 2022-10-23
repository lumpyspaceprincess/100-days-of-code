import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("open_weather_map_api_key")
OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 10.099346
MY_LONG = 99.830449


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,   # Only ask for this number of responses
}

response = requests.get(url=OPEN_WEATHER_MAP_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

for item in weather_data:
    time = item["dt_txt"].split(" ")[1]
    temperature = item["main"]["feels_like"]
    print(f"At {time} the temperature will be {temperature}°C")

    # Will it rain in the next 12 hours?
    if "rain" in item["weather"][0]["description"]:
        print(f"It is due to rain at {time}")
