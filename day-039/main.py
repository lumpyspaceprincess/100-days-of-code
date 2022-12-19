import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWILIO_ID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("PERSONAL_PHONE_NUMBER")

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.


# TODO 1:
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
# International Air Transport Association (IATA) codes for each city. Most of the cities in
# the sheet include multiple airports, you want the city code (not the airport code see here).


# TODO 2:
# Use the Flight Search API to check for the cheapest
# flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# TODO 3:
# If the price is lower than the lowest price listed in the Google Sheet then send
# an SMS to your own number with the Twilio API.


def send_sms_message(message_body):
    client = Client(TWILIO_ID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    print(message.status)


# send_sms_message(f"Low price alert! Only {price} to fly from {origin} to {destination}, from
# {date_from} to {date_to}.")

# TODO 4:
# The SMS should include the departure airport IATA code, destination airport IATA code,
# departure city, destination city, flight price and flight dates.
