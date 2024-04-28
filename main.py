import requests
import datetime as dt
import json
APP_ID = "f34647b8"
API_KEY = "a343f7c656ab88847164a225d50a7e1a"

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


natural_exe_response = requests.post(url=natural_excercise_endpoint,json=parameters,headers=headers)
nutrition_facts = natural_exe_response.text


data = json.loads(nutrition_facts)
print(data)

getting_sheet_data = requests.get(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/myWorkouts/workouts")

current_date_and_time = dt.datetime.now()
current_date = current_date_and_time.strftime("%d/%m/%Y")
current_time = current_date_and_time.strftime("%H:%M:%S")
excercise_done = data["exercises"][0]["name"]
excercise_duration = int(data["exercises"][0]["duration_min"])
excercise_calories = int(data["exercises"][0]["nf_calories"])


put_data_parameters = {
    "My Workouts":
        {"Date": current_date,
         "Time": current_time,
         "Exercise": excercise_done,
         "Duration": excercise_duration,
         "Calories": excercise_calories,
         "id": 3}
}


put_data_to_sheet = requests.post(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/myWorkouts/workouts",
                                  json=put_data_parameters,
                                  headers=headers)

print(put_data_to_sheet.content)