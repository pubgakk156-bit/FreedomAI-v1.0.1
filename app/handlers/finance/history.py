from aiogram import Router, F
from aiogram.types import Message

from app.services.finance_service import FinanceService
from app.services.user_service import UserService
from app.keyboards.history_keyboard import transaction_keyboard

router = Router()


@router.message(F.text == "📜 История")
async def history(message: Message):

    user_id = UserService.get_or_create_user(message.from_user)

    rows = FinanceService.get_history(user_id)

    if not rows:
        await message.answer("📭 История пуста")
        return

    for transaction_id, type_, amount, created_at in rows:

        icon = "➕" if type_ == "income" else "➖"
        title = "Доход" if type_ == "income" else "Расход"

        text = (
            "━━━━━━━━━━━━━━\n"
            f"🆔 #{transaction_id}\n\n"
            f"{icon} {title}\n"
            f"💰 {amount:,} ₽\n"
            f"📅 {created_at.split(' ')[0]}"
        ).replace(",", " ")

        await message.answer(
            text,
            reply_markup=transaction_keyboard(transaction_id)
        )