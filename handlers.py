from aiogram import types
from aiogram.dispatcher.filters import Text
from main import dp
from keyboards import keyboard_years, keyboard_2020, keyboard_2019, keyboard_2018, cd_years, cd_2020, cd_2019
from aiogram.types import CallbackQuery
from parse_timetable import parse
import datetime
from sqlite import add_user, get_info
import os


def data(message):
    user_id = int(message.chat.id)
    user_name = str(message.chat.full_name)
    print(user_id, user_name)
    user_text = str(message.text)
    time = datetime.datetime.now()
    return user_id, user_name, user_text, time


@dp.message_handler(commands=["admin"])
async def stats(message: types.Message):
    admin_id = os.getenv("admin_id")
    if int(message.from_user.id) == int(admin_id):
        await message.answer("Hi, boss")
        dataset = await (get_info())
        await message.answer(dataset)


#  > > >  BASE COMMANDS
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    user_id, user_name, user_text, time = data(message)
    await add_user(user_id, user_name, user_text, time)
    await message.answer("𝙲𝙷𝙴𝙲𝙺 𝚃𝙷𝙴 𝚃𝙸𝙼𝙴𝚃𝙰𝙱𝙻𝙴📋 𝙱𝚈 𝙶𝚁𝙾𝚄𝙿𝚂\n"
                         "  𝙸𝙽𝚂𝚃𝚄𝙲𝚃𝙸𝙾𝙽:\n"
                         "𝟭.  𝚃𝚈𝙿𝙴 𝙾𝚁 𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 /start 𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝙽𝚄 𝙸𝙽 𝚃𝙷𝙴 𝙻𝙾𝚆𝙴𝚁 𝙻𝙴𝙵𝚃 𝙲𝙾𝚁𝙽𝙴𝚁\n"
                         "𝟸.  𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈\n"
                         "𝟹.  𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿")


@dp.message_handler(commands=['start'])
async def show_keyboard_levels(message: types.Message):
    user_id, user_name, user_text, time = data(message)
    await add_user(user_id, user_name, user_text, time)
    await message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...', reply_markup=keyboard_years)
#  < < <


#  > > >  FILTER BY YEARS
@dp.callback_query_handler(cd_years.filter(year="20"))
async def year_20(call: CallbackQuery):
    await call.message.answer('𝟸𝟶𝟸𝟶 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
                              '‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›',
                              reply_markup=keyboard_2020)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_years.filter(year="19"))
async def year_19(call: CallbackQuery):
    await call.message.answer('𝟸𝟶𝟷𝟿 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
                              '‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›',
                              reply_markup=keyboard_2019)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(Text(equals='yyyy:18'))
async def year_18(call: CallbackQuery):
    await call.message.answer('𝟸𝟶𝟷𝟾 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
                              "‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›",
                              reply_markup=keyboard_2018)
    await call.message.edit_reply_markup(reply_markup=None)


# CANCEL
@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    # await call.answer('Cancel', show_alert=True)
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...', reply_markup=keyboard_years)
    await call.message.edit_reply_markup(reply_markup=None)
#  < < <


async def parse_data(call):
    clicked_btn = call.data
    await call.message.answer('𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶🔎...')
    await parse(clicked_btn[3:], call)
    await call.message.answer('⬇️ 𝚈𝙾𝚄𝚁 𝚃𝙸𝙼𝙴𝚃𝙰𝙱𝙻𝙴 ⬇️')
    await call.message.answer_photo(photo=open("image.png", "rb"))
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_2020.filter(
    group=[
        "1IT4-20", "1IT7-20", "1IT1-20", "1IT2-20", "1IT3-20", "1IT5-20",
        "1IT6-20",
        "1.ME1-2-20", "1.ME3-4-20",
        "1CIE1-2-20",
    ]))
async def groups_year_20(call: CallbackQuery):
    await parse_data(call)


@dp.callback_query_handler(cd_2019.filter(
    group=[
        "2IT1-19", "2IT2-19", "2IT3-19", "2IT4-19", "2IT5-19", "2IT6-19",
        "2.ME1-19", "2.ME2-19", "2.ME3-19", "2.ME4-19", "2.ME5-19", "2.ME6-19",
        "2CIE2-19", "2CIE2-19"
    ]))
async def groups_year_19(call: CallbackQuery):
    await parse_data(call)
