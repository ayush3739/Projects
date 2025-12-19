import requests
import json
import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime as dt
import Stock_handle
import news_data
load_dotenv(".env")




STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid=os.getenv('ACCOUNT_ID')
auth_token=os.getenv('auth_token')
what_from=os.getenv('what_from')
what_to=os.getenv('what_to')

now=dt.date.today()


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#Step -1
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

data=Stock_handle.Stock(STOCK,COMPANY_NAME)

yesterday=data.get_todays_stock()
day_before=data.get_yesterdays_stock()

difference=float(yesterday-day_before)
threshold=round((difference / float(yesterday)) * 100)


if difference>=0:
    up_down="🔺"
else:
    up_down="🔻"
print('handled stock')



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news=news_data.news(COMPANY_NAME)
news_list=news.news_data()
formatted_articles= [f"{STOCK}:{up_down} {threshold}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_list]
print('got news article succesfully')


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
client = Client(account_sid, auth_token)
n=1
for i in formatted_articles:
    msg=client.messages.create(
        from_=f"whatsapp:{what_from}",
        to=f"whatsapp:{what_to}",
        body=i

    )
    print('send message',n)
    n+=1
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

