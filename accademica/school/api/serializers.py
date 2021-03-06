from rest_framework import serializers
from school.models import School, Program, Course, Profile

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class ProgramSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True,read_only=True)
    class Meta:
        model=Program
        fields='__all__'

class SchoolSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True,read_only=True)
    class Meta:
        model=School
        fields='__all__'
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
