from datetime import datetime
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_APIKEY = "yIC9ls2wfJuWcwUO1cVZvYuNWVfojgJA"


class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, city_name):
        self.city_name = city_name
        self.new_method()

    def new_method(self):
        self.params = {
                "term": f"{self.city_name}",
                "location_types": "city"
            }
        self.headers = {
            'apikey': TEQUILA_APIKEY
        }

    def flight_response(self):
        tequila_response = requests.get(url=TEQUILA_ENDPOINT, params=self.params, headers=self.headers)
        return tequila_response
