import telebot
from telebot import types
from telegramm.Logger import BotLogger
from telegramm.Spoti import spotify

TOKEN = '1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0'
bot = telebot.TeleBot(TOKEN)

start_logger = BotLogger()
start_logger.main('Бот запущен, приятного пользования')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я AXIUS, для того, чтобы узнать, что я умею, используй /help')


@bot.message_handler(commands=['music'])
def spotify(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    item1 = types.KeyboardButton('Спотифай')

    markup.add(item1)

    bot.send_message(message.chat.id, 'На какой платформе будем слушать?'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, f'На данный момент имеется только команда /music')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Плейлист')
    markup.add(item1)
    if message.text == 'Спотифай':
        bot.send_message(message.chat.id, 'Выберите плейлист', reply_markup=markup)
    elif message.text == 'Плейлист':
        bot.send_message(message.chat.id, 'https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW',
                         reply_markup=markup)


bot.polling(none_stop=True)
