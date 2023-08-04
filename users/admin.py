from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Административная панель модели User
    """

    list_display = (
        "username",
        "first_name",
        "last_name",
        "user_type",
        "created_at",
        "updated_at",
    )
    list_filter = ("user_type",)
    search_fields = ("username", "first_name", "last_name")
    empty_value_display = "-пусто-"
