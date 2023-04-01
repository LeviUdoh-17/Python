import requests

response = requests.get(url="https://opentdb.com/api.php?amount=20&category=18&type=boolean")
question_data = response.json()["results"]