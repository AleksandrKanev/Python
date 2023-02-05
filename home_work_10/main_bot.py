from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import controllers

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Приветствую  {update.effective_user.first_name}\nВведите пример')



def cal(update, contex):
    user = f'{update.effective_user.first_name}; {update.message.from_user.id}'
    primer = update.message.text
    result = controllers.process_func(primer, user)
    contex.bot.send_message(update.effective_chat.id, f'{primer} = {result}')



start_handler = CommandHandler('start', start)
cal_handler = MessageHandler(Filters.text, cal)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(cal_handler)


print('Сервер запущен')
updater.start_polling()
updater.idle()
