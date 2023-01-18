import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_FLIGHTS")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_the_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data
                )
            print(response.text)
