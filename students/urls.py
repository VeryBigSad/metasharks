from django.urls import path

from students.views import StudentGroupListView


urlpatterns = [
    path("student-groups", StudentGroupListView.as_view(), name="student-group-list"),
]
