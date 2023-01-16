import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

FLIGHTS_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")


def date_from():
    date = datetime.date.today() + datetime.timedelta(days=1)
    return date.strftime("%d/%m/%Y")


def date_to():
    date = datetime.date.today() + datetime.timedelta(days=180)
    return date.strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def searching_for_flights(self, city):

        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": FLIGHTS_API_KEY}
        parameters = {
            "term": city,
            "location_types": "city",
        }

        response = requests.get(url=endpoint, headers=header, params=parameters)

        results = response.json()["locations"]
        code = results[0]["code"]

        return code

    def distance_from_london(self, destination):
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        header = {"apikey": FLIGHTS_API_KEY}
        parameters = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": date_from(),
            "date_to": date_to(),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=endpoint, headers=header, params=parameters)
