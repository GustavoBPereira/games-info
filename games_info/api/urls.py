from django.urls import path

from games_info.api.views import GameInfo, AppIds

app_name = 'api'
urlpatterns = [
    path('game/', GameInfo.as_view(), name='game'),
    path('app_ids/', AppIds.as_view(), name='api_app_ids'),
]
