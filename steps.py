import os
import requests
from datetime import date, timedelta
import psycopg2


yesterday = date.today() - timedelta(1)

access_key = os.getenv("Fitbit_Annual_Access_Key")

url = "https://api.fitbit.com"

steps_endpoint = f'/1/user/-/activities/steps/date/{yesterday}/1d.json'
header = {"Authorization": f'Bearer {access_key}',
          "accept-language": "en_US"}

response = requests.get(url=url+steps_endpoint, headers=header).json()
print(response['activities-steps'][0]['value'])

calories_endpoint = f'/1/user/-/activities/calories/date/{yesterday}/1d.json'
header = {"Authorization": f'Bearer {access_key}',
          "accept-language": "en_US"}

response = requests.get(url=url+calories_endpoint, headers=header).json()
print(response['activities-calories'][0]['value'])