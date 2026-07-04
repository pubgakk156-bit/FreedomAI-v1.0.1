from app.database.database import get_connection


class FinanceRepository:

    # -------------------------
    # INCOME
    # -------------------------
    @staticmethod
    def add_income(user_id: int, amount: int):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO transactions(user_id, type, amount)
            VALUES (?, ?, ?)
            """,
            (user_id, "income", amount)
        )

        conn.commit()
        conn.close()

    # -------------------------
    # EXPENSE
    # -------------------------
    @staticmethod
    def add_expense(user_id: int, amount: int):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO transactions(user_id, type, amount)
            VALUES (?, ?, ?)
            """,
            (user_id, "expense", amount)
        )

        conn.commit()
        conn.close()

    # -------------------------
    # BALANCE
    # -------------------------
    @staticmethod
    def get_balance(user_id: int):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(
                CASE
                    WHEN type = 'income' THEN amount
                    ELSE -amount
                END
            ), 0)
            FROM transactions
            WHERE user_id = ?
        """, (user_id,))

        result = cursor.fetchone()[0]

        conn.close()
        return result