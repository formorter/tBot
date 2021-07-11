from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_one_time_button(message):
    button_message = KeyboardButton(message)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_message)
    return btn


def create_button(message):
    button_message = KeyboardButton(message)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_message)
    return btn
