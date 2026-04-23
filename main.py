import requests
from twilio.rest import Client

api_key = "fbfd342fd71a2b812373fab83bbf472a"
MY_LANG= 80.9167
MY_LAT = 26.85
URL = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "AC17ed1e656347addc72617b44e02f52de"
auth_token = "91b2b4c572a6e732b1a6f4cd0dbea272"

parameters = {
        "lat": MY_LAT,
        "lon": MY_LANG,
        "appid": api_key,
        "cnt": 4,
}

response = requests.get(url = URL, params = parameters)
response.raise_for_status()
response = response.json()
FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=True 
ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=True

will_rain = False
for hour_data in response["list"]:
   id_code = hour_data["weather"][0]["id"]
   print(type(id_code))
   if id_code <= 800:
      will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, please bring an umbrella☔",
        from_='+12295754252',
        to='+919145480345'
    )
    print(message.status)
