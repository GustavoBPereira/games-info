from django.urls import path

from games_info.games_viewer.views import home

urlpatterns = [
    path('', home, name='home')
]
