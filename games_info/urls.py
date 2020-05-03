from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games-api/', include('games_info.api.urls')),
    path('', include('games_info.games_viewer.urls'))
]
