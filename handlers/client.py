from aiogram import Dispatcher, types
from dispatcher import bot
from buttons import client_raspisanie
from parser import result

x = None

async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Добро пожаловать. Данный бот создан для того что бы мониторить расписание. Для того что бы увидеть расписание нажмите на кнопку 'Отобразить расписание'. Приятного пользования.", reply_markup=client_raspisanie)

async def raspisanie(message: types.Message):
    await bot.send_message(message.from_user.id, result(x), reply_markup=client_raspisanie)

async def sets(message: types.Message):
    global x
    x = message.text[5:]
    await bot.send_message(message.from_user.id, "Ссылка успешно обновлена.", reply_markup = client_raspisanie)

async def other(message: types.Message):
    await message.answer("В данном случае, я не понимаю что вы от меня хотите.")
    await message.delete()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(sets, commands=['set'])
    dp.register_message_handler(raspisanie, text = "Отобразить расписание")
    dp.register_message_handler(other)

