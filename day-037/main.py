import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_API_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")

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

post_config = {
    "date": str(datetime.now()).split(" ")[0].replace("-", ""),
    "quantity": "2",
}

response = requests.post(url=f"{graph_endpoint}/{graph_config['id']}", json=post_config, headers=headers)
print(response.status_code)
