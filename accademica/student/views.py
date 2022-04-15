from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, GradeSerializer
from .models import Student, Grade

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

class GradeViewset(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer
    permission_classes=[permissions.IsAuthenticated]