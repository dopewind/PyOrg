from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

import os

updater = Updater(
    token='1185740681:AAG_H3nxkveqKBdl4z1-MCgA80Zln3Mpk3E', use_context=True)

dispatcher = updater.dispatcher


# =========================logging==============================

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# ============================ /start ============================
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Your wish is my command, master")


def stop(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I ain't going anywhere chief")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('stop', stop)
dispatcher.add_handler(start_handler)


updater.start_polling()

# ============================== echo all msgs =======================


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
