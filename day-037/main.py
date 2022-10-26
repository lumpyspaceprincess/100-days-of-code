import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_API_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
time_programming_today = input("How many minutes programming did you achieve today?")

pixela_parameters = {
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# To create a new user:
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

graph_config = {
    "id": "graph1",
    "unit": "minutes",
    "name": "Programming Graph",
    "type": "int",
    "color": "ajisai",
}

# To create a new graph:
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# what_day = datetime(year=2022, month=10, day=24)
# the_date = what_day.strftime("%Y%m%d")
the_date = datetime.now().strftime("%Y%m%d")

post_config = {
    "date": the_date,
    "quantity": time_programming_today,
}

# To add new information to an existing graph:
# response = requests.post(url=f"{graph_endpoint}/{graph_config['id']}", json=post_config, headers=headers)
# print(response.text)

put_config = {
    "quantity": time_programming_today,
}

# To update an existing entry in an existing graph:
# PUT requests will also create an entry where one doesn't exist, therefore POST seems redundant. Maybe this is only
# for Pixela
response = requests.put(url=f"{graph_endpoint}/{graph_config['id']}/{the_date}",
                        json=put_config, headers=headers)
print(response.text)
print(response.status_code)

# To delete an existing entry in an existing graph:
# response = requests.delete(url=f"{graph_endpoint}/{graph_config['id']}/{the_date}", headers=headers)
# print(response.text)
