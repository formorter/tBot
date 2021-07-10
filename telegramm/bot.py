import telebot
from aiogram import Bot, Dispatcher, executor, types
import logging
from telebot import types
from Logger import BotLogger

# from telegramm.Spoti import spotify
TOKEN = "1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

start_logger = BotLogger()
start_logger.main('Бот запущен, приятного пользования')

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет\nЧто хочешь ?')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






