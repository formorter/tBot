import telebot
from aiogram import Bot, Dispatcher, executor, types
import logging
from telebot import types
from Logger import BotLogger
import buttons as bt

# from telegramm.Spoti import spotify
TOKEN = "1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

start_logger = BotLogger()
start_logger.main('Бот запущен, приятного пользования')

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет\nЧто хочешь ?', reply_markup=bt.music_btn)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Spotify':
        await bot.send_message(message.from_user.id, "https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






