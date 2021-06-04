import json
import os

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic.base import View

from games_info.api.caching_manager import check_cached_response, cached_response
from games_info.api.models import Game
from games_info.crawler import accepted_currency
from games_info.crawler.main import GameCrawler


class GameInfo(View):

    def post(self, *args, **kwargs):
        app_id = self.request.POST.get('app_id', None)
        currency = self.request.POST.get('currency', 'us')
        if app_id is None:
            error_data = {'error': True, 'message': 'Required parameter app_id not found or empty'}
            return JsonResponse(status=422, data=error_data)

        game = Game.objects.existing_game_object(app_id, accepted_currency[currency]['code'])
        if check_cached_response(game):
            return cached_response(game)

        crawler = GameCrawler(app_id, currency=currency)
        game_data = crawler.get_data()

        try:
            game = Game.objects.get(app_id=app_id, currency=game_data['steamdb']['price_overview']['currency'])
            game.save()
            status_code = 200
        except Game.DoesNotExist:
            game = Game.create_from_crawl_data(app_id=app_id, crawler_data=game_data)
            status_code = 201
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
        with open(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/crawler/app_ids.json', 'r',
                  encoding='utf-8') as f:
            games_ids = json.load(f)
            matches = []
            for game in games_ids['applist']['apps']['app']:
                if query.lower() in game['name'].lower() and 'soundtrack' not in game['name'].lower():
                    matches.append(game)
            sorted_matches = sorted(matches, key=lambda k: len(k['name']))
        return JsonResponse({'games': sorted_matches[0:15]})
    else:
        return HttpResponseNotAllowed()
