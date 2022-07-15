from aiogram import types
from main import dp
from keyboards import keyboard_years, keyboard_2020, keyboard_2019, cd_years, cd_2020, cd_2019, \
    menu_keyboard, tel_numbers_keyboard, course_keyboard, faculty_keyboard, \
    cd_menu, cd_tel_num, cd_course, cd_faculty
from aiogram.types import CallbackQuery
from parse_timetable import parse
import datetime
from sqlite import add_user, get_info
import os
from aiogram.dispatcher import FSMContext
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


@dp.message_handler(commands=["admin"], state="*")
async def stats(message: types.Message):
    admin_id = os.getenv("admin_id")
    if int(message.from_user.id) == int(admin_id):
        await message.answer("Hi, boss")
        dataset = await (get_info())
        await message.answer(dataset)


#  > > >  BASE COMMANDS
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
    await message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...',
                         reply_markup=keyboard_years)


@dp.message_handler(commands=['menu'], state="*")
async def show_keyboard_categories(message: types.Message):
    user_id, user_name, user_text, time = data(message)
    await add_user(user_id, user_name, user_text, time)
    await message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈", reply_markup=menu_keyboard)


#  < < <


#  > > >  FILTER BY YEARS
@dp.callback_query_handler(cd_years.filter(year="20"), state="*")
async def year_20(call: CallbackQuery):
    await call.message.answer('𝟸𝟶𝟸𝟶 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
                              '‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›',
                              reply_markup=keyboard_2020)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_years.filter(year="19"), state="*")
async def year_19(call: CallbackQuery):
    await call.message.answer('𝟸𝟶𝟷𝟿 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
                              '‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›',
                              reply_markup=keyboard_2019)
    await call.message.edit_reply_markup(reply_markup=None)


# @dp.callback_query_handler(Text(equals='yyyy:18'))
# async def year_18(call: CallbackQuery):
#     await call.message.answer('𝟸𝟶𝟷𝟾 𝚈𝙴𝙰𝚁 𝙶𝚁𝙾𝚄𝙿𝚂\n'
#                               "‹𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚁𝙴𝙲𝙴𝙸𝚅𝙴 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁 𝚆𝙸𝚃𝙷𝙸𝙽 𝟷𝟶 𝚂𝙴𝙲𝙾𝙽𝙳𝚂⏱...›",
#                               reply_markup=keyboard_2018)
#     await call.message.edit_reply_markup(reply_markup=None)


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
    await call.message.answer('𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶🔎')
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


# <><><><><><><><><><><><><><><><>


# @dp.message_handler(commands=['menu'], state="*")
# async def menu(message: types.Message):
#     await message.answer("choose category ↘︎", reply_markup=menu_keyboard)



@dp.callback_query_handler(cd_menu.filter(category="catalog"))
async def catalog(call: CallbackQuery):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙻𝙴𝚅𝙴𝙻', reply_markup=course_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_menu.filter(category="contacts"))
async def contacts(call: CallbackQuery):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙾𝙽𝚃𝙰𝙲𝚃', reply_markup=tel_numbers_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)




@dp.callback_query_handler(cd_course.filter(course="py"))
async def py_catalog(call: CallbackQuery):
    await call.message.answer("""
                𝙽𝚘      𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣   𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚜   ➖   ⑩
2️⃣   𝚌𝚑𝚎𝚖𝚒𝚜𝚝𝚛𝚢 ➖   ⑨
3️⃣   𝚙𝚑𝚢𝚜𝚒𝚌𝚜   ➖  ⑧
4️⃣   𝚍𝚛𝚊𝚠𝚒𝚗𝚐   ➖  ⑥
5️⃣   𝚌𝚘𝚖𝚙𝚞𝚝𝚎𝚛 𝚜𝚌𝚒𝚎𝚗𝚌𝚎  ➖   ⑤
6️⃣   𝚎𝚗𝚐𝚕𝚒𝚜𝚑 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎 (𝚝𝚎𝚌𝚑𝚗𝚒𝚌𝚊𝚕)  ➖   ⑱
7️⃣   𝚑𝚒𝚜𝚝𝚘𝚛𝚢 𝚘𝚏 𝚞𝚣𝚋𝚎𝚔𝚒𝚜𝚝𝚊𝚗 ➖   ④
8️⃣   𝚌𝚘𝚗𝚜𝚝𝚒𝚝𝚞𝚝𝚒𝚘𝚗 𝚘𝚏 𝚛𝚎𝚙𝚞𝚋𝚕𝚒𝚌 𝚘𝚏 𝚞𝚣𝚋𝚎𝚔𝚒𝚜𝚝𝚊𝚗    ➖   ②
9️⃣   𝚎𝚌𝚘𝚗𝚘𝚖𝚒𝚌𝚜 ➖   ④
⏺   𝚛𝚞𝚜𝚜𝚒𝚊𝚗 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎
⏺   𝚙𝚑𝚢𝚜𝚒𝚌𝚊𝚕 𝚝𝚛𝚊𝚒𝚗𝚒𝚗𝚐\n
🟰   ⑥⑥
                 """)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_course.filter(course="first_lvl"))
