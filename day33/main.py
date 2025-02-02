import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
MY_EMAIL='piyushgilada12@gmail.com'
PASSWORD='kpyd gvnj tvli tkvm'

#If the ISS is close to my current position
# and it is currently dark
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True

def is_night():
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
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise: # dark
        return True


# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connection=smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,to_addrs='piyushgilada007@gmail.com',msg='Subject:ISS IS VISIBLE....\n\nTHE ISS IS ABOVE YOUR SKY'
        )



