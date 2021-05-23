import json
import random
import os

help_msg = os.getenv('HELP_MSG')
with open("quotes.json","r") as f:
    d = f.read()
data = json.loads(d)

def replyQuote(message):
    quote = data[random.randint(0,1840)]["text"]
    message.reply_message(quote)

def replyHelp(message):
    message.reply_message(f"Lavde abhi kam chal rha he apna kam kr nalla gandu!!!!\n\n{help_msg}")

def replyNoods(message):
    message.reply_message("Tharki sala porn dekh bathroom me jake<><>")

def replyMenu(message):
    message.reply_message(help_msg)

def replyModError(message):
    message.reply_message(f"{message.content} bhosad ye mod nahi chal rha dusra try kr!!!\n\n{help_msg}")