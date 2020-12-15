from django.contrib import admin
from django.urls import path, include

from games_info.front_end.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('games_info.api.urls')),
    path('', Index.as_view(), name='index')
]
