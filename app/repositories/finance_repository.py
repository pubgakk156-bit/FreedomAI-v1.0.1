from app.database.database import get_connection


class FinanceRepository:

    @staticmethod
    def get_transaction(transaction_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, user_id, type, amount, created_at
            FROM transactions
            WHERE id=?
            """,
            (transaction_id,)
        )

        row = cursor.fetchone()

        conn.close()

        return row

    @staticmethod
    def update_amount(transaction_id: int, amount: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE transactions
            SET amount=?
            WHERE id=?
            """,
            (amount, transaction_id)
        )

        conn.commit()
        conn.close()

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

    @staticmethod
    def get_balance(user_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COALESCE(
                SUM(
                    CASE
                        WHEN type='income' THEN amount
                        ELSE -amount
                    END
                ),
                0
            )
            FROM transactions
            WHERE user_id=?
            """,
            (user_id,)
        )

        result = cursor.fetchone()[0]

        conn.close()

        return result

    @staticmethod
    def get_history(user_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, type, amount, created_at
            FROM transactions
            WHERE user_id=?
            ORDER BY id DESC
            LIMIT 10
            """,
            (user_id,)
        )

        rows = cursor.fetchall()

        conn.close()

        return rows