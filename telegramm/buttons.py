from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_music = KeyboardButton("Spotify")
music_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(button_music)