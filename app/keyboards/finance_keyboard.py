from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

finance_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Доход"),
            KeyboardButton(text="➖ Расход"),
        ],
        [
            KeyboardButton(text="📊 Баланс"),
            KeyboardButton(text="📜 История"),
        ],
        [
            KeyboardButton(text="⬅️ Назад"),
        ],
    ],
    resize_keyboard=True
)