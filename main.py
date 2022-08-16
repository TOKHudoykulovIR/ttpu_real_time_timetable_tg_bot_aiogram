from aiogram import Bot, Dispatcher, executor
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from sql import sql_start
from aiogram.types import BotCommand

load_dotenv()


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Get Menu"),
        BotCommand(command="/help", description="Get Instructions"),
    ]
    await bot.set_my_commands(commands)


storage = MemoryStorage()

API_TOKEN = os.getenv("API_TOKEN")
api_token = API_TOKEN
bot = Bot(token=api_token)
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp):
    sql_start()
    print(">>>")
    await set_commands(bot)


if __name__ == '__main__':
    print(">")
    from handlers import dp

    print(">>")
    executor.start_polling(dp, on_startup=on_startup)
