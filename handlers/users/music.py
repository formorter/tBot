from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import MusicState
from loader import dp
from utils.misc.throttling import rate_limit


@dp.message_handler(text="Выход", state=MusicState.get_back_menu)
async def stop_cast_playlist(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=f"Ты вышел \nДля просмотра доступных команд используй /help \nИли \"/\" в чат")


@dp.message_handler(commands=['music'], state="*")
@rate_limit(limit=5, key='music')
async def music(message: types.Message):
    spotify = KeyboardButton("Spotify")
    vk = KeyboardButton("VK")
    playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        spotify).add(vk)
    await message.answer('На какой платформе будем слушать?',
                         reply_markup=playlists_markup, )
    await MusicState.choose_music_platform.set()  #


@dp.message_handler(state=MusicState.get_back_menu)
async def music(message: types.Message):
    spotify = KeyboardButton("Spotify")
    vk = KeyboardButton("VK")
    playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        spotify).add(vk)
    await message.answer('На какой платформе будем слушать?',
                         reply_markup=playlists_markup, )
    await MusicState.choose_music_platform.set()  # задано состояние выбора платформы(состояние 1)


@dp.message_handler(state=MusicState.choose_music_platform)
# вместо текста или команды фильтром выступает параметр state,
# определяющий в каком состоянии находится пользователь
async def bot_message(message: types.Message):
    spoti_plotniy_playlist = KeyboardButton('ПЛОТНЫЙ РЭП')
    spoti_witch_house = KeyboardButton('ViVoDDn3#2')
    vk_morgen_album = KeyboardButton('MORGENSHTERN - MILLION DOLLAR: HAPPINESS')
    spoti_playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        spoti_plotniy_playlist).add(spoti_witch_house)
    vk_playlists_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        vk_morgen_album)
    if message.text == 'Spotify':
        await message.answer("Вот все доступные плейлисты в спотифай",
                            reply_markup=spoti_playlists_markup)
    if message.text == 'VK':
        await message.answer("Вот все доступные плейлисты VK",
                             reply_markup=vk_playlists_markup)
    await MusicState.choose_music_album.set()  # установка состояния выхода в меню выбора(состояние 2)


@dp.message_handler(state=MusicState.choose_music_album)
async def choose_music(message: types.Message):
    get_back_button = KeyboardButton('Вернуться к выбору плейлиста')
    exit_button = KeyboardButton('Выход')
    exit_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        get_back_button).add(exit_button)
    if message.text == 'ПЛОТНЫЙ РЭП':
        await message.answer("https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW",
                             reply_markup=exit_menu)
    if message.text == 'VivoDDn3#2':
        await message.answer("https://open.spotify.com/playlist/2U9iYP0tAtDM8j5Zm3Eiv0?si=301482f1b4d54e85",
                             reply_markup=exit_menu)
    if message.text == 'MORGENSHTERN - MILLION DOLLAR: HAPPINESS':
        await message.answer("https://vk.com/music/album/-2000517727_11517727_acba018a8ba0af12f6",
                             reply_markup=exit_menu)
    await MusicState.get_back_menu.set()