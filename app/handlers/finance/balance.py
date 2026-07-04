from aiogram import Router
from aiogram import F
from aiogram.types import Message

from app.services.user_service import UserService
from app.services.finance_service import FinanceService

router = Router()


@router.message(F.text == "📊 Баланс")
async def balance(message: Message):

    user_id = UserService.get_or_create_user(
        message.from_user
    )

    balance = FinanceService.get_balance(user_id)

    await message.answer(
        f"💰 Текущий баланс:\n\n{balance:,} ₽".replace(",", " ")
    )