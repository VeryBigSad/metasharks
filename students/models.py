from django.db import models


class StudentGroup(models.Model):
    """
    Модель учебной группы

    name int: Название группы
    curator int: Куратор группы
    course int: Направление подготовки
    students m2m: Список студентов
    start_date date: Дата начала обучения
    end_date date: Дата окончания обучения
    created_at datetime: Дата создания
    updated_at datetime: Дата последнего обновления
    """

    name = models.CharField(max_length=50, verbose_name="Название")
    curator = models.ForeignKey(
        "courses.Curator",
        on_delete=models.SET_NULL,
        verbose_name="Куратор",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.SET_NULL,
        verbose_name="Направление подготовки",
        null=True,
        blank=True,
    )
    students = models.ManyToManyField(
        "students.Student",
        verbose_name="Студенты",
        related_name="student_groups",
        blank=True,
    )
    start_date = models.DateField(verbose_name="Дата начала обучения")
    end_date = models.DateField(verbose_name="Дата окончания обучения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
