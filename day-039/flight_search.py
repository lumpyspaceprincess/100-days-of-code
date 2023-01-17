import os
import requests
import datetime
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

FLIGHTS_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_from_now = (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

    def searching_for_flights(self, city):

        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": FLIGHTS_API_KEY}
        parameters = {
            "term": city,
            "location_types": "city",
        }

        response = requests.get(url=endpoint, headers=header, params=parameters)

        results = response.json()["locations"]
        iata_code = results[0]["code"]

        return iata_code

    def cost_from_london(self, destination):
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        header = {"apikey": FLIGHTS_API_KEY}
        parameters = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": self.tomorrow,
            "date_to": self.six_months_from_now,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=endpoint, headers=header, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_iata_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_iata_code=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price}")

        return flight_data
