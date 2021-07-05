import telebot

from botlogger import BotLogger

TOKEN = '1742555924:AAGRqx3iu9TKqVSA82CGuzpnYQ2oA2Ln4Ws'
bot = telebot.TeleBot(TOKEN)

logger = BotLogger()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Помощи пока нет.')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Ку')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю')

bot.polling(none_stop=True)
