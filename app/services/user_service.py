from app.repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def get_or_create_user(user):

        db_user = UserRepository.get_by_telegram_id(user.id)

        if db_user:
            return db_user[0]

        return UserRepository.create(
            telegram_id=user.id,
            first_name=user.first_name,
            username=user.username
        )