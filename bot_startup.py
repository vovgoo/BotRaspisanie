from aiogram import executor
from dispatcher import dp

async def on_startup(_):
    print("Бот успешно запущен. И готов к работе.")

from handlers import client

client.register_handlers_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup=on_startup)

