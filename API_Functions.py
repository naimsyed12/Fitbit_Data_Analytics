import requests


#API request for weight
def weight_API(date, header):
    weight_endpoint =  f'https://api.fitbit.com/1/user/-/body/log/weight/date/{date}.json'
    response = requests.get(url=weight_endpoint, headers=header)
    if response.status_code == 200:
        json = response.json()
        return json['weight'][0]['weight']
    else: 
        return response.status_code

#API request for steps 
def steps_API(date, header):
    steps_endpoint = f'https://api.fitbit.com/1/user/-/activities/steps/date/{date}/1d.json'
    response = requests.get(url=steps_endpoint, headers=header)
    if response.status_code == 200:
        json = response.json()
        return json['activities-steps'][0]['value'] 
    else:
        return response.status_code
    

#API request for calories
def calories_API(date, header):
    calories_endpoint = f'https://api.fitbit.com/1/user/-/activities/calories/date/{date}/1d.json'
    response = requests.get(url=calories_endpoint, headers=header)
    if response.status_code == 200:
        json = response.json()
        return json['activities-calories'][0]['value']
    else:
        return response.status_code
