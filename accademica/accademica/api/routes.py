from rest_framework import routers
from accademica.api.viewsets import UserViewset, GroupViewset

accademica_router = routers.SimpleRouter()
accademica_router.register(r'users', UserViewset)
accademica_router.register(r'groups', GroupViewset)

class DefaultRouter(routers.DefaultRouter):
    def extend(self,router):
        self.registry.extend(router.registry)