import smtplib
import pandas
import random
import datetime as dt

MY_EMAIL = "newtonde97@gmail.com"
PASSWORD = "blwrejwokdapjclz"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", f"{birthday_dict[today_tuple]['name']}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_dict[today_tuple]['email'],
            msg=f"Subject: Happy Birthday!\n\n{letter}"
        )



