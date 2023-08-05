from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from metasharks.permissions import IsCuratorOrAdminOrReadOnly

from students.models import StudentGroup
from students.serializers import StudentGroupSerializer
from users.models import User


class StudentGroupListView(generics.RetrieveUpdateDestroyAPIView):
    """
    CRUD view for StudentGroup model.
    """

    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsCuratorOrAdminOrReadOnly,)


class AddStudentView(generics.GenericAPIView):
    """View to add a student to a StudentGroup."""

    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer

    def post(self, request, *args, **kwargs):
        # url = studentgroups/<int:pk>/add-student/<int:student_id>
        student_id = self.kwargs.get("student_id")
        try:
            student = User.objects.get(id=student_id, user_type="S")
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student_group = self.get_object()
        student_group.students.add(student)
        return Response(status=status.HTTP_200_OK)
