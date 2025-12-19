import requests
import os
from dotenv import load_dotenv
from datetime import datetime 


load_dotenv(".env")

API_KEY=os.getenv("API_KEY")
APP_ID=os.getenv("APP_ID")
AGE=19
WEIGHT=50
Height=165.1
now = datetime.now()
date = now.strftime("%d/%m/%Y")

time=now.strftime("%H:%M:%S")




query=input("Tell me which exercises you did : ")

api_endpoints="https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoints="https://api.sheety.co/29a0dda7e1931290f65e6e6db683c34a/myWorkouts/workouts"


sheety_headers={
"Authorization": f"Basic {os.getenv("pass")}"
}

headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    
}
parameters={
    "query":query,
    "gender":"male",
    "height_cm":Height,
    "weight_kg":WEIGHT,
    "age":AGE
}


response=requests.post(url=api_endpoints,headers=headers,json=parameters)
result=response.json()
print(response.text)
sheety=requests.get(url=sheety_endpoints,headers=sheety_headers)
print(sheety.json())

for ex in result["exercises"]:
        
    body = {
        "workout": {
            "date":date,
            "time":time,
            "exercise":ex["name"].title(),
            "duration":ex["duration_min"],
            "calories":ex["nf_calories"]
        }
    }
    sheety=requests.post(url=sheety_endpoints,headers=sheety_headers,json=body)
    print(sheety.status_code, sheety.text)

sheety=requests.get(url=sheety_endpoints,headers=sheety_headers)
print(sheety.json())



