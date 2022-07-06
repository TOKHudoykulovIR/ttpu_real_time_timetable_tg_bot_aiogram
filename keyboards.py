from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
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

keyboard_2018 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="𝙲𝙾𝙼𝙸𝙽𝙶 𝚂𝙾𝙾𝙽...", callback_data="cs"),
        ],
        [
            InlineKeyboardButton(text='𝙲𝙰𝙽𝙲𝙴𝙻', callback_data='cancel')
        ]
    ],
    resize_keyboard=True
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Course Catalog 📋"),
            KeyboardButton(text="Turin's Contacts 📞"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)

tel_numbers_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rector’s reception"),
            KeyboardButton(text="Financial management department"),
            KeyboardButton(text="Accounting department"),
            KeyboardButton(text="HR management department"),
        ],
        [
            KeyboardButton(text="Back ⬅️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)

course_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="PY"),
            KeyboardButton(text="1-ST LEVEL"),
            KeyboardButton(text="2-ND LEVEL"),
            KeyboardButton(text="3-RD LEVEL"),
        ],
        [
            KeyboardButton(text="Back ⬅️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)

