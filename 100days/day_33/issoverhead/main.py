import requests
from datetime import datetime
import smtplib

MY_LAT = 6.8679122
MY_LONG = 3.4425298 

def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    #Your position is within +5 or -5 degrees of the ISS position.
    is_over = False
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
is_over = is_iss_above()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# MY_LAT = [round(MY_LAT)-5, round(MY_LAT)+6]
# MY_LONG = [round(MY_LONG)-5, round(MY_LONG)+6]

print(MY_LAT, MY_LONG)

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
#If the ISS is close to my current position
    # and it is currently dark
while time_now.hour >= 3 and is_over == True:
    # BONUS: run the code every 60 seconds.
    time_now = datetime.now()
    if time_now.second == 00:
        my_email = "ukaraobong15@gmail.com"
        my_password = "awydkdsgjgvtjzam"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                # Then send me an email to tell me to look up.
                msg="Subject:ISS Alert\n\nYo! look up.\nThe ISS is above you."
            )