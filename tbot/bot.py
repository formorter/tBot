import telebot 
from telebot import types

TOKEN = '1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    item1 = types.KeyboardButton('Спотифай')

    markup.add(item1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Спотифай':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Наш плейлист')
        back = types.KeyboardButton('Назад')
        markup.add(item1, back)
        bot.send_message(message.chat.id, 'https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW')


    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

        item1 = types.KeyboardButton('Спотифай')

        markup.add(item1)

        bot.send_message(message.chat.id, 'Назад', reply_markup = markup)

        

bot.polling(none_stop=True)