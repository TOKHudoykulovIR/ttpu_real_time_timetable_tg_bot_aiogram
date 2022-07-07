from aiogram import types
from aiogram.dispatcher.filters import Text
from main import dp
from keyboards import keyboard_years, keyboard_2020, keyboard_2019, keyboard_2018, cd_years, cd_2020, cd_2019, \
    menu_keyboard, tel_numbers_keyboard, course_keyboard, faculty_keyboard
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from parse_timetable import parse
import datetime
from sqlite import add_user, get_info
import os

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


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
    await message.answer('𝙲𝙷𝙾𝙾𝚂𝙴 𝚈𝙾𝚄𝚁 𝚈𝙴𝙰𝚁 𝙾𝙵 𝙰𝙳𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝚃𝙷𝙴 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙸𝚃𝚈...',
                         reply_markup=keyboard_years)


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


class FSMMenu(StatesGroup):
    menu_category_selection = State()
    course_catalog = State()
    tel_number = State()
    faculty_first_lvl = State()
    faculty_scnd_lvl = State()
    faculty_third_lvl = State()


@dp.message_handler(commands=['menu'], state="*")
async def menu(message: types.Message):
    await FSMMenu.menu_category_selection.set()
    await message.answer("choose category ↘︎", reply_markup=menu_keyboard)


@dp.message_handler(state=FSMMenu.menu_category_selection)
async def menu_categories(message: types.Message):
    if message.text == 'Course Catalog 📋':
        await message.answer('▷▷▷', reply_markup=course_keyboard)
        await FSMMenu.course_catalog.set()
    elif message.text == "Turin's Contacts 📞":
        await message.answer("▷▷▷", reply_markup=tel_numbers_keyboard)
        await FSMMenu.tel_number.set()


@dp.message_handler(state=FSMMenu.course_catalog)
async def course_catalog_btn(message: types.Message, state: FSMContext):
    if message.text == "Back ⬅️":
        await message.answer("▷▷▷", reply_markup=menu_keyboard)
        await FSMMenu.menu_category_selection.set()
    elif message.text == "PY":
        await message.answer("""
                №   Subject   Credits\n
1   Mathematics     ➓
2   Chemistry   ➒
3   Physics     ➑
4   Drawing     ➏
5   Computer science    ➎
6   English language (Technical)	➊➑
7   History of Uzbekistan   ➍
8   Constitution of Republic of Uzbekistan  ➋
9   Economics	➍
10  Russian Language	 
11  Physical training\n	 
Total   ➏➏
                """, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif message.text == "1-ST LEVEL":
        await message.answer("▷▷▷", reply_markup=faculty_keyboard)
        await FSMMenu.faculty_first_lvl.set()
    elif message.text == "2-ND LEVEL":
        await message.answer("▷▷▷", reply_markup=faculty_keyboard)
        await FSMMenu.faculty_scnd_lvl.set()
    elif message.text == "3-RD LEVEL":
        await message.answer("▷▷▷", reply_markup=faculty_keyboard)
        await FSMMenu.faculty_third_lvl.set()


@dp.message_handler(state=FSMMenu.faculty_first_lvl)
async def first_lvl_btn(message: types.Message, state: FSMContext):
    if message.text == "ME":
        print("me catalog 1st lvl")
        await message.answer("""
                №	    subjects    	credits\n
1	    chemistry 	    8️⃣
2	    math. analysis I    	🔟
3	    computer science	    8️⃣
4	    lin. algebra and geometry I 	6️⃣
5	    lin. algebra and geometry II	    4️⃣
6	    physics I	    🔟
7	    math. analysis II	    8️⃣
8	    engineering drawing 	6️⃣\n	 
🟰   6️⃣0️⃣
""",
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == "IT":
        print("it catalog 1st lvl")
        await message.answer("""
                 №	    subjects    	credits\n
1	    chemistry 	8️⃣
2	    mathematical analysis I	🔟
3	    computer science	8️⃣
4	    linear algebra and geometry I	6️⃣
5	    linear algebra and geometry II	4️⃣
6	    physics I	🔟
7	    mathematical analysis II	8️⃣
8	    algorithms and programming I	6️⃣\n
total   6️⃣0️⃣
""",
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == "CIE":
        print("cie faculty 1st lvl")
        await message.answer("""
                №	    subjects    	credits\n
1	    chemistry 	8️⃣
2	    mathematical analysis I 	🔟
3	    computer science 	8️⃣
4	    linear algebra and geometry I  	6️⃣
5	    linear algebra and geometry II 	4️⃣
6	    physics I 	🔟
7	    mathematical analysis II 	8️⃣
8	    drawing	 6️⃣\n
total   6️⃣0️⃣
""",
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=FSMMenu.faculty_scnd_lvl)
async def second_lvl_btn(message: types.Message, state: FSMContext):
    if message.text == "ME":
        print("me catalog 2nd lvl")
        await message.answer("""
                 №	    subjects    	credits\n
1       Physics II	6
2	    Fundam. of Eng. Thermodynamics and heat transfer	8
3	    Experimental Statistics and Mechanical Measurements	6
4	    Introduction to electrical engineering / Electrical machines	10
5	    Science & Technology of Materials (MEC)	5
6	    Technology of Metallic Materials	5
7   	Applied mechanics	10
8   	Fundamentals of strength of materials	8
total   6️⃣0️⃣""",
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == "IT":
        print("it catalog 2nd lvl")
        await message.answer("""
                №	    subjects    	credits\n
1       Physics II	6
9	 	Circuit Theory	8
10	 	Databases	8
11	 	Algorithms and Programming 2	6
12	 	Object-oriented programming	6
13	 	Electronic Systems and Technologies	10
14	 	Computer architectures	8
15	 	Mathematical methods A	4
16	 	Mathematical methods B	6
total   6️⃣0️⃣""",
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == "CIE":
        print("cie catalog 2nd lvl")
        await message.answer("""
                №	    subjects    	credits\n
1       Physics II	6
2	    Fundam. of Eng. Thermodynamics and heat transfer	8
17	 	Science & Technology of Materials (CIV)	6
18	 	Geology / Safety and civil protection 	8
19	    Analytical Mechanics 	8
20	    Statistical Methods for Engineering	4
21	    Structural Mechanics	12
22	    Land Surveying	8
total   6️⃣0️⃣""",
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=FSMMenu.tel_number)
async def turin_s_contacts_btn(message: types.Message, state: FSMContext):
    if message.text == "Back ⬅️":
        await message.answer("▷▷▷", reply_markup=menu_keyboard)
        await FSMMenu.menu_category_selection.set()
    elif message.text == "Rector’s reception":
        await message.answer("+998(71)246-70-82", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif message.text == "Financial management department":
        await message.answer("+998(71)246-10-25", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif message.text == "Accounting department":
        await message.answer("+998(71)246-20-79", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif message.text == "HR management department":
        await message.answer("+998(71)246-20-53", reply_markup=ReplyKeyboardRemove())
        await state.finish()
