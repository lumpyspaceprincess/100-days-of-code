import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIGHTS_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")


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
