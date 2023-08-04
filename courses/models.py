from django.db import models

from courses.validators import user_is_curator_valdator


class Course(models.Model):
    """
    Модель направления подготовки

    name str: Название направления подготовки
    description text: Описание направления подготовки
    created_at datetime: Дата создания
    updated_at datetime: Дата последнего обновления
    """

    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    curator = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        verbose_name="Куратор",
        validators=user_is_curator_valdator,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"
