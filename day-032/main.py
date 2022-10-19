import smtplib
import datetime as dt
import random

my_email = "definitely_my_email@gmail.com"
my_password = "secure_password"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="recipient_address@yahoo.com",
#                         msg="Subject:Hello\n\n This is the body of my email"
#                         )

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    quotes_list = []
    with open("quotes.txt", "r") as file:
        for line in file:
            quotes_list.append(line)
        quote = random.choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="recipient_address@yahoo.com",
                                msg=f"Subject:Your weekly inspirational quote!\n\n {quote}"
                                )
