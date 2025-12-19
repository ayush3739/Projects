import requests
import datetime as dt


time_now=dt.datetime.now()


parameter={
    'lat':'Your latitude',
    'lng':'Your longitude',
    'formatted':0,
}



response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)

response.raise_for_status()

data=response.json()

sunrise=data["results"]["sunrise"].split('T')[1].split(':')[0]

sunset=data["results"]["sunset"].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

print(time_now.hour)
