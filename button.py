import crypt
import config
import telebot
import secrets
import os

bot = telebot.TeleBot(config.TG_TOKEN)


def usb_out():
    password = secrets.token_hex(32)
    bot.send_message(config.TG_USERID, f'your password is:\n{password}')
    crypt.walk(config.TO_CRYPT, password, crypt.crypt)
    del password
    print('crypted successfully')
    os.system('shutdown -s -t 0')
    # your code here


usb_in = True

while usb_in:
    try:
        file = open(config.CHECK, 'r')
        file.close()
    except:
        usb_out()
        usb_in = False
