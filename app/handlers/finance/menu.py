from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.finance_keyboard import finance_keyboard
from app.keyboards.main_keyboard import main_keyboard

router = Router()


@router.message(F.text == "💰 Финансы")
async def finance_menu(message: Message):
    await message.answer(
        "💰 Финансовый центр",
        reply_markup=finance_keyboard
    )


@router.message(F.text == "⬅️ Назад")
async def back(message: Message):
    await message.answer(
        "🏠 Главное меню",
        reply_markup=main_keyboard
    )