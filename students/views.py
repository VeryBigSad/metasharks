from rest_framework import generics

from students.models import StudentGroup
from students.permissions import IsCuratorOrReadOnly
from students.serializers import StudentGroupSerializer


class StudentGroupListView(generics.ListCreateAPIView):
    """
        CRUD view for StudentGroup model.
    """
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsCuratorOrReadOnly,)

