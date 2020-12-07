from django.contrib import admin
from django.urls import path, include

from games_info.api.views import GameInfo, app_ids
from games_info.front_end.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/game/', GameInfo.as_view(), name='api'),
    path('api/app_ids/', app_ids, name='api_app_ids'),
    path('', Index.as_view(), name='index')
]
