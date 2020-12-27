from django.shortcuts import render
from django.views.generic.base import View

from games_info.front_end.forms import SearchGameForm


class Index(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        form = SearchGameForm()
        return render(self.request, 'index.html', {'form': form})
