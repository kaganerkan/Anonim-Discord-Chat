import os
import requests
import json
import time
webhook = ""#pole1 channels webhook
def select_pole():
  pole = input("🚥Select pole🚥\n 1:(💀Random💀), 2:(📋Politics📋)\n📪:")
  if int(pole) == 1 :
    return ""#pole1 channels webhook
  elif int(pole) == 2:
    return "" #pole2 channels webhook
  else:
    return os.environ['webhook']
sendable = "sd"

sending_mod = 2


username = input("🚥Username🚥 \n👤:")
showing_name = username
webhook = select_pole()
while 1 == 1:
  if sending_mod >= 1:  
   sendable = input("\nMessage: \n")
    
   sending_mod = 0
   data = {
      "content" : sendable,
      "username" : showing_name
   }

   result = requests.post(webhook, json = data)
  
   time.sleep(1)
  sending_mod = 2
  
