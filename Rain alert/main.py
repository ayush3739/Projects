import requests
import json
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv(".env")

api_key=os.getenv("API_KEY")

account_id=os.getenv("ACCOUNT_ID")
auth_token=os.getenv("auth_token")


parameter={
    
    'appid':api_key,
    'units':'metric',
    'lat':os.getenv('lat'),
    'lon':os.getenv('lon'),
    'cnt':4
}
response=requests.get(
    url='https://api.openweathermap.org/data/2.5/forecast',
    params=parameter
    )
response.raise_for_status()

weather_data=response.json()
with open ("weather.json",'w') as file:

    json.dump(weather_data,file,indent=4)
    
weather_id=[i['weather'][0]['id'] for i in weather_data["list"]]

for i in weather_id:
    if int(i)<700:
        will_rain=True

if will_rain:
    

    client=Client(account_id,auth_token)

    msg=client.messages.create(
        
        from_="whatsapp:+whatsapp no.",
        to="whatsapp:+whatsapp no.",
        body="It's going to 🌧️ today 🌦️. Don't forget your ☂️ and stay 😊!"
        
    )
    






