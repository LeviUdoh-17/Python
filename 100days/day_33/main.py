import requests
import datetime as dt

MY_LAT = 6.8679122
MY_LONG = 3.4425298

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("That resource doesn't exist")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access the data")
# response.raise_for_status()

# data = response.json()
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

# ##___RESPONSE CODE___##
# #__1XX: HOLD ON
# #__2XX: HERE YOU GO
# #__3XX: GO AWAY, YOU DON'T HAVE ACCESS
# #__4XX: YOU SCRWED UP SOMEWHERE, NOT FOUND
# #__5XX: I SCREWED UP, SERVER ISSUE

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = (data["results"]["sunrise"].split("T"))[1].split("+")[0].split(":")[0]
sunset = (data["results"]["sunset"].split("T"))[1].split("+")[0].split(":")[0]

timenow = dt.datetime.now()
print(sunrise, sunset, timenow.hour)