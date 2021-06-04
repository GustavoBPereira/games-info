import json
import os

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic.base import View

from games_info.api.caching_manager import check_cached_response, cached_response
from games_info.api.models import Game, Platform, Genre, TimeData
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
        game_datas = crawler.get_data()

        steam_data = game_datas['steamdb']

        try:
            game = Game.objects.get(app_id=app_id, currency=steam_data['price_overview']['currency'])
            game.save()
            status_code = 200

        except Game.DoesNotExist:
            status_code = 201
            game = Game.objects.create(
                app_id=app_id,
                type=steam_data['type'],
                currency=steam_data['price_overview']['currency'],
                game_name=steam_data['game_name'],
                short_description=steam_data['short_description'],
                supported_languages=steam_data['supported_languages'],
                metacritic_score=steam_data['metacritic'].get('score'),
                metacritic_url=steam_data['metacritic'].get('url'),
                recommendations=steam_data['recommendations'],
                coming_soon=steam_data['release_date']['coming_soon'],
                release_date=steam_data['release_date']['date'],
                is_free=steam_data['is_free'],
                discount_percent=steam_data['price_overview']['discount_percent'],
                initial_formatted=steam_data['price_overview']['initial_formatted'],
                final_formatted=steam_data['price_overview']['final_formatted'],
                header_image=steam_data['header_image'],
                background_image=steam_data['background_image'],
            )
            for time_data in game_datas['how_long']:
                TimeData.objects.create(game=game, description=time_data[0], content=time_data[1])

            for platform in steam_data['platforms'].items():
                Platform.objects.create(game=game, platform=platform[0], supported=platform[1])

            for genre in steam_data['genres']:
                Genre.objects.create(game=game, name=genre['description'])

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
