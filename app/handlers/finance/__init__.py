from aiogram import Router

from .menu import router as menu_router
from .income import router as income_router
from .expense import router as expense_router

router = Router()

router.include_router(menu_router)
router.include_router(income_router)
router.include_router(expense_router)