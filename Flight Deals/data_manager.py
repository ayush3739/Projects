import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')
Sheety_users_endpoint=os.getenv('Sheety_users_endpoint')


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        print("API Response:", data)
        print("Available keys:", list(data.keys()) if isinstance(data, dict) else "Response is not a dictionary")
        
        if "prices" in data:
            self.destination_data = data["prices"]
        else:
            if isinstance(data, list):
                self.destination_data = data
            elif isinstance(data, dict) and len(data) == 1:
                key = list(data.keys())[0]
                self.destination_data = data[key]
            else:
                print("Unexpected response structure:", data)
                self.destination_data = []
        
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customers_emails(self):
        response=requests.get(url=Sheety_users_endpoint,auth=self._authorization)
        res=response.json()
        return res["users"]
