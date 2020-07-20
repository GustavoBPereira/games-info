from django.contrib import admin
from django.urls import path, include

from games_info.api.views import GameInfo
from games_info.front_end.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games-api/', GameInfo.as_view(), name='api'),
    path('', Index.as_view(), name='index')
]
