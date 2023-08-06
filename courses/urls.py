from django.urls import path

from courses.views import CourseDetailView, CourseListView


urlpatterns = [
    path("courses", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
]
