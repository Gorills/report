
import re

import telepot

token = '5582931297:AAFGK31SftLD5cewmHJqhDbeIVK73YkBJAM'
my_id = -1001586184216
telegramBot = telepot.Bot(token)

def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")
