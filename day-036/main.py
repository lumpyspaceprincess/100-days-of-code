import os
import requests
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

ALPHA_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_price_change():
    yesterdays_date = str(date.today() - timedelta(days=1))
    ereyesterdays_date = str(date.today() - timedelta(days=4))

    response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    yesterday_close_price = data[yesterdays_date]["4. close"]
    ereyesterday_close_price = data[ereyesterdays_date]["4. close"]

    change_percentage = ((float(yesterday_close_price) - float(ereyesterday_close_price)) / float(ereyesterday_close_price)) * 100
    if change_percentage >= 5 or change_percentage <= -5:
        print("Get News")


get_stock_price_change()


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
investors are required to file by the SEC The 13F filings show the funds' and investors' 
portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
investors are required to file by the SEC The 13F filings show the funds' and investors' 
portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
