from django.shortcuts import render
from django.views.generic.base import View
from django.urls import reverse
import requests

from games_info.front_end.forms import SearchGameForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject


class Index(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        form = SearchGameForm()
        return render(self.request, 'index.html', {'form': form})

    def post(self, *args, **kwargs):
        form = SearchGameForm(self.request.POST)
        game = form['game_search'].value()
        currency = form['currency'].value()
        current_site = SimpleLazyObject(lambda: get_current_site(self.request))
        url = 'http://' + str(current_site) + reverse('api')
        game_data = requests.post(url=url, data={'searched_game': game, 'currency': currency})
        return render(self.request, 'index.html', {'game': game_data.json(), 'form': form})
