from rest_framework import viewsets, permissions
from student.api.serializers import StudentSerializer, GradeSerializer
from student.models import Student, Grade

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

class GradeViewset(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]