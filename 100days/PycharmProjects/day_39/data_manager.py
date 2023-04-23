import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b0577c9bb4d063ac711cbaf45ef33742/copyOfFlightDeals/prices"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.response = requests.get(url=SHEETY_ENDPOINT)
        self.data = self.response.json()