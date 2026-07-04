import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from app.config import BOT_TOKEN
from app.database.database import create_database

from app.handlers.start import router as start_router
from app.handlers.finance import router as finance_router


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


async def main():

    create_database()

    dp.include_router(start_router)
    dp.include_router(finance_router)

    print()

    print("=" * 45)
    print(" FreedomAI v1.0.1")
    print("=" * 45)

    print("✓ Database connected")
    print("✓ Routers loaded")
    print("✓ Bot started")

    print("=" * 45)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())