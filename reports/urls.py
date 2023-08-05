from django.urls import path

from reports.views import ReportDetailView, ReportListView


urlpatterns = [
    path("report/", ReportListView.as_view(), name="report"),
    path("report/<int:pk>/", ReportDetailView.as_view(), name="report_detail"),
]
