import requests

api_key = "617a77dee8831fd3d34e99e564e363b7"
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
        print("Bring an umbrella")
        break

