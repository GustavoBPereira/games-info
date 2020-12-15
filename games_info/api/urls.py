from django.urls import path

from games_info.api.views import GameInfo, app_ids

urlpatterns = [
    path('game/', GameInfo.as_view(), name='api'),
    path('app_ids/', app_ids, name='api_app_ids'),
]
