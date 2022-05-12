from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import os
from sqlite import get_info


async def stats(message: types.Message, state: FSMContext):
    await state.finish()
    admin_id = os.getenv("admin_id")
    if int(message.from_user.id) == int(admin_id):
        await message.answer("Hi, boss")
        data = await (get_info())
        await message.answer(data)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(stats, commands=["admin"], state="*")
