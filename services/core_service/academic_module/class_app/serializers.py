from rest_framework import serializers

from .models import Class, ClassGroup


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class ClassGroupSerializer(serializers.ModelSerializer):
    class_fk_detail = ClassSerializer(source="class_fk", read_only=True)

    class Meta:
        model = ClassGroup
        fields = "__all__"
