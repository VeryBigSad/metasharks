from typing import Union
from django.contrib.auth.models import User as OriginalUserModel
from django.db import models


class User(OriginalUserModel):
    """
    Модель пользователя, наследованная от модели пользователя Django

    user_type str: Тип пользователя
    patronymic str: Отчество
    date_of_birth date: Дата рождения
    gender str: Пол
    study_group m2one: Учебная группа
    updated_at datetime: Дата последнего обновления
    """

    USER_TYPES = (
        ("S", "Студент"),
        ("C", "Куратор"),
        ("A", "Администратор"),
    )

    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPES,
        verbose_name="Тип пользователя",
    )

    patronymic = models.CharField(max_length=50, verbose_name="Отчество", null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(
        max_length=1, choices=(("M", "Мужской"), ("F", "Женский")), verbose_name="Пол"
    )

    # only for students
    study_group = models.ForeignKey(
        "students.StudentGroup",
        on_delete=models.SET_NULL,
        verbose_name="Учебная группа",
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def get_specifics_or_none(self) -> Union[Student, Curator, None]:
        """
        Возвращает специфичные данные пользователя или None

        Returns:
            [Student, Curator, None]: Специфичные данные пользователя

        """

        try:
            if self.user_type == "S":
                return self.student
            elif self.user_type == "C":
                return self.curator
            else:
                return None
        except (Student.DoesNotExist, Curator.DoesNotExist):
            return None
    
    @property
    def is_student(self) -> bool:
        """
        Возвращает True, если пользователь - студент
        """
        return self.user_type == "S"

    @property
    def is_curator(self) -> bool:
        """
        Возвращает True, если пользователь - куратор
        """
        return self.user_type == "C"
    
    @property
    def is_admin(self) -> bool:
        """
        Возвращает True, если пользователь - администратор
        """
        return self.user_type == "A"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("last_name", "first_name", "patronymic")



class Student(models.Model):
    """
    Модель студента

    study_group m2one: Учебная группа
    """    

    study_group = models.ForeignKey(
        "students.StudentGroup",
        on_delete=models.SET_NULL,
        verbose_name="Учебная группа",
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        primary_key=True,
    )

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.user.patronymic}"


class Curator(models.Model):
    """
    Модель куратора

    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        primary_key=True,
    )

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.user.patronymic}"
