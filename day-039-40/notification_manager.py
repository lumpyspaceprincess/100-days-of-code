import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

TWILIO_ID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("PERSONAL_PHONE_NUMBER")

MY_EMAIL = os.environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_ID, TWILIO_AUTH_TOKEN)

    def send_sms_message(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(message.status)

    def send_emails(self, message_body):
        # ---------------------------- SEND EMAIL FROM COMMAND LINE ------------------------------- #

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="recipient_address@yahoo.com",
                                msg="Subject:Hello\n\n This is the body of my email"
                                )
        