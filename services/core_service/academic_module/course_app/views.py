from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by("course_name")
    serializer_class = CourseSerializer
