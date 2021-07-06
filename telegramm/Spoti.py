import telebot
from telebot import types

TOKEN = '1742555924:AAGRqx3iu9TKqVSA82CGuzpnYQ2oA2Ln4Ws'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['Музыка'])
def spotify(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    item1 = types.KeyboardButton('Спотифай')

    markup.add(item1)

    bot.send_message(message.chat.id, 'На какой платформе будем слушать?'.format(message.from_user), reply_markup=markup)
