import datetime as dt
import random
import smtplib


with open("quotes.txt") as file:
    all_quotes = file.readlines()


my_email = "newtonde97@gmail.com"
password = "blwrejwokdapjclz"

today = dt.datetime.now().weekday()
if today == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="newtonnarzary28@gmail.com",
            msg=f"Subject: Motivational Monday.\n\n{random.choice(all_quotes)}"
        )
