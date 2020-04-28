import requests
import tweepy
from time import sleep
auth = tweepy.OAuthHandler('PlaceAPIKeyHere', 'PlaceAPISecretHere')
auth.set_access_token('PlaceAccessTokenHere', 'PlaceAccessTokenSecretHere')


interval = 1    # <-- Change to the amount of seconds between each check


#----------------------------------------------------------------



loop = True
count = 1

#-------------------

response = requests.get('https://fnbot.shop/api/aes')
aes = response.text

#-------------------

while loop == True:
         response = requests.get('https://fnbot.shop/api/aes')
         aesloop = response.text
         print("Checking for change in AES key:" ,count)
         count = count + 1
         sleep(interval)

         if aes != aesloop:
                  print("AES Key has changed...")
                  try:
                           url = "https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version"
                           response = requests.get(url)
                           version = response.json()["version"]

                           api = tweepy.API(auth)
                           api.update_status("New AES key detected for #Fortnite v"+version+":\n\n0x"+aesloop+"\n\nGrabbed by FortEncryption by fortbrleaks")
                           loop = False
                           print("Tweeted aes key change! Please re-run the program.")
                  except:
                           print("ERROR: Tweepy module is not working, aes key has changed but not tweeted! Please re-run the program.") # Error line
                           loop = False

