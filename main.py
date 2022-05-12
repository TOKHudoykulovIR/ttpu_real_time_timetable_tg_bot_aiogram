from aiogram import Bot, Dispatcher, executor
import os
from dotenv import load_dotenv
from sqlite import sql_start

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
api_token = API_TOKEN
bot = Bot(token=api_token)
dp = Dispatcher(bot)


async def on_startup(dp):
    sql_start()
    print(">>>")

if __name__ == '__main__':
    print(">")
    from handlers import dp
    print(">>")
    executor.start_polling(dp, on_startup=on_startup)
