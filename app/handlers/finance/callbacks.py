from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("edit:"))
async def edit_transaction(call: CallbackQuery):

    transaction_id = call.data.split(":")[1]

    await call.message.answer(
        f"✏️ Редактирование операции #{transaction_id}\n\n"
        "Функция будет добавлена в следующем спринте"
    )

    await call.answer()


@router.callback_query(F.data.startswith("delete:"))
async def delete_transaction(call: CallbackQuery):

    transaction_id = call.data.split(":")[1]

    await call.message.answer(
        f"🗑 Удаление операции #{transaction_id}\n\n"
        "Функция будет добавлена в следующем спринте"
    )

    await call.answer()