import requests
APP_ID = "f34647b8"
API_KEY = "a343f7c656ab88847164a225d50a7e1a"

natural_excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("tell me what you did today ? "),
    "weight_kg": 55,
    "height_cm": 167.64,
    "age": 60
}


natural_exe_response = requests.post(url=natural_excercise_endpoint,json=parameters,headers=headers)
# print(natural_exe_response.text)

getting_sheet_data = requests.get(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/myWorkouts/workouts")
print(getting_sheet_data.json())