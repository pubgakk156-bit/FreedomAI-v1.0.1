from app.database.database import get_connection


class FinanceRepository:

    @staticmethod
    def add_income(user_id: int, amount: int):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO transactions(
                user_id,
                type,
                amount
            )
            VALUES(?,?,?)
            """,
            (
                user_id,
                "income",
                amount
            )
        )

        conn.commit()
        conn.close()