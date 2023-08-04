from rest_framework import serializers

from students.models import StudentGroup


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'


