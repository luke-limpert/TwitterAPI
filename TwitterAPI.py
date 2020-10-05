#Twitter API 
import urllib.request, urllib.parse, urllib.error
import twitter
import ssl

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

print(api.VerifyCredentials())