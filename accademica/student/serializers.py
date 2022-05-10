from rest_framework import serializers
from .models import Student, Grade
from school.serializers import ProgramSerializer, CourseSerializer

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grade
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True,read_only=True)
    class Meta:
        model=Student
        fields='__all__'