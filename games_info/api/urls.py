from django.urls import path

from games_info.api.views import GameInfo, app_ids

app_name = 'api'
urlpatterns = [
    path('game/', GameInfo.as_view(), name='game'),
    path('app_ids/', app_ids, name='api_app_ids'),
]
