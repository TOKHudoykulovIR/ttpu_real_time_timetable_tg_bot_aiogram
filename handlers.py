from aiogram import types
from main import dp
from keyboards import keyboard_years, keyboard_2020, keyboard_2019, cd_years, cd_2020, cd_2019, \
    menu_keyboard, tel_numbers_keyboard, course_keyboard, \
    cd_menu, cd_tel_num, cd_course
from aiogram.types import CallbackQuery
from parser import parse
import datetime
from sql import add_user, get_info
import os
# from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMMenu(StatesGroup):
    first_lvl = State()
    second_lvl = State()
    third_lvl = State()


def data(message):
    user_id = int(message.chat.id)
    user_name = str(message.chat.full_name)
    print(user_id, user_name)
    user_text = str(message.text)
    time = datetime.datetime.now()
    return user_id, user_name, user_text, time


#                                           $ $ $ BASE COMMANDS $ $ $
@dp.message_handler(commands=["admin"], state="*")
async def stats(message: types.Message):
    admin_id = os.getenv("admin_id")
    if int(message.from_user.id) == int(admin_id):
        await message.answer("<𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝙴>")
        await (get_info())
        await message.answer_document(open("usage_history.csv", "rb"))
        await message.answer_document(open("users_list.csv", "rb"))


@dp.message_handler(commands=['help'], state="*")
async def send_instruction(message: types.Message):
    user_id, user_name, user_text, time = data(message)
    await add_user(user_id, user_name, user_text, time)
    await message.answer("𝙲𝙷𝙴𝙲𝙺 𝚃𝙷𝙴 𝚃𝙸𝙼𝙴𝚃𝙰𝙱𝙻𝙴📋 𝙱𝚈 𝙶𝚁𝙾𝚄𝙿𝚂\n"
                         "  𝙸𝙽𝚂𝚃𝚄𝙲𝚃𝙸𝙾𝙽:\n"
                         "𝟭.  𝚃𝚈𝙿𝙴 𝙾𝚁 𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 /start 𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝙽𝚄 𝙸𝙽 𝚃𝙷𝙴 𝙻𝙾𝚆𝙴𝚁 𝙻𝙴𝙵𝚃 𝙲𝙾𝚁𝙽𝙴𝚁\n"
                         "𝟸.  𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈\n"
                         "𝟹.  𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿")


@dp.message_handler(commands=['start'], state="*")
async def show_keyboard_levels(message: types.Message):
    user_id, user_name, user_text, time = data(message)
    await add_user(user_id, user_name, user_text, time)
    await message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈", reply_markup=menu_keyboard)
    # await message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...',
    #                      reply_markup=keyboard_years)


# @dp.message_handler(commands=['menu'], state="*")
# async def show_keyboard_categories(message: types.Message):
#     user_id, user_name, user_text, time = data(message)
#     await add_user(user_id, user_name, user_text, time)
#     await message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈", reply_markup=menu_keyboard)

#                                           & & &

@dp.callback_query_handler(cd_menu.filter(category=["timetable", "catalog", "contacts"]))
async def menu(call: CallbackQuery):
    if str(call.data)[5:] == "timetable":
        await call.message.answer(
            '𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...',
            reply_markup=keyboard_years)
    elif str(call.data)[5:] == "catalog":
        await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙻𝙴𝚅𝙴𝙻', reply_markup=course_keyboard)
    elif str(call.data)[5:] == "contacts":
        await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙾𝙽𝚃𝙰𝙲𝚃', reply_markup=tel_numbers_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)


#  > > >  FILTER BY YEARS
@dp.callback_query_handler(cd_years.filter(year=["20", "19"]), state="*")
async def admission_years(call: CallbackQuery):
    if str(call.data)[5:] == "20":
        await call.message.answer(
            '𝟸𝟶𝟸𝟶 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
            '‹𝙾𝙽 𝙰𝚅𝙴𝚁𝙰𝙶𝙴 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂 ⏱›\n'
            '❗❗❗️️ 𝙸𝙵 𝚈𝙾𝚄 𝙶𝙴𝚃 𝙰𝙽 𝙸𝙽𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙰𝙽𝚂𝚆𝙴𝚁, 𝚃𝚁𝚈 𝙰𝙶𝙰𝙸𝙽 ❗❗❗️',
            reply_markup=keyboard_2020)
    elif str(call.data)[5:] == "19":
        await call.message.answer(
            '𝟸𝟶𝟷𝟿 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
            '‹𝙾𝙽 𝙰𝚅𝙴𝚁𝙰𝙶𝙴 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂 ⏱›\n'
            '❗❗❗️️ 𝙸𝙵 𝚈𝙾𝚄 𝙶𝙴𝚃 𝙰𝙽 𝙸𝙽𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙰𝙽𝚂𝚆𝙴𝚁, 𝚃𝚁𝚈 𝙰𝙶𝙰𝙸𝙽 ❗❗❗️',
            reply_markup=keyboard_2019)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_years.filter(year=["back"]), state="*")
