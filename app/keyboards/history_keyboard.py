from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def transaction_keyboard(transaction_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✏️ Изменить",
                    callback_data=f"edit:{transaction_id}"
                ),
                InlineKeyboardButton(
                    text="🗑 Удалить",
                    callback_data=f"delete:{transaction_id}"
                )
            ]
        ]
    )