from users.models import User


def user_is_curator_valdator(user: User) -> bool:
    """Возвращает, является ли пользователь куратором.

    Args:
        user (User): модель пользователя

    Returns:
        bool: True, если пользователь куратор, иначе False
    """
    return user.user_type == "C"
