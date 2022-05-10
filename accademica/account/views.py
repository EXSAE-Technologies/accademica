from rest_framework import viewsets, permissions
from .serializers import AccountSerializer
from .models import Account

class AccountViewset(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    permission_classes=[permissions.IsAuthenticated]
    