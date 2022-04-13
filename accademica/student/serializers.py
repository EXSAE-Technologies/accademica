from rest_framework import serializers
from .models import Student
from school.serializers import ProgramSerializer

class StudentSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(many=False)
    class Meta:
        model=Student
        fields='__all__'
