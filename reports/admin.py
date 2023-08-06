from django.contrib import admin

from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "state", "created_at")
    list_filter = ("state", "created_at")
    search_fields = ("owner__username",)
    readonly_fields = ("state", "file", "created_at")
    fields = ("owner", "state", "file", "created_at")
