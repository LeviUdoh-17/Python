"""This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
program requirements."""
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/b0577c9bb4d063ac711cbaf45ef33742/copyOfFlightDeals/prices/'

response = DataManager()

sheet_data = response.data
iataCode = sheet_data['prices']
for dictionary in iataCode:
    for key, item in dictionary.items():
        if key == 'iataCode' and item == '':
            flight_data = FlightData(dictionary['city'])
            row_id = dictionary['id']
            iataCode_testing = flight_data.flight_response()
            endpoint = f"{SHEETY_ENDPOINT}{row_id}"
            iata_code = iataCode_testing.json()['locations'][0]['code']
            sheety_params = {'price':
                {
                "iataCode": iata_code
                }
            }
            sheety_response = requests.put(url=endpoint, json=sheety_params)
            print(sheety_response.text)