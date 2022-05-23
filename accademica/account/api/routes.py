from rest_framework import routers
from account.api.viewsets import AccountViewset

account_router = routers.SimpleRouter()
account_router.register(r'accounts', AccountViewset)