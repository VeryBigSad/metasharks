from django.db import models


class Report(models.Model):
    STATES = (
        ("in_progress", "В процессе"),
        ("done", "Завершен"),
        ("error", "Что-то пошло не так"),
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        verbose_name="Владелец",
        limit_choices_to={"user_type": "A"},
    )

    state = models.CharField(
        max_length=50, verbose_name="Статус", choices=STATES, default="in_progress"
    )
    file = models.FileField(
        upload_to="reports/",
        verbose_name="Файл",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
        ordering = ("-created_at",)
