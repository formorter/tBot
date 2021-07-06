import telebot
from telebot import types

TOKEN = '1742555924:AAGRqx3iu9TKqVSA82CGuzpnYQ2oA2Ln4Ws'
bot = telebot.TeleBot(TOKEN)


class Spotify:
    def __init__(self, message):
        self.message = message
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    @bot.message_handler(content_types=['text'])
    def mess(self):
        item1 = types.KeyboardButton(f'{self.message}')
        self.markup.add(item1)


