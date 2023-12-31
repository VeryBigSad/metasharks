from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from metasharks.permissions import IsCuratorOrAdminOrReadOnly

from students.models import StudentGroup
from students.serializers import StudentGroupSerializer
from users.models import User


class StudentGroupListView(generics.ListCreateAPIView):
    """
    List view for StudentGroup model.
    """

    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsCuratorOrAdminOrReadOnly,)


class StudentGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
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
    permission_classes = (IsCuratorOrAdminOrReadOnly,)

    def post(self, request, *args, **kwargs):
        student_id = self.kwargs.get("student_id")
        try:
            student = User.objects.get(id=student_id, user_type="S")
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student_group = self.get_object()
        # if more > 20 students in group, return 400
        if student_group.students.count() >= 20:
            return Response(
                {"detail": "This group already has 20 students"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        student_group.students.add(student)
        return Response(status=status.HTTP_200_OK)
