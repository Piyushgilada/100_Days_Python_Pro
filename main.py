import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

account_sid = ''
auth_token = ''  # hidden in environment variable
# auth_token=os.environ.get('MY_PASS_KEY')
URL='https://api.openweathermap.org/data/2.5/forecast'
api_key=''    # hidden in environment variable
# api_key=os.environ.get('MY_API_KEY')
parameter={
    'lat':33.590355,
    'lon':130.401718,
    'appid':api_key,
    'cnt':4
}
response=requests.get(url=URL,params=parameter)
response.raise_for_status()
weather_data=response.json()

# weather_id=weather_data['list'][1]['weather'][0]['id']
# print(weather_id)
will_rain=False
for hour_data in weather_data['list']:
    condition_code=hour_data['weather'][0]['id']
    if int(condition_code)< 700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's Going to be rain today,Bring an umbrella 🌂",
        from_='+12312396410',
        to='+917620462490'
    )
print(message.status)


