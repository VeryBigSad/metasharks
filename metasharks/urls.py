from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("students/", include("students.urls")),
    path("courses/", include("courses.urls")),
    path("reports/", include("reports.urls")),
]
