from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_name() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    ib1 = InlineKeyboardButton('⬅️ Главное меню', callback_data="main")
    ikb.add(ib1)
    return ikb
