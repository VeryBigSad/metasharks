from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.
    """

    class Meta:
        model = Course
        fields = ("id", "name", "description", "curator", "created_at", "updated_at")
