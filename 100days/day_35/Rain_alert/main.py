import requests
from twilio.rest import Client


OPW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LATITUDE = 6.516525416635757
LONGITUDE = 3.3978529
TESTING_LATITUDE = 39.516667
TESTING_LONGITUDE = -149.950000

API_KEY = "00eae5731061f7acb1f85a59e67dc96f"
account_sid = "AC13be41687f58356816eb0dadbf9378e7"
auth_token = "3129e32904c27aacf5c5dd76be120b7a"

weather_params = {
    "lat": TESTING_LATITUDE,
    "lon": TESTING_LONGITUDE,
    "appid": API_KEY
}

data = requests.get(OPW_ENDPOINT, params=weather_params)
weather_data = data.json()
weather_id = weather_data['list'][0]['weather'][0]['id']
if weather_id > 700:
    print('Its not raining')
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Today is a rainy day, bring an umbrella☔",
                        from_='+15856481486',
                        to='+2347015140269'
                 )
    print(message.status)                