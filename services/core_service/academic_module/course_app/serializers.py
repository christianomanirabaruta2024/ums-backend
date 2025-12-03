from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source="module.module_name", read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "module",
            "module_name",
            "course_name",
            "cm",
            "td",
            "tp",
            "credits",
        ]
