from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cd_years = CallbackData("yyyy", "year")
keyboard_years = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2️⃣0️⃣2️⃣0️⃣", callback_data="yyyy:20"),
            InlineKeyboardButton(text="2️⃣0️⃣1️⃣9️⃣", callback_data="yyyy:19"),
            InlineKeyboardButton(text="2️⃣0️⃣1️⃣8️⃣", callback_data="yyyy:18"),
        ],
        [
            InlineKeyboardButton(text="𝙱𝚊𝚌𝚔 ⬅️", callback_data="yyyy:back")
        ],
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
            InlineKeyboardButton(text='𝙱𝚊𝚌𝚔 ⬅️', callback_data='cancel')
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
            InlineKeyboardButton(text='𝙱𝚊𝚌𝚔 ⬅️', callback_data='cancel')
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
            InlineKeyboardButton(text="𝚃𝙸𝙼𝙴𝚃𝙰𝙱𝙻𝙴 📋", callback_data="menu:timetable"),
            InlineKeyboardButton(text="𝙲𝙾𝚄𝚁𝚂𝙴 𝙲𝙰𝚃𝙰𝙻𝙾𝙶 📝", callback_data="menu:catalog"),
            InlineKeyboardButton(text="𝚃𝚄𝚁𝙸𝙽'𝚂 𝙲𝙾𝙽𝚃𝙰𝙲𝚃𝚂 📞", callback_data="menu:contacts"),

        ],
    ],
    resize_keyboard=True,
)

cd_tel_num = CallbackData("telephone_numbers", "owner")
tel_numbers_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="𝚁𝚎𝚌𝚝𝚘𝚛’𝚜 𝚛𝚎𝚌𝚎𝚙𝚝𝚒𝚘𝚗", callback_data="telephone_numbers:rector")],
        [InlineKeyboardButton(text="𝙵𝚒𝚗𝚊𝚗𝚌𝚒𝚊𝚕 𝚖𝚊𝚗𝚊𝚐𝚎𝚖𝚎𝚗𝚝 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:finance")],
        [InlineKeyboardButton(text="𝙰𝚌𝚌𝚘𝚞𝚗𝚝𝚒𝚗𝚐 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:accounting")],
        [InlineKeyboardButton(text="𝙷𝚁 𝚖𝚊𝚗𝚊𝚐𝚎𝚖𝚎𝚗𝚝 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:hr")],
        [InlineKeyboardButton(text="𝙿𝚘𝚜𝚝 𝚘𝚏𝚏𝚒𝚌𝚎", callback_data="telephone_numbers:post")],
        [InlineKeyboardButton(text="𝚂𝚝𝚛𝚊𝚝𝚎𝚐𝚒𝚌 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚖𝚎𝚗𝚝 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:strategy")],
        [InlineKeyboardButton(text="𝙸𝚗𝚝𝚎𝚛𝚗𝚊𝚝𝚒𝚘𝚗𝚊𝚕 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:inter")],
        [InlineKeyboardButton(text="𝙸𝚃-𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:it-dep")],
        [InlineKeyboardButton(text="𝙼𝚊𝚛𝚔𝚎𝚝𝚒𝚗𝚐 𝚍𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝", callback_data="telephone_numbers:marketing")],
        [InlineKeyboardButton(text="𝙳𝚎𝚊𝚗’𝚜 𝚘𝚏𝚏𝚒𝚌𝚎", callback_data="telephone_numbers:deans")],
        [InlineKeyboardButton(text="𝙳𝚎𝚙𝚊𝚛𝚝𝚖𝚎𝚗𝚝 𝚘𝚗 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝚠𝚒𝚝𝚑 𝚢𝚘𝚞𝚝𝚑", callback_data="telephone_numbers:working-youth")],
        [InlineKeyboardButton(text="𝙸𝚁𝙲 (𝚕𝚒𝚋𝚛𝚊𝚛𝚢)", callback_data="telephone_numbers:irc")],
        [InlineKeyboardButton(text="𝚂𝚙𝚘𝚛𝚝𝚜 𝚌𝚎𝚗𝚝𝚎𝚛", callback_data="telephone_numbers:sport")],
        [InlineKeyboardButton(text="𝙼𝚎𝚍𝚒𝚌𝚊𝚕 𝚌𝚎𝚗𝚝𝚎𝚛", callback_data="telephone_numbers:medical")],

        [InlineKeyboardButton(text="𝙱𝚊𝚌𝚔 ⬅️", callback_data="telephone_numbers:back")],
    ],
    resize_keyboard=True,
)

cd_course = CallbackData("c", "course")
course_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="𝙿𝚈", callback_data="c:py"),
            InlineKeyboardButton(text="𝟷-𝚂𝚃 𝙻𝚅𝙻", callback_data="c:first_lvl"),
        ],
        [
            InlineKeyboardButton(text="𝟸-𝙽𝙳 𝙻𝚅𝙻", callback_data="c:second_lvl"),
            InlineKeyboardButton(text="𝟹-𝚁𝙳 𝙻𝚅𝙻", callback_data="c:third_lvl"),
        ],
        [InlineKeyboardButton(text="𝙱𝚊𝚌𝚔 ⬅️", callback_data="c:back")]
    ],
    resize_keyboard=True,
)
