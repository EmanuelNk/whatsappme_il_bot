#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def isValid(s):     
    # 1) Begins with 0 or 972 or +972
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|972|+972)?[0-9]{9}")
    return Pattern.match(s)

def whatsapp_link(s):
    if s.startswith('0'):       
        phone = '+972'+s[1:]
    if s.startswith('972'): 
        phone = '+'+s
    else:
        phone = s
    return f'http://api.whatsapp.com/send?phone={phone}'

# Driver Code
s = "347873923408"
if (isValid(s)): 
    print ("Valid Number")     
else :
    print ("Invalid Number") 
  
  
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def whatsapp_me(update, context):
    """Echo the user message."""
    s = update.message.text
    if (isValid(s)): 
        link = whatsapp_link()
        update.message.reply_text(link)
    else:
        update.message.reply_text("please enter a valid phone number")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5126302250:AAGN7TFh4DNfxQx7xvrjAH7sOLjcMOvEXYY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, whatsapp_me))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()