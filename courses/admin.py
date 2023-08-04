from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class CouseAdmin(admin.ModelAdmin):
    """
    Административная панель модели Course
    """

    list_display = ("name", "curator", "created_at", "updated_at")
    list_filter = ("curator",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"
