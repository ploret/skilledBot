#!/usr/bin/python

import sys
import os
import configparser
import traceback

import telebot
from modules.currency import *
from modules.motivation import *

try:
    if len(sys.argv) == 1:
        sys.exit("Usage %s token" % sys.argv[0])

    token = sys.argv[1]
    bot = telebot.TeleBot(token)

    work_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = work_dir + '/config/settings.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    @bot.message_handler(func=lambda message: message.text == "help")
    def help(m):
        bot.send_message(m.chat.id, "1. help\n"
                                    "2. usd\n"
                                    "3. motivation")

    @bot.message_handler(func=lambda message: message.text == "usd")
    def display_usd(m):
        usd_info_url = config['currency']['privatbank']
        html = get_html_source_code(usd_info_url)
        usd = get_privatbank_usd(html)
        message = "Приватбанк\nпокупка: {usd_buy} грн\nпродажа: {usd_sale} грн".format(usd_buy=usd['buy'],
                                                                               usd_sale=usd['sale'])
        bot.send_message(m.chat.id, message)


    @bot.message_handler(func=lambda message: message.text == "motivation")
    def display_motivation(m):
        motivation_db_path = work_dir + '/db/' + config['motivation']['sqlite_db']
        quotations_table = config['motivation']['sqlite_table']
        quotation_info = get_random_quotation(motivation_db_path, quotations_table)
        message = "{quotation}\n{author}".format(quotation=quotation_info['text'],
                                                 author=quotation_info['author'])
        bot.send_message(m.chat.id, message)


    bot.polling()

except Exception:
    traceback.print_exc()