################################################################
# Chanka Bot
# ----------------------------------------------------------------
# uses openwa library


from openwa import WhatsAPIDriver
import json
import time
from Mods.ReplyMods import replymods as RM  #NOTE:all the mods are saved in this module you can ad new modules there


#NOTE: this is used get UserConfig data from UserConfig.json 
with open("UserConfig.json","r") as f:
    d = f.read()
config_data = json.loads(d)
help_msg = config_data.get("HELP_MSG")
prefix = config_data.get("PREFIX")
owner = config_data.get("OWNER")
groups = config_data.get("GROUPS")
flag = 0

#NOTE:This inisitaes the driver from whatsapp web app and authenictes by scaning
# driver = WhatsAPIDriver(client="chrome",executable_path="chromedriver.exe",headless=False,chrome_options=['--disable-gpu'])
driver = WhatsAPIDriver(client="chrome",executable_path="chromedriver.exe",headless=False)

#NOTE:this class is used for receving and handling message
class NewMessageObserver:
    def on_message_received(self, new_messages):
        for message in new_messages:
            print(f"New message {message} received from number {message.sender.id}")

            if message.content.startswith(prefix):
                if message.content == f"{prefix}quote":
                    RM.replyQuote(message)

                elif message.content == f"{prefix}help":
                    RM.replyHelp(message)

                elif message.content == f"{prefix}noods":
                    RM.replyNoods(message)

                elif message.content == f"{prefix}menu":
                    RM.replyMenu(message)

                elif message.content == f"{prefix}namo":
                    RM.replyNamo(message, driver=driver)

                elif f"{prefix}namo " in message.content:
                    count = int(message.content.split(" ")[1])
                    RM.replyNamo(message, driver=driver, count=count)

                elif message.content == f"{prefix}ping":
                    RM.replyPing(message)

                elif message.content == f"{prefix}sticker":
                    RM.replySticker(message, driver=driver)

                elif message.content == f"{prefix}gif":
                    RM.replyVideoToGif(message, driver=driver)

                elif message.content.startswith(f"{prefix}memes"):
                    content_list = message.content.split(" ")
                    if len(content_list) == 2:
                        RM.replySr(message, driver=driver, count=int(content_list[-1]))
                    else:
                        RM.replySr(message, driver=driver)

                elif message.content.startswith(f"{prefix}sr"):
                    content_list = message.content.split(" ")
                    if len(content_list) == 2:
                        RM.replySr(message, driver=driver,query=content_list[-1])
                    elif len(content_list) == 3:
                        RM.replySr(message, driver=driver,query=content_list[-2],count=int(content_list[-1]))
                    else:
                        message.reply_message("First lean how to use this command, Biyath.")

                elif message.content.startswith(f"{prefix}say:"):
                    content_list = message.content.split(':')
                    if len(content_list) == 2:
                        text = content_list[-1]
                        RM.replySay(message,text,driver=driver)
                    elif len(content_list) == 3:
                        text = content_list[-2]
                        lang = content_list[-1]
                        RM.replySay(message,text,driver=driver,lang=lang)
                    else:
                        text=""
                        RM.replySay(message,text,driver=driver)
                        
                elif message.content.startswith(f"{prefix}r6p"):
                    content_list = message.content.split(" ")
                    text = content_list[-1]
                    RM.replyRsixP(message,text,driver=driver)

                elif message.content.startswith(f"{prefix}r6t"):
                    content_list = message.content.split(" ")
                    text = content_list[-1]
                    RM.replyRsixT(message,text,driver=driver)

                elif message.content.startswith(f"{prefix}r6s"):
                    content_list = message.content.split(" ")
                    if len(content_list) == 2:
                        p = content_list[-1]
                        RM.replyRsixS(message,p,driver=driver)
                    elif content_list == 3:
                        p = content_list[2]
                        pl = content_list[1]
                        RM.replyRsixS(message,p,pl,driver=driver)
                    else:
                        message.reply_message("Command use krna sikh bhosad.")
                else:
                    RM.replyModError(message)
            else:
                pass

print("Waiting for QR")

#NOTE:this is used to subscribe message handling class to the driver
driver.subscribe_new_messages(NewMessageObserver())

#NOTE: loop is infinite coz of continues listning of messages
while(True):
    time.sleep(60)


# while True:
#     if driver.wait_for_login():
#         #starting bot
#         print("*Lord is Back* 👑 ⚒ 🙋 🎁 ")
#         driver.chat_send_message(owner,"*Lord is Back* 👑 ⚒ 🙋 🎁 ")
#         groups = driver.get_all_groups()
#         # for group in groups:
#         #     group.send_message("*Lord is Back* 👑 ⚒ 🙋 🎁 ")       
#         break
#     else:
#         pass

# while not driver.wait_for_login():
#     pass


#starting bot
# print("*Lord is Back* 👑 ⚒ 🙋 🎁 ")
# driver.chat_send_message(owner,"*Lord is Back* 👑 ⚒ 🙋 🎁 ")
# groups = driver.get_all_groups()
# for group in groups:
#     group.send_message("*Lord is Back* 👑 ⚒ 🙋 🎁 ")


# def replyMission(message):
#     if message.sender.id == owner:
#         #bot stopped
#         print("*Lord is going on mission* 👨‍🚒 💂 🔫 ⚠ \n*he will be back*\n\n*WISH HIM LUCK 👍*")
#         driver.chat_send_message(owner,"*Lord is going on mission* 👨‍🚒 💂 🔫 ⚠ \n*he will be back*\n\n*WISH HIM LUCK 👍*")

#         # groups = driver.get_all_groups()
#         # for group in groups:
#         #     group.send_message("*Lord is going on mission* 👨‍🚒 💂 🔫 ⚠ \n*he will be back*\n\n*WISH HIM LUCK 👍*")
#         return 1
#     else:
#         message.reply_message("*You are not my boss.*\n\n _Only chevi sensei can send to me to the mission._")
#         return 0




