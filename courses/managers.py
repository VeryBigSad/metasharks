from django.db.models import F, Manager
from django.db.models.functions import Concat


class CoursesManager(Manager):
    def get_data_for_report(self):
        return (
            self.get_queryset()
            .annotate(
                curator_name=Concat(
                    F("curator__first_name"),
                    F("curator__last_name"),
                    F("curator__patronymic"),
                )
            )
            .values("name", "description", "curator_id", "curator_name")
        )
