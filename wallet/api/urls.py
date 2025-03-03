from django.urls import include, path
from rest_framework import routers

from api.views import WalletViewSet


app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'wallets', WalletViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
