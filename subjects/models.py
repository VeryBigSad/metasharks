from django.db import models

class Subject(models.Model):
    """
    Модель предмета

    name str: Название предмета
    description text: Описание предмета
    created_at datetime: Дата создания
    updated_at datetime: Дата последнего обновления
    """
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
