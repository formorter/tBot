from aiogram import Bot, Dispatcher, \
                    executor, types

from Logger import BotLogger
import buttons as bt
# from Spoti import spotify

TOKEN = "1782289333:AAF66r8nfRumURI9O1Dvv_mLc5rBh_4OZh0"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

start_logger = BotLogger()
start_logger.info_logg('Бот запущен, приятного пользования')


@dp.message_handler(commands=['start', 'help'])
async def hello(message: types.Message):
    if message.text == '/start':
        await bot.send_message(message.from_user.id, 'Привет, я AXIUS.\nЧтобы узнать, что я умею, пиши /help',)
    else:
        help_txt = open('help-commands.txt', encoding='utf-8')
        await bot.send_message(message.from_user.id, help_txt.read(),)


@dp.message_handler(commands=['music'])
async def music(message: types.Message):
    await bot.send_message(message.from_user.id, 'На какой платформе будем слушать?',
                           reply_markup=bt.create_one_time_button('Spotify'))


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Spotify':
        await bot.send_message(message.from_user.id, "https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






