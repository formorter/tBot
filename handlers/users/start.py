from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, middleware_data):
    await message.answer(f'Привет, я AXIUS.\nЧтобы узнать, что я умею, пиши /help')  # \n{middleware_data=}
    return {"data_from_handler": "информация из хендлера"}  # тест мидлваря
