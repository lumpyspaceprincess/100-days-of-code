import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "definitely_my_email@gmail.com"
MY_PASSWORD = "secure_password"

# ---------------------------- SEND EMAIL FROM COMMAND LINE ------------------------------- #
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL,
#                         to_addrs="recipient_address@yahoo.com",
#                         msg="Subject:Hello\n\n This is the body of my email"
#                         )

# ---------------------------- SEND INSPIRATIONAL QUOTE AS EMAIL ------------------------------- #
#
# now = dt.datetime.now()
# weekday = now.weekday()
#
# if weekday == 2:
#     quotes_list = []
#     with open("quotes.txt", "r") as file:
#         for line in file:
#             quotes_list.append(line)
#         quote = random.choice(quotes_list).split(" - ")
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL,
#                             to_addrs="recipient_address@yahoo.com",
#                             msg=f"Subject:Your weekly inspirational quote!\n\n"
#                                 f"{quote[0]}\n\n"
#                                 f" - {quote[1]}"
#                             )

# ---------------------------- EXTRA HARD STARTING PROJECT ------------------------------- #

# 1. Update the birthdays.csv
# Done.

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
day_today = now.day
month_today = now.month

file = pandas.read_csv("birthdays.csv")
birthdays = pandas.DataFrame.to_dict(file, orient="records")
print(birthdays)

for person in birthdays:
    if person["month"] == month_today:
        if person["day"] == day_today:

            # 3. If step 2 is true,
            # pick a random letter from letter templates and replace the [NAME] with
            # the person's actual name from birthdays.csv
            with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as data:
                email_contents = data.read()
                email_contents = email_contents.replace("[NAME]", person["name"])

            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=person["email"],
                                    msg=f"Subject:Happy Birthday!\n\n"
                                        f"{email_contents}"
                                    )
