import requests
from datetime import datetime, timezone

MY_LAT = 10.099346
MY_LONG = 99.830449

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Get sunrise and sunset times
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Get Internation Space Station location

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.utcnow().hour + 7   # ITC is UTC + 7 hours

print(sunrise, sunset, time_now)

#If the ISS is close to my current position
if
# and it is currently dark
if time_now > sunset or time_now < sunrise:
    # Then send me an email to tell me to look up.

# BONUS: run the code every 60 seconds.
