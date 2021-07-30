from aiogram.dispatcher.filters.state import StatesGroup, State


# здесь заданы состояния для хендлера выбора музыки

class MusicState(StatesGroup):
    on_start_menu = State()
    choose_music_platform = State()
    choose_music_album = State()
    get_back_menu = State()