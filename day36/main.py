import json
import math
from twilio.rest import Client
import requests

COMPANY_NAME = "Tesla Inc"
STOCK_NAME='TSLA'
STOCK_ENDPOINT='https://www.alphavantage.co/query'
NEWS_ENDPOINT='https://newsapi.org/v2/everything'
STOCK_API_KEY='6RSBPH15WDKYGM296RSBPH15WDKYGM29'
NEWS_API_KEY='1adcfd3aaea248fda128cb8aab97084d'
ACC_SID='AC9332e77db5927544d0728b56cb0f7439'
AUTH_TOKEN='9db3270f638b3008745d010c522ee984'

parameter={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':STOCK_API_KEY,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


response=requests.get(url=STOCK_ENDPOINT,params=parameter)
response.raise_for_status()
yesterday_data=response.json()['Time Series (Daily)']['2025-01-31']
day_before_yesterday_data=response.json()['Time Series (Daily)']['2025-01-30']

yesterday_list=[value for (key,value) in yesterday_data.items()]
day_before_yesterday_list=[value for (key,value) in day_before_yesterday_data.items()]

yesterday_close=yesterday_list[3]
day_before_yesterday_close=day_before_yesterday_list[3]
print(yesterday_close)
print(day_before_yesterday_close)

difference=abs(float(day_before_yesterday_close)-float(yesterday_close))
print(difference)

difference_percent=(difference/float(yesterday_close))*100
if difference_percent > 1:
    news_parameter={
        'apiKey':NEWS_API_KEY,
        'qInTitle':COMPANY_NAME,
    }
    news_response=requests.get(url=NEWS_ENDPOINT,params=news_parameter)
    articles=news_response.json()['articles']
    articles=articles[0:3]
    news_list=[f"Headline :{news['title']}. \nContent : {news['content']}" for news in articles]
    print(news_list)
    client = Client(ACC_SID,AUTH_TOKEN)
    for articles in news_list:
        message = client.messages.create(
          from_='+12312396410',
          to='+917620462490',
            body=articles
        )


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

