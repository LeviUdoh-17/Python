from datetime import datetime
import requests

USERNAME = "leviudoh"
TOKEN = "ulahfgiefhurpdj2nf"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_param={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"
graph_param={
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()
add_pixel_param={
    "date": today.strftime("%Y%m%d"),
    "quantity": f"{input('How many hours did you program today? ')}"
}
pixel_update_param = {
    "quantity": "5.0"
}
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.post(url=add_pixel_endpoint, json=add_pixel_param, headers=headers)
# response = requests.put(url=update_pixel_endpoint, json=pixel_update_param, headers=headers)
# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
print(response.text)
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)