async def first_lvl_catalog(call: CallbackQuery):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴︎ 𝙵𝙰𝙲𝚄𝙻𝚃𝚈', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.first_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["second_lvl"]))
async def second_lvl_catalog(call: CallbackQuery):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴︎ 𝙵𝙰𝙲𝚄𝙻𝚃𝚈', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.second_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["third_lvl"]))
async def third_lvl_catalog(call: CallbackQuery):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴︎ 𝙵𝙰𝙲𝚄𝙻𝚃𝚈', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.third_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["back"]))
async def back_catalog(call: CallbackQuery):
    await call.message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)




@dp.callback_query_handler(cd_faculty.filter(faculty=["me"]), state=FSMMenu.first_lvl)
async def me_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                𝙽𝚘      𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣	    𝚌𝚑𝚎𝚖𝚒𝚜𝚝𝚛𝚢   ➖   ⑧
2️⃣	    𝚖𝚊𝚝𝚑. 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸    ➖   ⑩
3️⃣	    𝚌𝚘𝚖𝚙𝚞𝚝𝚎𝚛 𝚜𝚌𝚒𝚎𝚗𝚌𝚎    ➖   ⑧
4️⃣	    𝚕𝚒𝚗. 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸 ➖   ⑥
5️⃣	    𝚕𝚒𝚗. 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸𝙸    ➖   ④
6️⃣	    𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝙸   ➖   ⑩
7️⃣	    𝚖𝚊𝚝𝚑. 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸𝙸   ➖   ⑧
8️⃣	    𝚎𝚗𝚐𝚒𝚗𝚎𝚎𝚛𝚒𝚗𝚐 𝚍𝚛𝚊𝚠𝚒𝚗𝚐 ➖   ⑥\n
🟰   ⑥⓪
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.first_lvl)
async def it_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                 𝙽𝚘     𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣	    𝚌𝚑𝚎𝚖𝚒𝚜𝚝𝚛𝚢   ➖   ⑧
2️⃣	    𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸 ➖   ⑩
3️⃣	    𝚌𝚘𝚖𝚙𝚞𝚝𝚎𝚛 𝚜𝚌𝚒𝚎𝚗𝚌𝚎    ➖   ⑧
4️⃣	    𝚕𝚒𝚗𝚎𝚊𝚛 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸   ➖   ⑥
5️⃣	    𝚕𝚒𝚗𝚎𝚊𝚛 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸𝙸  ➖   ④
6️⃣	    𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝙸   ➖   ⑩
7️⃣	    𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸𝙸    ➖   ⑧
8️⃣	    𝚊𝚕𝚐𝚘𝚛𝚒𝚝𝚑𝚖𝚜 𝚊𝚗𝚍 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚖𝚒𝚗𝚐 𝙸    ➖   ⑥\n
🟰   ⑥⓪
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.first_lvl)
async def cie_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                𝙽𝚘      𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣	    𝚌𝚑𝚎𝚖𝚒𝚜𝚝𝚛𝚢   ➖   ⑧
2️⃣	    𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸 ➖   ⑩
3️⃣	    𝚌𝚘𝚖𝚙𝚞𝚝𝚎𝚛 𝚜𝚌𝚒𝚎𝚗𝚌𝚎    ➖   ⑧
4️⃣	    𝚕𝚒𝚗𝚎𝚊𝚛 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸   ➖   ⑥
5️⃣	    𝚕𝚒𝚗𝚎𝚊𝚛 𝚊𝚕𝚐𝚎𝚋𝚛𝚊 𝚊𝚗𝚍 𝚐𝚎𝚘𝚖𝚎𝚝𝚛𝚢 𝙸𝙸  ➖   ④
6️⃣	    𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝙸   ➖   ⑩
7️⃣	    𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚊𝚗𝚊𝚕𝚢𝚜𝚒𝚜 𝙸𝙸    ➖   ⑧
8️⃣	    𝚍𝚛𝚊𝚠𝚒𝚗𝚐 ➖   ⑥\n
🟰   ⑥⓪
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="back"), state=FSMMenu.first_lvl)
async def back_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙻𝙴𝚅𝙴𝙻', reply_markup=course_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()



