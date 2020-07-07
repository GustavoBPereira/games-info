from django.contrib import admin
from django.urls import path, include

from games_info.api.views import GameInfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games-api/', GameInfo.as_view()),
    path('', include('games_info.games_viewer.urls'))
]
