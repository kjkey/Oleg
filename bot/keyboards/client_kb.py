from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class KBoards:
    b1 = KeyboardButton('/Fiction')
    b2 = KeyboardButton('/Publicism')
    b3 = KeyboardButton('/Diaries')
    b4 = KeyboardButton('/Letters')
    b5 = KeyboardButton('/Collected_Works')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

    kb_client.add(b1).add(b2).add(b3).add(b4).add(b5)
