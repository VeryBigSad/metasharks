from django.db import models
from django.db.models import F, Q, Count
from rest_framework.generics import QuerySet


class StudentGroupManager(models.Manager):
    def get_data_for_students_report(self) -> QuerySet:
        """Get data for students report

        Returns:
            QuerySet: QuerySet of students data
        """
        return self.get_queryset().annotate(
            male_count=Count(
                "students",
                filter=Q(
                    students__gender="M",
                ),
            ),
            female_count=Count(
                "students",
                filter=Q(
                    students__gender="F",
                ),
            ),
            places_left=20 - F("male_count") - F("female_count"),
        )
