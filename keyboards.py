from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton
from aiogram.utils.callback_data import CallbackData

cd_years = CallbackData("yyyy", "year")
keyboard_years = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2️⃣0️⃣2️⃣0️⃣", callback_data="yyyy:20"),
            InlineKeyboardButton(text="2️⃣0️⃣1️⃣9️⃣", callback_data="yyyy:19"),
            InlineKeyboardButton(text="2️⃣0️⃣1️⃣8️⃣", callback_data="yyyy:18"),
        ]
    ],
    resize_keyboard=True
)

cd_2020 = CallbackData("20", "group")
keyboard_2020 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1.ME1-2-20", callback_data="20:1.ME1-2-20"),
            InlineKeyboardButton(text="1.ME3-4-20", callback_data="20:1.ME3-4-20"),
        ],
        [
            InlineKeyboardButton(text="1CIE1-2-20", callback_data="20:1CIE1-2-20"),
        ],
        [
            InlineKeyboardButton(text="1IT1-20", callback_data="20:1IT1-20"),
            InlineKeyboardButton(text="1IT2-20", callback_data="20:1IT2-20"),
            InlineKeyboardButton(text="1IT3-20", callback_data="20:1IT3-20"),
            InlineKeyboardButton(text="1IT4-20", callback_data="20:1IT4-20"),
        ],
        [
            InlineKeyboardButton(text="1IT5-20", callback_data="20:1IT5-20"),
            InlineKeyboardButton(text="1IT6-20", callback_data="20:1IT6-20"),
            InlineKeyboardButton(text="1IT7-20", callback_data="20:1IT7-20"),
        ],
        [
            InlineKeyboardButton(text='𝙲𝙰𝙽𝙲𝙴𝙻', callback_data='cancel')
        ]
    ],
    resize_keyboard=True
)

cd_2019 = CallbackData("19", "group")
keyboard_2019 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2.ME1-19", callback_data="19:2.ME1-19"),
            InlineKeyboardButton(text="2.ME2-19", callback_data="19:2.ME2-19"),
            InlineKeyboardButton(text="2.ME3-19", callback_data="19:2.ME3-19"),
        ],
        [
            InlineKeyboardButton(text="2.ME4-19", callback_data="19:2.ME4-19"),
            InlineKeyboardButton(text="2.ME5-19", callback_data="19:2.ME5-19"),
            InlineKeyboardButton(text="2.ME6-19", callback_data="19:2.ME6-19"),
        ],
        [
            InlineKeyboardButton(text="2CIE1-19", callback_data="19:2CIE1-19"),
            InlineKeyboardButton(text="2CIE2-19", callback_data="19:2CIE2-19"),
        ],
        [
            InlineKeyboardButton(text="2IT1-19", callback_data="19:2IT1-19"),
            InlineKeyboardButton(text="2IT2-19", callback_data="19:2IT2-19"),
            InlineKeyboardButton(text="2IT3-19", callback_data="19:2IT3-19"),
        ],
        [
            InlineKeyboardButton(text="2IT4-19", callback_data="19:2IT4-19"),
            InlineKeyboardButton(text="2IT5-19", callback_data="19:2IT5-19"),
            InlineKeyboardButton(text="2IT6-19", callback_data="19:2IT6-19"),
        ],
        [
            InlineKeyboardButton(text='𝙲𝙰𝙽𝙲𝙴𝙻', callback_data='cancel')
        ]
    ],
    resize_keyboard=True
)

# keyboard_2018 = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="𝙲𝙾𝙼𝙸𝙽𝙶 𝚂𝙾𝙾𝙽...", callback_data="cs")],
#         [InlineKeyboardButton(text='𝙲𝙰𝙽𝙲𝙴𝙻', callback_data='cancel')]
#     ],
#     resize_keyboard=True
# )

cd_menu = CallbackData("menu", "category")
menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Course Catalog 📋", callback_data="menu:catalog"),
            InlineKeyboardButton(text="Turin's Contacts 📞", callback_data="menu:contacts")
        ],
    ],
    resize_keyboard=True,
)

cd_tel_num = CallbackData("telephone_numbers", "owner")
tel_numbers_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Rector’s reception", callback_data="telephone_numbers:rector")],
        [InlineKeyboardButton(text="Financial management department", callback_data="telephone_numbers:finance")],
        [InlineKeyboardButton(text="Accounting department", callback_data="telephone_numbers:accounting")],
        [InlineKeyboardButton(text="HR management department", callback_data="telephone_numbers:hr")],
        [InlineKeyboardButton(text="Back ⬅️", callback_data="telephone_numbers:back")],
    ],
    resize_keyboard=True,
)

cd_course = CallbackData("c", "course")
course_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="PY", callback_data="c:py")],
        [
            InlineKeyboardButton(text="1-ST LVL", callback_data="c:first_lvl"),
            InlineKeyboardButton(text="2-ND LVL", callback_data="c:second_lvl"),
            InlineKeyboardButton(text="3-RD LVL", callback_data="c:third_lvl"),
        ],
        [InlineKeyboardButton(text="Back ⬅️", callback_data="c:back")]
    ],
    resize_keyboard=True,
)

cd_faculty = CallbackData("f", "faculty")
faculty_keyboard = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text="ME", callback_data="f:me"),
            InlineKeyboardButton(text="CIE", callback_data="f:cie"),
            InlineKeyboardButton(text="IT", callback_data="f:it")
        ],
        [InlineKeyboardButton(text="Back ⬅️")]
    ],
    resize_keyboard=True,
)

