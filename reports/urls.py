from django.urls import path

from reports.views import ReportDetailView, ReportListView


urlpatterns = [
    path("report/", ReportListView.as_view(), name="report-list"),
    path("report/<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
]
