import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}


def get_question():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]


question_data = get_question()
