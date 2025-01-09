import os
import requests
from datetime import date, timedelta
from API_Functions import weight_API, steps_API, calories_API
import psycopg2

#Setting up function arguments
yesterday = date.today() - timedelta(1)

access_key = os.getenv("Fitbit_Annual_Access_Key")

header = {"Authorization": f'Bearer {access_key}',
          "accept-language": "en_US"}


current_weight = weight_API(yesterday, header)
current_steps = steps_API(yesterday, header)
current_calories = calories_API(yesterday, header)

date_string = yesterday.strftime('%Y-%m-%d') 


connection = psycopg2.connect(
    database = "Naim_Fitbit",
    user = "postgres",
    password = os.getenv('Postgre'),
    host = 'localhost',
    port = '5432'
)  

cursur = connection.cursor()

cursur.execute(
    "INSERT INTO health (date, steps, calories, weight) VALUES (%s, %s, %s, %s)", (date_string, current_steps, current_calories, current_weight)
)

connection.commit()
cursur.close()
connection.close()
