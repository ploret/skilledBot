#!/usr/bin/python

import telebot
import sys

if len(sys.argv) == 1:
    sys.exit("Usage %s token" % sys.argv[0])

token = sys.argv[1]
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: message.text == "help")
def my_func(m):
    bot.send_message(m.chat.id, "My respond")

bot.polling()