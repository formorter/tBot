from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_one_time_button(message=[]):
    for i in range(len(message)):
        button_message = KeyboardButton(message[i])
        btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_message)
    return btn


def create_button(message=[]):
    for i in range(len(message)):
        button_message = KeyboardButton(message[i])
        btn = ReplyKeyboardMarkup(resize_keyboard=True).add(button_message)
    return btn
