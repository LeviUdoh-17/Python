import requests
from datetime import datetime
from os import environ as env

APP_ID = "71d4195b"
# API_KEY = "ba6af71de62289ce7bcf5ecac95291c1"
API_KEY = env.get('API_KEY')
print(API_KEY)
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/b0577c9bb4d063ac711cbaf45ef33742/myWorkouts/workouts"
SHEETY_TOKEN = "Bearer workout_levi"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
nutritionix_params = {
    "query": f"{input('Tell me which exercise you did: ')}",
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 175,
    "age": 19
}


reaponse = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=headers)
results = reaponse.json()


date = datetime.now()
sheety_header = {
    "Authorization": SHEETY_TOKEN
}
sheety_params = {
    "workouts":{
        "date": f"{date.strftime('%d/%m/%Y')}",
        "time": f"{date.strftime('%X')}",
        "exercise": (results['exercises'][0]['user_input']).title(),
        "duration": results['exercises'][0]['duration_min'],
        "calories": results['exercises'][0]['nf_calories'],
    }
}
response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers= sheety_header)
print(response.text)