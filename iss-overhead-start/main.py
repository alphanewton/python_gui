import cmath
import math
import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 28.704060 # Your latitude
MY_LONG = 77.102493 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = int(time_now.hour)

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if abs(iss_longitude - MY_LONG) < 5 and abs(iss_latitude - MY_LAT) < 5:
        if sunrise > hour_now > sunset:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login("newtonde97@gmail.com", "blwrejwokdapjclz")
                connection.sendmail(
                    to_addrs="newtonnarzary28@gmail.com",
                    from_addr="newtonde97@gmail.com",
                    msg="Subject:Look up☝️ \n\nThe International Space Station could be visible in the sky!"
                )


