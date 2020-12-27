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
