## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



import requests
import json
from dotenv import load_dotenv
import datetime as dt
import os
load_dotenv(".env")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"


class Stock:
    def __init__(self,name,company):
        self.stock_api=os.getenv('Alphabvantage_api')
        self.check_stock(name)

    def check_stock(self,name):

        parameter={
            'apikey':self.stock_api,
            'function':'TIME_SERIES_DAILY',
            'symbol':name,
            'outputsize':'compact',
            'datatype':'json',
            'outputsize':'compact'
        }

        response=requests.get(
            url="https://www.alphavantage.co/query",
            params=parameter)

        response.raise_for_status()
        self.stock_data=response.json()

        with open('stock_json.json','w') as file:
            json.dump(self.stock_data,file,indent=4)

        self.dates=list(self.stock_data["Time Series (Daily)"].keys())


    def get_todays_stock(self):
        todays_close=self.stock_data["Time Series (Daily)"][self.dates[0]]["4. close"]
        return float(todays_close)

    def get_yesterdays_stock(self):

        yesterday_close=self.stock_data["Time Series (Daily)"][self.dates[1]]["4. close"]
        return float(yesterday_close)

                