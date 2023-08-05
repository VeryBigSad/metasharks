from rest_framework import generics

from students.permissions import IsCuratorOrAdminOrReadOnly
from users.models import Student
from users.serializers import StudentSerializer


class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorOrAdminOrReadOnly]
