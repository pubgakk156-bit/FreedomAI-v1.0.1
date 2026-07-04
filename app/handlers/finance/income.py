from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.finance_states import FinanceState
from app.services.user_service import UserService
from app.services.finance_service import FinanceService

router = Router()


@router.message(F.text == "➕ Доход")
async def income_start(
    message: Message,
    state: FSMContext
):
    await state.set_state(FinanceState.waiting_income)

    await message.answer(
        "💰 Введите сумму дохода:"
    )


@router.message(FinanceState.waiting_income)
async def income_save(
    message: Message,
    state: FSMContext
):
    text = message.text.strip()

    if not text.isdigit():
        await message.answer(
            "❌ Введите сумму цифрами."
        )
        return

    amount = int(text)

    user_id = UserService.get_or_create_user(
        message.from_user
    )

    FinanceService.add_income(
        user_id=user_id,
        amount=amount
    )

    await state.clear()

    await message.answer(
        f"✅ Доход {amount:,} ₽ успешно сохранён.".replace(",", " ")
    )