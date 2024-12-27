from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def keys_main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text ="Магазин")
    kb.button(text ="Арена")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)