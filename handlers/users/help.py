from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def hello(message: types.Message):
    await message.answer('Доступные команды:\n/music - можешь выбрать плейлист')
