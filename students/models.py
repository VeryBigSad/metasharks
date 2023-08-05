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
        "users.User",
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
        "users.User",
        verbose_name="Студенты",
        related_name="student_groups",
        blank=True,
        limit_choices_to={"user_type": "S"},
    )
    start_date = models.DateField(verbose_name="Дата начала обучения")
    end_date = models.DateField(verbose_name="Дата окончания обучения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
        ordering = ("name",)

        # validate only 20 students max
        constraints = [
            models.CheckConstraint(
                check=models.Q(students__count__lte=20),
                name="max_students_per_group",
            )
        ]
