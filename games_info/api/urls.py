from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from games_info.api.api.viewsets import GameViewSet

router = routers.DefaultRouter()
router.register('', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
