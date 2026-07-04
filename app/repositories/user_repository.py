from app.database.database import get_connection


class UserRepository:

    @staticmethod
    def get_by_telegram_id(telegram_id: int):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE telegram_id=?",
            (telegram_id,)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    @staticmethod
    def create(
        telegram_id: int,
        first_name: str,
        username: str | None
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(
                telegram_id,
                first_name,
                username
            )
            VALUES(?,?,?)
            """,
            (
                telegram_id,
                first_name,
                username
            )
        )

        conn.commit()

        user_id = cursor.lastrowid

        conn.close()

        return user_id