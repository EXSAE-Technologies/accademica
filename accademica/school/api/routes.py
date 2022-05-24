from rest_framework import routers
from school.api import viewsets

school_router = routers.SimpleRouter()
school_router.register(r'schools', viewsets.SchoolViewset)
school_router.register(r'programs', viewsets.ProgramViewset)
school_router.register(r'courses', viewsets.CourseViewset)
school_router.register(r'profiles', viewsets.ProfileViewset)