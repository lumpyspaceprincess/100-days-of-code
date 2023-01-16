import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIGHTS_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")

class FlightData:
    #This class is responsible for structuring the flight data.

    def distance_from_london(self, destination, date_from, date_to):
    endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
    header = {"apikey": FLIGHTS_API_KEY}
    parameters = {
        "fly_from": "LON",
        "fly_to": destination,
        "date_from": date_from,
        "date_to": date_to,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "max_stopovers": 0,
        "curr": "GBP",
    }

    response = requests.get(url=endpoint, headers=header, params=parameters)
