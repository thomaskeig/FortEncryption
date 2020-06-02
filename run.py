import requests
import tweepy
from time import sleep
auth = tweepy.OAuthHandler('PlaceAPIKeyHere', 'PlaceAPISecretHere')
auth.set_access_token('PlaceAccessTokenHere', 'PlaceAccessTokenSecretHere')

#--------#--------#--------#--------#--------#

interval = 10    # <-- Change to the amount of seconds between each check

#--------#--------#--------#--------#--------#

loop = True
count = 1
response = requests.get('https://fnbot.shop/api/aes')
aes = response.json()['mainKey']

while loop == True:
         response = requests.get('https://fnbot.shop/api/aes')
         aes = response.json()['mainKey']
         print("Checking for change in AES key:" ,count)
         count = count + 1
         sleep(interval)

         if aes != aesloop:
                  print("AES Key has changed...")
                  
                  response = requests.get('https://benbotfn.tk/api/v1/status')
                  version = response.json()["currentFortniteVersionNumber"]

                  api = tweepy.API(auth)
                  api.update_status("New AES key detected for #Fortnite v"+version+":\n\n0x"+aesloop+"\n\nGrabbed by FortEncryption by fortbrleaks")

