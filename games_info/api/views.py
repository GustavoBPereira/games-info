import json
import os

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic.base import View

from games_info.api.models import Game
from games_info.crawler.main import GameCrawler


class GameInfo(View):

    def post(self, *args, **kwargs):
        app_id = self.request.POST.get('app_id', None)
        currency = self.request.POST.get('currency', 'us')
        if app_id is None or app_id == '':
            raise ValidationError(message='Parameter searched_game not found or empty')

        crawler = GameCrawler(app_id, currency=currency)
        game_datas = crawler.get_data()

        game_name = game_datas['steamdb']['game_name']
        current_price = game_datas['steamdb']['price']
        best_price = 'not implemented yet'

        try:
            game = Game.objects.get(game_name=game_name)
            game.searched_game = 'not implemented yet'
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
            game = Game.objects.create(searched_game='not implemented yet', game_name=game_name,
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
