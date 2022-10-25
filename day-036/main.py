import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

ALPHA_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

change_direction = ""

TWILIO_ID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("PERSONAL_PHONE_NUMBER")

NEWS_API_KEY = os.environ.get("NEWSAPIORG_API_KEY")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_price_change():
    alpha_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday_close_price = data_list[0]["4. close"]
    ereyesterday_close_price = data_list[1]["4. close"]

    change_percentage = ((float(yesterday_close_price) - float(ereyesterday_close_price))
                         / float(ereyesterday_close_price)) * 100
    if change_percentage >= 0 or change_percentage <= -0:
        global change_direction
        if change_percentage > 0:
            change_direction = "🔺"
        else:
            change_direction = "🔻"
        get_stock_news()


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_stock_news():
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en",
        "pageSize": 3,
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    articles = response.json()["articles"]
    headlines = [f"{STOCK}: {change_direction}\n Headline: {article['title']}\n "
                 f"Brief: {article['description']}" for article in articles]

    for item in headlines:
        send_sms_message(item)


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


def send_sms_message(headline):
    client = Client(TWILIO_ID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=headline,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    print(message.status)


get_stock_price_change()
