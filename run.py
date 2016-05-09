#!/usr/bin/python
import sys
import os
import traceback
import configparser
import telebot
from modules.currency import *
from modules.motivation import *
from modules.gift import *


try:
    if len(sys.argv) == 1:
        sys.exit("Usage %s token" % sys.argv[0])

    token = sys.argv[1]
    bot = telebot.TeleBot(token)

    work_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = work_dir + '/config/settings.ini'

    if not os.path.isfile(config_path):
        raise Exception(config_path + ' file doesn`t exist')

    config = configparser.ConfigParser()
    config.read(config_path)

    @bot.message_handler(func=lambda message: message.text == "help")
    def commands(m):
        """ display all allowed commands """
        bot.send_message(m.chat.id, "1. help\n"
                                    "2. usd\n"
                                    "3. motivation\n"
                                    "4. gift")

    @bot.message_handler(func=lambda message: message.text == "usd")
    def display_usd(m):
        """ display actual USD exchange rate """
        usd_info_url = config['currency']['bank']
        html = get_html_source_code(usd_info_url)
        usd = get_usd(html)
        message = "Курс валют USD\nпокупка: {usd_buy} грн\nпродажа: {usd_sale} грн".format(usd_buy=usd['buy'],
                                                                                           usd_sale=usd['sale'])
        bot.send_message(m.chat.id, message)


    @bot.message_handler(func=lambda message: message.text == "motivation")
    def display_motivation(m):
        """ display random motivational quotation """
        motivation_db_path = work_dir + '/db/' + config['motivation']['sqlite_db']
        quotations_table = config['motivation']['sqlite_table']
        quotation_info = get_random_quotation(motivation_db_path, quotations_table)
        message = "{quotation}\n{author}".format(quotation=quotation_info['text'],
                                                 author=quotation_info['author'])
        bot.send_message(m.chat.id, message)


    @bot.message_handler(func=lambda message: message.text == "gift")
    def display_gift(m):
        """ display random gift idea """
        gift_json_path = work_dir + '/db/' + config['gifts']['json_file']
        gifts = get_gifts_from_json(gift_json_path)
        gift = get_random_gift(gifts)
        message = "Идея для подарка:\n{random_gift}".format(random_gift=gift)
        bot.send_message(m.chat.id, message)

    bot.polling()

except Exception:
    traceback.print_exc()