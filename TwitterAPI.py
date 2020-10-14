#Twitter API 
import urllib.request, urllib.parse, urllib.error
import twitter
import ssl
from twurl import augment
import json


APIinfo = open("TwitterAPIKey.txt", "r")
Authenticator = APIinfo.readlines()
CK = Authenticator[0]
CK = CK[:-1]
CS = Authenticator[1]
CS = CS[:-1]
ATK = Authenticator[2]
ATK = ATK[:-1]
ATS = Authenticator[3]
ATS = ATS[:-1]

api = twitter.Api(consumer_key=CK,
consumer_secret=CS,
access_token_key=ATK,
access_token_secret=ATS)

#static start for URL
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'elonmusk'})

#print(api.VerifyCredentials())

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#establish connection
connection = urllib.request.urlopen(url, context=ctx)
data= connection.read().decode()
headers = dict(connection.getheaders())
# print headers
print('Remaining', headers['x-rate-limit-remaining'])

users = api.GetUserTimeline(screen_name = 'elonmusk')
js = json.loads(data)
print(json.dumps(js, indent=4))
with open("freeplay_data.json", "w") as write_file:
	json.dump(json.dumps(js, indent=4), write_file)

for user in users:
	print(user.text)






#Check rate limit
