
import requests
from twilio.rest import Client
import os
appid=os.environ["id"]
bring_umbrella=False
lat=39.254749
lng=-76.699951
exclude=["current","minutely","daily"]
dicta={"lat":39.254749,"lon":-76.699951,"exclude":exclude,"appid":appid}
response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=dicta)
response.raise_for_status()
data=response.json()
for i in range(0,12):
    if data["hourly"][i]["weather"][0]["id"] < 700:
        bring_umbrella=True
        break
if bring_umbrella:
    print("Bring Umbrella")



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid =os.environ["owm"]
auth_token =os.environ["aut"]
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Bring Umbrella",
                     from_='+12569146476',
                     to='+16673454884'
                 )

print(message.sid)