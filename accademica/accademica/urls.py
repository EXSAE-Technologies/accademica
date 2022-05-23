"""latoh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from accademica.api.routes import DefaultRouter
from .views import CustomAuthToken, UserViewset, GroupViewset
from school.views import SchoolViewset, ProgramViewset, CourseViewset, ProfileViewset
from student.views import StudentViewset, GradeViewset
from account.api.routes import account_router

api_routes = DefaultRouter()
api_routes.register(r'users', UserViewset)
api_routes.register(r'groups', GroupViewset)
api_routes.register(r'schools', SchoolViewset)
api_routes.register(r'programs', ProgramViewset)
api_routes.register(r'courses', CourseViewset)
api_routes.register(r'students', StudentViewset)
api_routes.register(r'profiles', ProfileViewset)
api_routes.register(r'grades', GradeViewset)
api_routes.extend(account_router)
#api_routes.register(r'account', AccountViewset)

#for x in account_routes:
#    api_routes.register(x[0], x[1])

#api_routes.include_routes(account_routes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include(api_routes.urls))
]