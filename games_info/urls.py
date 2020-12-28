from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('games_info.api.urls')),
    path('', include('games_info.front_end.urls')),
]
