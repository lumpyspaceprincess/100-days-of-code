import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_URL = os.environ.get("SHEETY_FLIGHT_CLUB")


def post_to_sheety(name, surname, email):
    new_data = {
        "user":
            {
                "firstName": name,
                "lastName": surname,
                "email": email,
            }
    }
    response = requests.post(url=SHEETY_URL, json=new_data)
    response.raise_for_status()


def get_emails():
    prenom = input("Welcome to Lumpy Flight Club. \n "
                   "We find the best flight deals and email you. \n "
                   "What is your first name?")
    surnom = input("What is your last name?")
    email = input("What is your email?")
    emailconfirm = input("Type your email again.")
    if email == emailconfirm:
        print("You're in the club!")
    else:
        print("emails don't match")
    post_to_sheety(prenom, surnom, email)
