import requests
import json
from dotenv import load_dotenv
import datetime as dt
import os
load_dotenv(".env")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

class news:
    def __init__(self,company_name):
        self.company=company_name
        self.news_data()

    def news_data(self):
        parameter={
            'apikey':os.getenv('news_api'),
            "q": self.company,         # search by company name
            "language": "en",
            "pageSize": 3

        }
        response=requests.get(url=NEWS_ENDPOINT,params=parameter)
        response.raise_for_status()
        articles = response.json()['articles']   # use plural
        return articles