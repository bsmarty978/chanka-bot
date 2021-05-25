################################################################
# Chanka Bot
# ----------------------------------------------------------------
# uses openwa library


from openwa import WhatsAPIDriver
import json
from Mods.ReplyMods import replymods as RM  #NOTE:all the mods are saved in this module you can ad new modules there


#
# with open("quotes.json","r") as f:
#     d = f.read()
# data = json.loads(d)

#NOTE: this is used get UserConfig data from UserConfig.json 
with open("UserConfig.json","r") as f:
    d = f.read()
config_data = json.loads(d)
help_msg = config_data.get("HELP_MSG")
prefix = config_data.get("PREFIX")


#NOTE:This inisitaes the driver from whatsapp web app and authenictes by scaning
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

                else:
                    RM.replyModError(message)
            else:
                pass

#NOTE:this is used to subscribe message handling class to the driver
driver.subscribe_new_messages(NewMessageObserver())

#NOTE: loop is infinite coz of continues listning of messages
while(True):
    pass




