import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 10.099346
MY_LONG = 99.830449

MY_EMAIL = "definitely_my_email@gmail.com"
MY_PASSWORD = "secure_password"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# ---------------------------- GET SUNRISE AND SUNSET TIMES ------------------------------- #


def is_it_nighttime():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow().hour

    # Test if the sky is dark, and therefore ISS might be visible
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

# ---------------------------- GET INTERNATIONAL SPACE STATION LOCATION ------------------------------- #


def is_the_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_lat = int(iss_response.json()["iss_position"]["latitude"].split(".")[0])
    iss_long = int(iss_response.json()["iss_position"]["longitude"].split(".")[0])

    # If ISS is within 5 degrees latitude of me
    if int(str(MY_LAT).split(".")[0]) in range(iss_lat - 5, iss_lat + 5):
        # If ISS is within 5 degrees longitude of me
        if int(str(MY_LONG).split(".")[0]) in range(iss_long - 5, iss_long + 5):
            return True
        else:
            return False
    else:
        return False


# ---------------------------- SEND EMAIL TO ALERT ISS IS NEAR ------------------------------- #


while True:
    if is_it_nighttime() is True:
        if is_the_iss_overhead() is True:
            # Email user to inform them
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="recipient_address@yahoo.com",
                                    msg="Subject:LOOK UP!\n\n The International Space Station is above you!"
                                    )
    # Test every 60 seconds
    time.sleep(60)
