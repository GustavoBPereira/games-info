import json
import os

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic.base import View
from selenium.common.exceptions import NoSuchElementException

from games_info.api.models import Game
from games_info.crawler.main import GameCrawler


class GameInfo(View):

    def post(self, *args, **kwargs):
        searched_game = self.request.POST.get('searched_game', None)
        currency = self.request.POST.get('currency', 'us')
        if searched_game is None or searched_game == '':
            raise ValidationError(message='Parameter searched_game not found or empty')

        crawler = GameCrawler(searched_game, currency)
        try:
            game_datas = crawler.get_data()
        except NoSuchElementException:
            return JsonResponse({'error': 'Invalid Game', 'searched_game': searched_game}, status=400)

        game_name = game_datas['steamdb']['real_name']
        current_price = game_datas['steamdb']['current_price']
        best_price = game_datas['steamdb']['best_price']

        try:
            game = Game.objects.get(game_name=game_name)
            game.searched_game = searched_game
            game.game_name = game_name
            game.current_price = current_price
            game.best_price = best_price
            if not game.time_information.exists():
                for time_data in game_datas['how_long']:
                    game.time_information.create(description=time_data[0], content=time_data[1])
            game.save()
            status_code = 200
        except Game.DoesNotExist:
            status_code = 201
            game = Game.objects.create(searched_game=searched_game, game_name=game_name,
                                       current_price=current_price, best_price=best_price)
            for time_data in game_datas['how_long']:
                game.time_information.create(description=time_data[0], content=time_data[1])

        return JsonResponse(game.as_dict(), safe=False, status=status_code)

    def get(self, *args, **kwargs):
        registered_games = Game.objects.all()
        data = [game.as_dict() for game in registered_games]
        return JsonResponse(data, safe=False)


def app_ids(request):
    if request.method == 'GET':
        try:
            query = request.GET['q']
        except KeyError:
            return HttpResponseBadRequest('q param is required')
        with open(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/crawler/app_ids.json', 'r') as f:
            games_ids = json.load(f)
            matches = []
            for game in games_ids['applist']['apps']['app']:
                if query.lower() in game['name'].lower():
                    matches.append(game)
        return JsonResponse({'games': matches})
    else:
        return HttpResponseNotAllowed()
