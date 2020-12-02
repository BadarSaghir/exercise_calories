import requests
import datetime

API_END_POiNTS_SHEETY = 'https://api.sheety.co/12c97efe70fa8b60f1607e1b2846422e/exercise/workouts'

API_KEY = "3629ea4681570fb302c63c899a4a06f0"
SHEET_NAME = 'exercise'
API_END_POiNTS = f"https://trackapi.nutritionix.com/v2/natural/{SHEET_NAME}"
API_ID = "9b28d2cb"

query = input("Hellow, How much exercises your did today: ")
params = {
    "query": query,
    # query:"ran 3 miles",
    # "gender": "female",
    # "weight_kg": 72.5,
    # "height_cm": 167.64,
    # "age": 30
}
HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

response = requests.post(API_END_POiNTS, data=params, headers=HEADER)
json_data = (response.json()['exercises'])
print(json_data)
information = [{SHEET_NAME:{
    'Date': datetime.datetime.now().strftime(f"%d/%m/%Y"),
    'Time': datetime.datetime.now().strftime("%H:%M:%S"),
    'Exercise': exercise['user_input'],
    'Duration': exercise['duration_min'],
    'Calories': exercise['nf_calories']
}
}
    for exercise in json_data
]
print(information)
for post in information:
    response = requests.post(API_END_POiNTS_SHEETY, params=post)
