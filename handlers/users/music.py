from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import MusicState
from buttons import buttons as bt
from loader import dp

@dp.message_handler(state=MusicState.get_back)
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
async def bot_message(message: types.Message, state: FSMContext):
    get_back_button = KeyboardButton('Вернуться к выбору плейлиста')
    exit_button = KeyboardButton('Выход')
    exit_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        get_back_button).add(exit_button)
    if message.text == 'Spotify':
        await message.answer("https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW",
                             reply_markup=exit_menu)
    if message.text == 'VK':
        await message.answer("https://vk.com/music/album/-2000517727_11517727_acba018a8ba0af12f6",
                             reply_markup=exit_menu)
    await MusicState.get_back.set()  # установка состояния выхода в меню выбора(состояние 2)