@dp.callback_query_handler(cd_faculty.filter(faculty="me"), state=FSMMenu.second_lvl)
async def me_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                 𝙽𝚘     𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣      𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝙸𝙸 ➖   ⑥
2️⃣	    𝚏𝚞𝚗𝚍𝚊𝚖. 𝚘𝚏 𝚎𝚗𝚐. 𝚝𝚑𝚎𝚛𝚖𝚘𝚍𝚢𝚗𝚊𝚖𝚒𝚌𝚜 𝚊𝚗𝚍 𝚑𝚎𝚊𝚝 𝚝𝚛𝚊𝚗𝚜𝚏𝚎𝚛    ➖   ⑧
3️⃣	    𝚎𝚡𝚙𝚎𝚛𝚒𝚖𝚎𝚗𝚝𝚊𝚕 𝚜𝚝𝚊𝚝𝚒𝚜𝚝𝚒𝚌𝚜 𝚊𝚗𝚍 𝚖𝚎𝚌𝚑𝚊𝚗𝚒𝚌𝚊𝚕 𝚖𝚎𝚊𝚜𝚞𝚛𝚎𝚖𝚎𝚗𝚝𝚜 ➖   ⑥
4️⃣	    𝚒𝚗𝚝𝚛𝚘𝚍𝚞𝚌𝚝𝚒𝚘𝚗 𝚝𝚘 𝚎𝚕𝚎𝚌𝚝𝚛𝚒𝚌𝚊𝚕 𝚎𝚗𝚐𝚒𝚗𝚎𝚎𝚛𝚒𝚗𝚐 / 𝚎𝚕𝚎𝚌𝚝𝚛𝚒𝚌𝚊𝚕 𝚖𝚊𝚌𝚑𝚒𝚗𝚎𝚜    ➖   ⑩
5️⃣	    𝚜𝚌𝚒𝚎𝚗𝚌𝚎 & 𝚝𝚎𝚌𝚑𝚗𝚘𝚕𝚘𝚐𝚢 𝚘𝚏 𝚖𝚊𝚝𝚎𝚛𝚒𝚊𝚕𝚜 (𝚖𝚎𝚌) ➖    ⑤
6️⃣	    𝚝𝚎𝚌𝚑𝚗𝚘𝚕𝚘𝚐𝚢 𝚘𝚏 𝚖𝚎𝚝𝚊𝚕𝚕𝚒𝚌 𝚖𝚊𝚝𝚎𝚛𝚒𝚊𝚕𝚜    ➖   ⑤
7️⃣      𝚊𝚙𝚙𝚕𝚒𝚎𝚍 𝚖𝚎𝚌𝚑𝚊𝚗𝚒𝚌𝚜  ➖   ⑩
8️⃣      f𝚞𝚗𝚍𝚊𝚖𝚎𝚗𝚝𝚊𝚕𝚜 𝚘𝚏 𝚜𝚝𝚛𝚎𝚗𝚐𝚝𝚑 𝚘𝚏 𝚖𝚊𝚝𝚎𝚛𝚒𝚊𝚕𝚜  ➖   ⑧
🟰   ⑤⑧""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.second_lvl)
async def it_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                 𝙽𝚘     𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣      𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝙸𝙸 ➖   ⑥
2️⃣	 	𝚌𝚒𝚛𝚌𝚞𝚒𝚝 𝚝𝚑𝚎𝚘𝚛𝚢  ➖   ⑧
3️⃣	 	𝚍𝚊𝚝𝚊𝚋𝚊𝚜𝚎𝚜   ➖   ⑧
4️⃣	 	𝚊𝚕𝚐𝚘𝚛𝚒𝚝𝚑𝚖𝚜 𝚊𝚗𝚍 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚖𝚒𝚗𝚐 𝙸𝙸    ➖   ⑥
5️⃣	 	𝚘𝚋𝚓𝚎𝚌𝚝-𝚘𝚛𝚒𝚎𝚗𝚝𝚎𝚍 𝚙𝚛𝚘𝚐𝚛𝚊𝚖𝚖𝚒𝚗𝚐 ➖   ⑥
6️⃣	 	𝚎𝚕𝚎𝚌𝚝𝚛𝚘𝚗𝚒𝚌 𝚜𝚢𝚜𝚝𝚎𝚖𝚜 𝚊𝚗𝚍 𝚝𝚎𝚌𝚑𝚗𝚘𝚕𝚘𝚐𝚒𝚎𝚜 ➖   ⑩
7️⃣	 	𝚌𝚘𝚖𝚙𝚞𝚝𝚎𝚛 𝚊𝚛𝚌𝚑𝚒𝚝𝚎𝚌𝚝𝚞𝚛𝚎𝚜  ➖   ⑧
8️⃣	 	𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 𝙰	➖   ④
9️⃣	 	𝚖𝚊𝚝𝚑𝚎𝚖𝚊𝚝𝚒𝚌𝚊𝚕 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 𝙱  ➖   ⑥
🟰   ⑥②""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.second_lvl)
async def cie_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                 𝙽𝚘     𝚜𝚞𝚋𝚓𝚎𝚌𝚝𝚜        𝚌𝚛𝚎𝚍𝚒𝚝𝚜\n
1️⃣      𝚙𝚑𝚢𝚜𝚒𝚌𝚜 𝚒𝚒 ➖   ⑥
2️⃣	    𝚏𝚞𝚗𝚍𝚊𝚖. 𝚘𝚏 𝚎𝚗𝚐. 𝚝𝚑𝚎𝚛𝚖𝚘𝚍𝚢𝚗𝚊𝚖𝚒𝚌𝚜 𝚊𝚗𝚍 𝚑𝚎𝚊𝚝 𝚝𝚛𝚊𝚗𝚜𝚏𝚎𝚛    ➖   ⑧
3️⃣	 	    𝚜𝚌𝚒𝚎𝚗𝚌𝚎 & 𝚝𝚎𝚌𝚑𝚗𝚘𝚕𝚘𝚐𝚢 𝚘𝚏 𝚖𝚊𝚝𝚎𝚛𝚒𝚊𝚕𝚜 (𝚌𝚒𝚟) ➖   ⑥
4️⃣	 	    𝚐𝚎𝚘𝚕𝚘𝚐𝚢 / 𝚜𝚊𝚏𝚎𝚝𝚢 𝚊𝚗𝚍 𝚌𝚒𝚟𝚒𝚕 𝚙𝚛𝚘𝚝𝚎𝚌𝚝𝚒𝚘𝚗   ➖   ⑧
5️⃣	    𝚊𝚗𝚊𝚕𝚢𝚝𝚒𝚌𝚊𝚕 𝚖𝚎𝚌𝚑𝚊𝚗𝚒𝚌𝚜    ➖   ⑧
6️⃣	    𝚜𝚝𝚊𝚝𝚒𝚜𝚝𝚒𝚌𝚊𝚕 𝚖𝚎𝚝𝚑𝚘𝚍𝚜 𝚏𝚘𝚛 𝚎𝚗𝚐𝚒𝚗𝚎𝚎𝚛𝚒𝚗𝚐 ➖   ④
7️⃣	    𝚜𝚝𝚛𝚞𝚌𝚝𝚞𝚛𝚊𝚕 𝚖𝚎𝚌𝚑𝚊𝚗𝚒𝚌𝚜    ➖   ⑫
8️⃣	    𝚕𝚊𝚗𝚍 𝚜𝚞𝚛𝚟𝚎𝚢𝚒𝚗𝚐  ➖   ⑧
🟰   ⑤⓪""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()

