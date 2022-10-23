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
    # Will it rain in the next 12 hours?
    # Open Weather Map weather condition codes: https://openweathermap.org/weather-conditions
    rain = ""
    if item["weather"][0]["id"] < 700:
        rain = "It is due to rain at this time."

    time = item["dt_txt"].split(" ")[1]
    temperature = item["main"]["feels_like"]  # "Feels like" is the only valid measurement of temperature
    print(f"At {time} the temperature will be {temperature}°C. {rain}")
