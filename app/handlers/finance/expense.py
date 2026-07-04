from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.finance_states import FinanceState
from app.services.finance_service import FinanceService
from app.services.user_service import UserService

router = Router()


# -------------------------
# START EXPENSE
# -------------------------
@router.message(F.text == "➖ Расход")
async def expense_start(message: Message, state: FSMContext):

    await state.set_state(FinanceState.waiting_expense_amount)

    await message.answer("💸 Введите сумму расхода:")


# -------------------------
# SAVE EXPENSE
# -------------------------
@router.message(FinanceState.waiting_expense_amount)
async def expense_save(message: Message, state: FSMContext):

    text = message.text.strip()

    if not text.isdigit():
        await message.answer("❌ Введите сумму цифрами.")
        return

    amount = int(text)

    user_id = UserService.get_or_create_user(message.from_user)

    FinanceService.add_expense(user_id, amount)

    balance = FinanceService.get_balance(user_id)

    await state.clear()

    await message.answer(
        f"❌ Расход {amount} ₽ сохранён\n💰 Баланс: {balance} ₽"
    )