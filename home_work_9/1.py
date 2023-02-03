from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint as rd

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Hello')

def rand(update, context):
    context.bot.send_message(update.effective_chat.id, f'{rd(1, 100)}')


def default(update, contex):
    contex.bot.send_message(update.effective_chat.id, "Я не знаю таких команд")


def filter_txt(update, contex):
    text = update.message.text
    text = [i for i in text.split() if 'абв' not in i]
    contex.bot.send_message(update.effective_chat.id, f'{" ".join(text)}')


start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random', rand)
default_handler = MessageHandler (Filters.command, default)
filter_txt_handler = MessageHandler(Filters.text, filter_txt)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(default_handler)
dispatcher.add_handler(filter_txt_handler)


print('Сервер запущен')
updater.start_polling()
updater.idle()
