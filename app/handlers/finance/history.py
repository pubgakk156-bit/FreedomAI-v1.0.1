from aiogram import Router, F
from aiogram.types import Message

from app.services.finance_service import FinanceService
from app.services.user_service import UserService

router = Router()


@router.message(F.text == "📜 История")
async def history(message: Message):

    user_id = UserService.get_or_create_user(message.from_user)

    rows = FinanceService.get_history(user_id)

    if not rows:
        await message.answer("📭 История пуста")
        return

    text = "📜 Последние операции:\n\n"

    for t, amount, date in rows:

        icon = "➕" if t == "income" else "➖"

        text += f"{icon} {amount} ₽ | {date}\n"

    await message.answer(text)