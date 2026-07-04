from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_keyboard import main_keyboard
from app.services.user_service import UserService

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    UserService.get_or_create_user(
        message.from_user
    )

    await message.answer(
        f"👋 Добро пожаловать, {message.from_user.first_name}!\n\n"
        "FreedomAI готов к работе.",
        reply_markup=main_keyboard
    )