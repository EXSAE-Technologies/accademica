from django.contrib.auth.models import User, Group
from rest_framework import serializers
from student.api.serializers import StudentSerializer
from school.models import Profile
from school.api.serializers import ProfileSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False,read_only=True)
    groups = GroupSerializer(many=True,read_only=True)
    profile = ProfileSerializer(many=False,read_only=True)
    class Meta:
        model=User
        fields='__all__'
