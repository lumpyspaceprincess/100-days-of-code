import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
import time
import schedule

load_dotenv()
API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

TWILIO_ID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("PERSONAL_PHONE_NUMBER")

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


def sms_rain_messaging():
    rain_message = ""
    will_rain = False

    for item in weather_data:
        # Will it rain in the next 12 hours?
        # Open Weather Map weather condition codes: https://openweathermap.org/weather-conditions
        if item["weather"][0]["id"] < 700:
            will_rain = True

    if will_rain is True:
        rain_message += "It will rain today. Take an ☂️"

        client = Client(TWILIO_ID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=rain_message,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        print(message.status)


while True:
    schedule.every().day.at("07:00").do(sms_rain_messaging)
    time.sleep(1)
    