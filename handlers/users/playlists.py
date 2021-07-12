from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Spotify':
        await message.answer("https://open.spotify.com/playlist/5BQemH4tSKWnOeUjOGGCJW")