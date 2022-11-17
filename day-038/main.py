import os

import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
APP_ID = os.environ.get("NUTRITIONIX_ID")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

nutritionix_postconfig = {
    # "query": input("Tell me which exercises you did: "),
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30,
}

response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_postconfig)
exercises = response.json()["exercises"][0]

the_date = datetime.now().strftime("%Y%m%d")
the_time = datetime.now().strftime("%H:%M:%S")

sheety_parameters = dict()

for item in exercises:
    sheety_parameters = {
        "workout": {
            "date": the_date,
            "time": the_time,
            "exercise": exercises["name"],
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"],
        }
    }


response = requests.post(url=sheety_endpoint, json=sheety_parameters)
response.raise_for_status()
