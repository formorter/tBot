from aiogram import types

from telegramm import buttons as bt
from loader import dp


@dp.message_handler(commands=['music'])
async def music(message: types.Message):
    await message.answer('На какой платформе будем слушать?',
                         reply_markup=bt.create_button(['Spotify']))
