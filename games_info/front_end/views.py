from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View

from games_info.api.models import Game
from games_info.front_end.forms import SearchGameForm


class Index(View):
    http_method_names = ['get', 'post']

    def get(self, *args, **kwargs):
        form = SearchGameForm()
        return render(self.request, 'index.html', {'form': form})


class ResultDetail(DetailView):
    template_name = 'result_detail.html'
    model = Game

    def get_context_data(self, *args, **kwargs):
        context = super(ResultDetail, self).get_context_data(*args, **kwargs)
        context['game'] = context['object'].as_dict()
        context['game_url'] = f"https://store.steampowered.com/app/{context['game']['app_id']}"
        return context
