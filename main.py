import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

api_key = os.environ.get("OMW_API_KEY")
latitude = 47.986130
longitude = 18.163610
excluded = "current,minutely,daily,"
response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={api_key}")

response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+15017122661',
            to='+15558675310'
        )
        print(message.status)
        break



