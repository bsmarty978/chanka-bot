import json
import random

#NOTE: fetches quotes from locak quote fil
#TO-DO: convert this method with API
with open("quotes.json","r") as f:
    d = f.read()
data = json.loads(d)

#NOTE: this is used get UserConfig data from UserConfig.json 
with open("UserConfig.json","r") as f:
    d = f.read()
config_data = json.loads(d)

help_msg = config_data.get("HELP_MSG")

#NOTE: This is the class where every mods is store you can add you mods as function/method here accordingly...
#pass thr message object to every new mod
#NOTE:DON'T forget to add mod descrpition as comment to help other devs
class replymods:
    # def __init__(self,name="Chanka"):
    #     self.message = name

    def replyQuote(message):
        #sends random quotes
        quote = data[random.randint(0,1840)]["text"]
        message.reply_message(quote)

    def replyHelp(message):
        #sends help menu
        message.reply_message(f"Lavde abhi kam chal rha he apna kam kr nalla gandu!!!!\n\n{help_msg}")
        
    def replyNoods(message):
        #sends random nudes
        message.reply_message("Tharki sala porn dekh bathroom me jake<><>")

    def replyMenu(message):
        #sends menu
        message.reply_message(help_msg)

    def replyModError(message):
        #sends Error msg with menu
        message.reply_message(f"{message.content} bhosad ye mod nahi chal rha dusra try kr!!!\n\n{help_msg}")

