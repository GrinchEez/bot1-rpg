from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import keyboards

from keyboards.keyboards import keys_main_menu
router = Router()
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Приветсвую, путник?, чего пожелаешь?",
        reply_markup=keys_main_menu()
    )
