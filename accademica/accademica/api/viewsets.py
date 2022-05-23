from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwarg):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        userSerialized = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': userSerialized.data
        })

class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def authenticated_user(self, request, *args, **kwargs):
        user = UserSerializer(request.user)
        return Response({
            'user': user.data
        })

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]