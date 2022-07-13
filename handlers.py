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
    await message.answer("choose category ↘︎", reply_markup=menu_keyboard)


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
    await call.message.answer('catalog of subjects', reply_markup=course_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_menu.filter(category="contacts"))
async def contacts(call: CallbackQuery):
    await call.message.answer('turins contacts', reply_markup=tel_numbers_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)




@dp.callback_query_handler(cd_course.filter(course="py"))
async def py_catalog(call: CallbackQuery):
    await call.message.answer("""
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
                 """)
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_course.filter(course="first_lvl"))
async def first_lvl_catalog(call: CallbackQuery):
    await call.message.answer('choose faculty', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.first_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["second_lvl"]))
async def second_lvl_catalog(call: CallbackQuery):
    await call.message.answer('choose faculty', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.second_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["third_lvl"]))
async def third_lvl_catalog(call: CallbackQuery):
    await call.message.answer('choose faculty', reply_markup=faculty_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
    await FSMMenu.third_lvl.set()


@dp.callback_query_handler(cd_course.filter(course=["back"]))
async def third_lvl_catalog(call: CallbackQuery):
    await call.message.answer("choose category ↘︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)




@dp.callback_query_handler(cd_faculty.filter(faculty=["me"]), state=FSMMenu.first_lvl)
async def me_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
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
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.first_lvl)
async def it_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
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
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.first_lvl)
async def cie_first_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
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
""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="me"), state=FSMMenu.second_lvl)
async def me_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
               №         subjects    	credits\n
1️⃣      Physics II ➖   𝟲
2️⃣	    Fundam. of Eng. Thermodynamics and heat transfer    ➖   𝟴
3️⃣	    Experimental Statistics and Mechanical Measurements ➖   𝟲
4️⃣	    Introduction to electrical engineering / Electrical machines    ➖   𝟭𝟬
5️⃣	    Science & Technology of Materials (MEC) ➖    𝟱
6️⃣	    Technology of Metallic Materials    ➖   𝟱
7️⃣      Applied mechanics  ➖   𝟭𝟬
8️⃣      Fundamentals of strength of materials  ➖   𝟴
total   𝟲𝟮""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.second_lvl)
async def it_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                №	    subjects    	credits\n
1️⃣      Physics II ➖   𝟲
2️⃣	 	Circuit Theory  ➖   𝟴
3️⃣	 	Databases   ➖   𝟴
4️⃣	 	Algorithms and Programming 2    ➖   𝟲
5️⃣	 	Object-oriented programming ➖   𝟲
6️⃣	 	Electronic Systems and Technologies ➖   𝟭𝟬
7️⃣	 	Computer architectures  ➖   𝟴
8️⃣	 	Mathematical methods A	➖   𝟰
9️⃣	 	Mathematical methods B  ➖   𝟲
total   𝟲𝟮""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.second_lvl)
async def cie_second_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer("""
                №	    subjects    	credits\n
1️⃣      Physics II ➖   𝟲
2️⃣	    Fundam. of Eng. Thermodynamics and heat transfer    ➖   𝟴
3️⃣	 	Science & Technology of Materials (CIV) ➖   𝟲
4️⃣	 	Geology / Safety and civil protection   ➖   𝟴
5️⃣	    Analytical Mechanics    ➖   𝟴
6️⃣	    Statistical Methods for Engineering ➖   𝟰
7️⃣	    Structural Mechanics    ➖   𝟭𝟮
8️⃣	    Land Surveying  ➖   𝟴
total   𝟲𝟮""")
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty=["me"]), state=FSMMenu.third_lvl)
async def me_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be ME CAtaLOG for 3rd lvl')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="it"), state=FSMMenu.third_lvl)
async def it_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be IT CAtaLOG for 3rd lvl')
    await call.message.edit_reply_markup(reply_markup=None)
    await state.finish()


@dp.callback_query_handler(cd_faculty.filter(faculty="cie"), state=FSMMenu.third_lvl)
async def cie_third_catalog(call: CallbackQuery, state: FSMContext):
    await call.message.answer('here will be CIE CAtaLOG for 3rd lvl')
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


@dp.callback_query_handler(cd_tel_num.filter(owner="mediacal"))
async def med_contact(call: CallbackQuery):
    await call.message.answer('+998(71)246-30-73')
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(cd_tel_num.filter(owner="back"))
async def back(call: CallbackQuery):
    await call.message.answer("choose category ↘︎", reply_markup=menu_keyboard)
    await call.message.edit_reply_markup(reply_markup=None)
