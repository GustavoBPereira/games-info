from django.urls import path

from games_info.api.views import game_api


urlpatterns = [
    path('', game_api, name='game_api'),
]