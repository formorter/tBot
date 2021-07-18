from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import MusicState
from buttons import buttons as bt
from loader import dp


@dp.message_handler(commands=['music'])
async def music(message: types.Message):
    spotify = KeyboardButton("Spotify")
    vk = KeyboardButton("VK")
    playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        spotify).add(vk)
    await message.answer('На какой платформе будем слушать?',
                         reply_markup=playlists_markup, )
    await MusicState.choose_platform.set()  # задано состояние выбора платформы(состояние 1)


@dp.message_handler(state=MusicState.choose_platform)
# вместо текста или команды фильтром выступает параметр state,
# определяющий в каком состоянии находится пользователь
async def bot_message(message: types.Message):
    if message.text == 'Spotify':
        await message.answer("https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW",
                             reply_markup=bt.create_one_time_button('Вернуться к выбору плейлиста'))
    if message.text == 'VK':
        await message.answer("https://vk.com/music/album/-2000517727_11517727_acba018a8ba0af12f6",
                             reply_markup=bt.create_one_time_button('Вернуться к выбору плейлиста'))
    await MusicState.get_back.set()  # установка состояния выхода в меню выбора(состояние 2)


@dp.message_handler(state=MusicState.get_back)
async def music(message: types.Message, state: FSMContext):
    spotify = KeyboardButton('Spotify')
    vk = KeyboardButton('VK')
    playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        spotify).add(vk)
    await message.answer('На какой платформе будем слушать?',
                         reply_markup=playlists_markup, )

    await MusicState.first()  # возвращаемся к первому состоянию выбора плейлиста
     # await state.finish()  # сбрасываем состояние
