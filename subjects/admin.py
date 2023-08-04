from django.contrib import admin

from subjects.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Административная панель модели Subject
    """

    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    empty_value_display = "-пусто-"
