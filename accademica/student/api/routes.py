from rest_framework import routers
from student.api import viewsets

student_router = routers.SimpleRouter()
student_router.register(r'students', viewsets.StudentViewset)
student_router.register(r'grades', viewsets.GradeViewset)