async def back_main(call: CallbackQuery):
    await call.message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)


# CANCEL
@dp.callback_query_handler(text_contains='cancel', state="*")
async def cancel(call: CallbackQuery):
    # await call.answer('Cancel', show_alert=True)
    await call.message.answer(
        '𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...',
        reply_markup=keyboard_years)
    await call.message.edit_reply_markup(reply_markup=None)


#  < < <


async def parse_data(call):
    clicked_btn = call.data
    await call.message.answer(f'𝚂𝙴𝙰𝚁𝙲𝙷... 🔎  {clicked_btn[3:]}')
    await parse(clicked_btn[3:], call)
    await call.message.answer('⬇️ 𝚈𝙾𝚄𝚁 𝚃𝙸𝙼𝙴𝚃𝙰𝙱𝙻𝙴 ⬇️')
    await call.message.answer_photo(photo=open("image.png", "rb"))
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_2020.filter(
    group=[
        "1IT4-20", "1IT7-20", "1IT1-20", "1IT2-20", "1IT3-20", "1IT5-20",
        "1IT6-20",
        "1.ME1-2-20", "1.ME3-4-20",
        "1CIE1-2-20", ]))
async def groups_year_20(call: CallbackQuery):
    await parse_data(call)


@dp.callback_query_handler(cd_2019.filter(
    group=[
        "2IT1-19", "2IT2-19", "2IT3-19", "2IT4-19", "2IT5-19", "2IT6-19",
        "2.ME1-19", "2.ME2-19", "2.ME3-19", "2.ME4-19", "2.ME5-19", "2.ME6-19",
        "2CIE2-19", "2CIE2-19"]))
async def groups_year_19(call: CallbackQuery):
    await parse_data(call)


# <><><><><><><><><><><><><><><><>


# @dp.message_handler(commands=['menu'], state="*")
# async def menu(message: types.Message):
#     await message.answer("choose category ↘︎", reply_markup=menu_keyboard)


@dp.callback_query_handler(cd_course.filter(course=["py", "first_lvl", "second_lvl", "third_lvl"]))
async def catalog(call: CallbackQuery):
    if str(call.data)[2:] == "py":
        await call.message.answer('py')
        await call.message.answer_photo(photo=open("levels/py.png", "rb"))
    elif str(call.data)[2:] == "first_lvl":
        await call.message.answer('first_lvl')
        await call.message.answer_photo(photo=open("levels/st_level.png", "rb"))
    elif str(call.data)[2:] == "second_lvl":
        await call.message.answer('second_lvl')
        await call.message.answer_photo(photo=open("levels/nd_level.png", "rb"))
    elif str(call.data)[2:] == "third_lvl":
        await call.message.answer('third_lvl')
        await call.message.answer_photo(photo=open("levels/rd_level.png", "rb"))
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_course.filter(course=["back"]))
async def back_catalog(call: CallbackQuery):
    await call.message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_tel_num.filter(
    owner=[
        "rector", "finance", "accounting", "hr",
        "post", "strategy", "inter", "it-dep",
        "marketing", "deans", "working-youth", "irc",
        "sport", "medical"]))
async def contacts(call: CallbackQuery):
    if str(call.data)[18:] == "rector":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟽0-𝟾𝟸')
    elif str(call.data)[18:] == "finance":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟷0-𝟸𝟻')
    elif str(call.data)[18:] == "accounting":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟸0-𝟽𝟿')
    elif str(call.data)[18:] == "hr":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟸0-𝟻𝟹')
    elif str(call.data)[18:] == "post":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟼0-𝟿𝟸')
    elif str(call.data)[18:] == "strategy":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟻0-𝟿𝟸')
    elif str(call.data)[18:] == "inter":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟹0-𝟼𝟽')
    elif str(call.data)[18:] == "it-dep":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟼𝟹-𝟾𝟽')
    elif str(call.data)[18:] == "marketing":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟺0-𝟾𝟽')
    elif str(call.data)[18:] == "deans":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟾0-𝟻𝟸')
    elif str(call.data)[18:] == "working-youth":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟹0-𝟽𝟹')
    elif str(call.data)[18:] == "irc":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟻0-𝟹𝟸')
    elif str(call.data)[18:] == "sport":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟻0-𝟽𝟿')
    elif str(call.data)[18:] == "medical":
        await call.message.answer('+𝟿𝟿𝟾(𝟽𝟷)𝟸𝟺𝟼-𝟹0-𝟽𝟹')
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_tel_num.filter(owner="back"))
async def back(call: CallbackQuery):
    await call.message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
