import requests
from datetime import datetime
import os
# app_id=os.environ.get("APP_ID")
# api_key=os.environ.get("API_KEY")


GENDER='male'
HEIGHT_CM=180
WEIGHT_KG=59
AGE=21

APP_ID='e801c5b7'
API_KEY='4c629e890841fe26beb8bd72830537ac'

headers={
   'x-app-id':APP_ID,
    'x-app-key':API_KEY
}
exercise_text=input('Tell me,which exercise you done today ? ')

END_POINT='https://trackapi.nutritionix.com/v2/natural/exercise'
parameters={
    'query':exercise_text,
    'gender':GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':AGE
}

response=requests.post(url=END_POINT,json=parameters,headers=headers)
result=response.json()
print(result)

GOOGLESHEET_END_POINT = "https://api.sheety.co/25b8076140b67a1be72552b9972bb7a6/myWorkouts/workouts"


today_date=datetime.now().strftime("%d/%m/%Y")
workout_time=datetime.now().strftime('%X')
for exercise in result['exercises']:
    sheet_parameter = {
        "workout": {
            "date": today_date,
            'time': workout_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheet_response = requests.post(GOOGLESHEET_END_POINT, json=sheet_parameter,headers={"Content - Type": "json"})
    print(sheet_response.text)
    if sheet_response.status_code == 200:
        print("Workout logged successfully:", sheet_response.json())
    else:
        print("Error logging workout:", sheet_response.text)

