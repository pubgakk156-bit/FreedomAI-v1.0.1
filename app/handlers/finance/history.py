from aiogram import Router, F
from aiogram.types import Message

from app.services.finance_service import FinanceService
from app.services.user_service import UserService

router = Router()


@router.message(F.text == "📜 История")
async def history(message: Message):

    user_id = UserService.get_or_create_user(
        message.from_user
    )

    history = FinanceService.get_history(user_id)

    if not history:
        await message.answer(
            "📭 История пока пуста."
        )
        return

    text = "📜 Последние операции\n\n"

    for transaction_id, type_, amount, created_at in history:

        icon = "➕" if type_ == "income" else "➖"

        date = created_at.split(" ")[0]

        text += (
            "━━━━━━━━━━━━━━\n"
            f"🆔 #{transaction_id}\n\n"
            f"{icon} {'Доход' if type_ == 'income' else 'Расход'}\n"
            f"💰 {amount:,} ₽\n"
            f"📅 {date}\n"
        ).replace(",", " ")

    await message.answer(text)