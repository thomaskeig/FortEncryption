import requests
import tweepy
from time import sleep
auth = tweepy.OAuthHandler('PlaceAPIKeyHere', 'PlaceAPISecretHere')
auth.set_access_token('PlaceAccessTokenHere', 'PlaceAccessTokenSecretHere')

#--------#--------#--------#--------#--------#

interval = 10    # <-- Change to the amount of seconds between each check (Recommended: 10)

#--------#--------#--------#--------#--------#

count = 1

response = requests.get('https://fortnite-api.com/v2/aes')
aes = response.json()['data']['mainKey']

while 1:
         response = requests.get('https://fortnite-api.com/v2/aes')
         aesloop = response.json()['data']['mainKey']
         print("Checking for change in AES key:" ,count)
         count = count + 1
         sleep(interval)

         if aes != aesloop:
                  print("AES Key has changed...")
                  
                  response = requests.get('https://fortnite-api.com/v2/aes')
                  version = response.json()['data']['build']

                  api = tweepy.API(auth)
                  api.update_status("New AES key detected for #Fortnite:\n\nVersion: "+version+"\n\nAes Key: 0x"+aesloop+"\n\nGrabbed by FortEncryption by fortbrleaks")

