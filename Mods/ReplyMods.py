import json
import random
import requests
import time

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
prefix = config_data.get("PREFIX")

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
        '''Sends help menu.'''
        message.reply_message(f"Lavde abhi kam chal rha he apna kam kr nalla gandu!!!!\n\n{help_msg}")
        
    def replyNoods(message):
        '''Sends random nudes.'''
        message.reply_message("Tharki sala porn dekh bathroom me jake<><>")

    def replyMenu(message):
        '''Sends menu.'''
        message.reply_message(help_msg)

    def replyModError(message):
        '''Sends Error msg with menu.'''
        message.reply_message(f"{message.content} bhosad ye mod nahi chal rha dusra try kr!!!\n\n{help_msg}")

    def replyNamo(message,driver,count=1):
        '''Sends random NAMO Memes.'''

        if count > 10:
            count = 10
        url = f"https://namo-memes.herokuapp.com/memes/{count}"

        response = requests.get(url)

        data = json.loads(response.text)

        bad = 0

        for d in data:
            print(d['url'])
            try:
                if (d['url']).endswith('gif'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.gif","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.gif",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('jpg'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.jpg","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.jpg",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('jpeg'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.jpeg","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.jpeg",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                elif (d['url']).endswith('png'):
                    resp = requests.get(d['url'])
                    if resp.status_code == 200:
                        f  = open("media/sample.png","wb")
                        f.write(resp.content)
                        f.close()
                        driver.send_media(path="media/sample.png",chatid = message.chat_id, caption = "Pyare MODIJI")
                    else:
                        bad = bad + 1

                else:
                    bad = bad + 1
            except Exception as e:
                print(e)
                bad = bad + 1
        if bad !=0:
            message.reply_message(f"{bad} images has been taken down by MODIJI")
    
    def replyPing(message):
        '''Sends Ping.'''
        current_time = time.ctime()
        hr = time.localtime().tm_hour

        if 5 <= hr <=11:
            ping_msg = f"Good Morning 🌅 🌇 🌄 Boiis\n No need to fear *LORD* is here.\n{current_time}\n\n LORD is doing workout with IQ, and you should also pump your body."
        elif 12 <= hr <= 17:
            ping_msg = f"Good afternoon 🌞 ⛅ 🕛 Boiss\n {current_time}\n\n *LORD* is doing some research with *MIRA* to upgrade his LMG."
        elif 18 <= hr <= 22:
            ping_msg = f"Good Evening 🌇 🌄 🌅 🌆 Boiss\n {current_time}\n\n *LORD* is in the evening traning session with *CAV*💀."
        else:
            ping_msg = f"Good Night 🌃 🌉 Boiis\n {current_time}\n\n *LORD* is going for bed 🛏 🛌 😴 💤 after having drink party 🍹 🍺 🎉 🥳  with his mates."
    

        message.reply_message(ping_msg)


