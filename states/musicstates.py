from aiogram.dispatcher.filters.state import StatesGroup, State


# здесь заданы состояния для хендлера выбора музыки

class MusicState(StatesGroup):
    choose_platform = State()
    get_back = State()
