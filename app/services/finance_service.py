from app.repositories.finance_repository import FinanceRepository


class FinanceService:

    @staticmethod
    def add_income(user_id: int, amount: int):
        FinanceRepository.add_income(user_id, amount)

    @staticmethod
    def add_expense(user_id: int, amount: int):
        FinanceRepository.add_expense(user_id, amount)

    @staticmethod
    def get_balance(user_id: int):
        return FinanceRepository.get_balance(user_id)

    @staticmethod
    def get_history(user_id: int, limit: int = 10):
        return FinanceRepository.get_history(user_id, limit)