@dp.callback_query_handler(cd_faculty.filter(faculty="back"), state=FSMMenu.second_lvl)
async def back_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙻𝙴𝚅𝙴𝙻', reply_markup=course_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()



@dp.callback_query_handler(cd_faculty.filter(faculty=["me"]), state=FSMMenu.third_lvl)
async def me_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be ME catalog for 3rd lvl')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.third_lvl)
async def it_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be IT catalog for 3rd lvl')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.third_lvl)
async def cie_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be CIE catalog for 3rd lvl')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="back"), state=FSMMenu.third_lvl)
async def back_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝙻𝙴𝚅𝙴𝙻', reply_markup=course_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()




@dp.callback_query_handler(cd_tel_num.filter(owner="rector"))
async def rector_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-70-82')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="finance"))
async def finance_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-10-25')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="accounting"))
async def accountant_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-20-79')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="hr"))
async def hr_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-20-53')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="post"))
async def post_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-60-92')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="strategy"))
async def strategy_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-50-92')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="inter"))
async def inter_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-30-67')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="it-dep"))
async def it_dep_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-63-87')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="marketing"))
async def marketing_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-40-87')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="deans"))
async def deans_contacts(call: CallbackQuery):
    await call.message.answer('+998(71)246-80-52')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="working-youth"))
async def working_youth_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-30-73')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="irc"))
async def irc_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-50-32')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="sport"))
async def sport_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-50-79')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="medical"))
async def med_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-30-73')
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(cd_tel_num.filter(owner="back"))
async def back(call: CallbackQuery):
    await call.message.answer("𝙲𝙷𝙾𝙾𝚂𝙴 𝙲𝙰𝚃𝙴𝙶𝙾𝚁𝚈︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
