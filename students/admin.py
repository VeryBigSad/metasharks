from django.contrib import admin

from students.models import StudentGroup


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    """
    Административная панель модели StudentGroup
    """

    list_display = ("name", "curator", "created_at", "updated_at")
    list_filter = ("curator",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"
