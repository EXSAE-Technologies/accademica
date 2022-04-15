from rest_framework import viewsets, permissions
from .serializers import SchoolSerializer, ProgramSerializer, CourseSerializer, ProfileSerializer
from .models import School, Program, Course, Profile

class SchoolViewset(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    permission_classes=[permissions.IsAuthenticated]

class ProgramViewset(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=ProgramSerializer
    permission_classes=[permissions.IsAuthenticated]

class CourseViewset(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[permissions.IsAuthenticated]

class ProfileViewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAuthenticated]