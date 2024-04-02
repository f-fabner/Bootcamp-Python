import requests
from datetime import datetime
import os
import base64
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NT_APP_ID")
API_KEY = os.getenv("NT_API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")

auth_string = f"{USERNAME}:{PASSWORD}"
encoded_auth_string = base64.b64encode(auth_string.encode()).decode()

try:
    exercise_text = input("Tell me which exercises you did: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": exercise_text,
        "gender": "<yourgender>",  
        "weight_kg": "<yourweight>", 
        "height_cm": "<yourheight>", 
        "age": "<yourage>"    
 
    }

    response = requests.post(exercise_endpoint, json=parameters, headers=headers)

    if response.status_code == 200:
        result = response.json()

        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%I:%M %p")

        for exercise in result["exercises"]:
            sheet_inputs = {
                "workouttracking": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            auth_header = {"Authorization": f"Basic {encoded_auth_string}"}

            sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=auth_header)

            if sheet_response.status_code == 200:
                print("Data successfully added to the sheet.")
            else:
                print(f"Failed to add data to the sheet: {sheet_response.text}")
    else:
        print(f"Error fetching exercise data: {response.text}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
