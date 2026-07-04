from app.repositories.finance_repository import FinanceRepository


class FinanceService:

    @staticmethod
    def add_income(
        user_id: int,
        amount: int
    ):
        FinanceRepository.add_income(
            user_id=user_id,
            amount=amount
        )