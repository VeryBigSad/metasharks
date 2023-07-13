from django.db import models


class StudentGroup(models.Model):
    """
    Модель учебной группы

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


class Student(models.Model):
    """
    Модель студента

    """

    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(
        max_length=1, choices=(("M", "Мужской"), ("F", "Женский")), verbose_name="Пол"
    )

    study_group = models.ForeignKey(
        "students.StudentGroup",
        on_delete=models.SET_NULL,
        verbose_name="Учебная группа",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ("last_name", "first_name", "patronymic")
