from django.urls import path

from users.views import StudentListView


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/<int:pk>/", StudentListView.as_view(), name="student-detail"),
]
