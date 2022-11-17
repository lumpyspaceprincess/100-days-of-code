import os

import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_ID")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_AUTH = os.environ.get("SHEETY_AUTHENTICATION")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

sheety_headers = {
    "authentication": f"Bearer {SHEETY_AUTH}",
}

nutritionix_postconfig = {
    # "query": input("Tell me which exercises you did: "),
    "query": "ran 3 miles and swam 3km",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_postconfig)
exercises = response.json()["exercises"]

the_date = datetime.now().strftime("%Y-%m-%d")
the_time = datetime.now().strftime("%H:%M:%S")

sheety_parameters = dict()

for item in exercises:
    sheety_parameters = {
        "workout": {
            "date": the_date,
            "time": the_time,
            "exercise": item["name"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    response.raise_for_status()
