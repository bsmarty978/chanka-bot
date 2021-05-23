from openwa import WhatsAPIDriver
import time
import json
import random
import os
from Mods import ReplyMods as RM


# random.randint(0,22)
# import asyncio
# from selenium import webdriver
# with open("quotes.json","r") as f:
#     d = f.read()
# data = json.loads(d)

driver = WhatsAPIDriver(client="chrome",executable_path="chromedriver.exe",headless=False)

prefix = os.getenv("PREFIX")
help_msg = os.getenv("HELP_MSG")


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
                else:
                    RM.replyModError(message)
            else:
                pass

                
                

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Firefox()
# browser.get('http://selenium.dev/')
driver.subscribe_new_messages(NewMessageObserver())
while(True):
    pass
    # # Save image to file
    # driver.get_qr()

    # # Get image in base64 
    # driver.get_qr_base64()




