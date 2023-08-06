from django.urls import path

from subjects.views import SubjectDetailView, SubjectListView


urlpatterns = [
    path("subjects/", SubjectListView.as_view(), name="subject-list"),
    path("subjects/<int:pk>/", SubjectDetailView.as_view(), name="subject-detail"),
]
