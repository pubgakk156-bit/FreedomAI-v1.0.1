from app.database.database import get_connection


class FinanceRepository:

    @staticmethod
    def add_income(user_id: int, amount: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO transactions(user_id, type, amount) VALUES (?, ?, ?)",
            (user_id, "income", amount)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def add_expense(user_id: int, amount: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO transactions(user_id, type, amount) VALUES (?, ?, ?)",
            (user_id, "expense", amount)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def get_balance(user_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(
                CASE
                    WHEN type='income' THEN amount
                    ELSE -amount
                END
            ), 0)
            FROM transactions
            WHERE user_id=?
        """, (user_id,))

        return cursor.fetchone()[0]

    @staticmethod
    def get_history(user_id: int, limit: int = 10):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT type, amount, created_at
            FROM transactions
            WHERE user_id=?
            ORDER BY id DESC
            LIMIT ?
        """, (user_id, limit))

        rows = cursor.fetchall()
        conn.close()

        return rows