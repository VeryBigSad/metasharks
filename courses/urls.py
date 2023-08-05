from django.urls import path

from courses.views import CourseView


urlpatterns = [
    path("courses", CourseView.as_view(), name="courses"),
    path("courses/<int:pk>", CourseView.as_view(), name="course"),
]
