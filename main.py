import requests
import datetime as dt
import json

APP_ID = "f34647b8"
API_KEY = "a34d6s5656gh23847rt56cha225d50a7e1a"

natural_excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Enter your excersice "),
    "weight_kg": 55,
    "height_cm": 167.64,
    "age": 60
}

natural_exe_response = requests.post(url=natural_excercise_endpoint, json=parameters, headers=headers)
nutrition_facts = natural_exe_response.text

data = json.loads(nutrition_facts)

getting_sheet_data = requests.get(url="https://api.sheety.co/ce56a24dd896549001e616b7fe7ac4c/myWorkouts/sheet1")

current_date_and_time = dt.datetime.now()
current_date = current_date_and_time.strftime("%d/%m/%Y")
current_time = current_date_and_time.strftime("%H:%M:%S")
excercise_done = data["exercises"][0]["name"]
excercise_duration = int(data["exercises"][0]["duration_min"])
excercise_calories = int(data["exercises"][0]["nf_calories"])

put_data_parameters = {
    "sheet1": {
        "Date": current_date,
        "Time": current_time,
        "Exercise": excercise_done,
        "Duration": excercise_duration,
        "Calories": excercise_calories,
        # "Id": "4"
    }
}

user_cred = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

json_data = json.dumps(put_data_parameters)
put_data_to_sheet = requests.post(url="https://api.sheety.co/ce03a4rty6107449001e616b7fe7ac4c/myWorkouts/sheet1",
                                  json=put_data_parameters,
                                  # auth=("nirav6656", "N.k.6656")
                                  headers={"Authorization": "Basic bmlyYXY245rfgOk4uay42NjU2"}
                                  )

print(put_data_to_sheet.content)
