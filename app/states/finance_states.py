from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class FinanceState(StatesGroup):

    waiting_income = State()