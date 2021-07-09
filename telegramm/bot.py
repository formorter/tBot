"""
Заготовка под пода на aiogram
Выводит только текст к команде /start
"""

from Logger import BotLogger
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0'

start_logg = BotLogger()
start_logg.info_log('Бот запущен, приятного пользования')
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Я AXIUS.\nДля того, чтобы узнать, что я умею, используй /help")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
