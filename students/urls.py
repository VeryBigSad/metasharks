from django.urls import path

from students.views import AddStudentView, StudentGroupListView


urlpatterns = [
    path("student-groups", StudentGroupListView.as_view(), name="student-group-list"),
    path(
        "student-groups/<int:pk>",
        StudentGroupListView.as_view(),
        name="student-group-detail",
    ),
    path(
        "student-groups/<int:pk>/add-student/<int:student_id>",
        AddStudentView.as_view(),
        name="add-student",
    ),
]
