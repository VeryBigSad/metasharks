from django.db import models
from django.db.models.query import QuerySet


class UserManager(models.Manager):
    def get_data_for_students_report(self) -> QuerySet:
        """Get data for students report

        Returns:
            QuerySet: QuerySet of students data
        """
        return self.get_queryset().only(
            "id",
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "date_of_birth",
            "gender",
        )
