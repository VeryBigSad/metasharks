from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import User


class UserManager(BaseUserManager):
    def get_data_for_report(self) -> QuerySet:
        """Get data for report

        Returns:
            QuerySet: QuerySet of students data
        """
        return self.get_queryset().values(
            "id",
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "date_of_birth",
            "gender",
        )

    def create_user(self, email: str, password: str, **extra_fields) -> "User":
        """Create and save a User with the given email and password.

        Args:
            email (str): User email
            password (str): User password

        Returns:
            User: User model
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        """Create and save a SuperUser with the given email and password.

        Args:
            email (str): User email
            password (str): User password

        Returns:
            User: User model
        """
        extra_fields.setdefault("user_type", "A")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("user_type") != "A":
            raise ValueError("Superuser must have user_type=A.")

        return self.create_user(email, password, **extra_fields)
