from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

buttons1 = KeyboardButton("Отобразить расписание")

client_raspisanie = ReplyKeyboardMarkup(resize_keyboard=True)
client_raspisanie.add(buttons1)