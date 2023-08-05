from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from reports.models import Report
from reports.serializers import ReportSerializer


class ReportListView(generics.ListCreateAPIView):
    """
    API endpoint that allows reports to be created or viewed.
    """

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]


class ReportDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows reports to be viewed or edited.
    """

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAdminUser]
