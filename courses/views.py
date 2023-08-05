from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer
from metasharks.permissions import IsAdminOrReadOnly


class CourseView(generics.RetrieveUpdateDestroyAPIView):
    """
    CRUD view for Course model.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAdminOrReadOnly,)
