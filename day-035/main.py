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
    "cnt": 12,   # Only ask for this number of responses
}

response = requests.get(url=OPEN_WEATHER_MAP_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

for item in weather_data:
    time = item["dt_txt"].split(" ")[1]
    temperature = item["main"]["feels_like"]
    print(f"At {time} the temperature will be {temperature}°C")
