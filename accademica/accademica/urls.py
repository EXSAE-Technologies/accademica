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
from .api.routes import DefaultRouter, accademica_router
from .api.viewsets import CustomAuthToken
from student.api.routes import student_router
from school.api.routes import school_router
from account.api.routes import account_router

api_routes = DefaultRouter()
api_routes.extend(accademica_router)
api_routes.extend(school_router)
api_routes.extend(account_router)
api_routes.extend(student_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include(api_routes.urls))
]