import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_FLIGHTS")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheet_data = list

    def get_the_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        stuff = response.json()

        for item in stuff["prices"]:
            self.sheet_data.append(item)

        print(self.sheet_data)


DataManager.get_the_data()