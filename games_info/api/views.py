import json
import os

from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.generic.base import View

from games_info.api.models import Game, Platform, Genre
from games_info.crawler.main import GameCrawler


class GameInfo(View):

    def post(self, *args, **kwargs):
        app_id = self.request.POST.get('app_id', None)
        currency = self.request.POST.get('currency', 'us')
        if app_id is None or app_id == '':
            raise ValidationError(message='Parameter searched_game not found or empty')

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
                currency=steam_data['price_overview']['currency'],
                game_name=steam_data['game_name'],
                short_description=steam_data['short_description'],
                supported_languages=steam_data['supported_languages'],
                metacritic_score=steam_data['metacritic']['score'],
                metacritic_url=steam_data['metacritic']['url'],
                recommendations=steam_data['recommendations'],
                coming_soon=steam_data['release_date']['coming_soon'],
                release_date=steam_data['release_date']['date'],
                is_free=steam_data['is_free'],
                discount_percent=steam_data['price_overview']['discount_percent'],
                initial_formatted=steam_data['price_overview']['initial_formatted'],
                final_formatted=steam_data['price_overview']['final_formatted'],
                header_image=steam_data['header_image']
            )
            for time_data in game_datas['how_long']:
                game.time_information.create(description=time_data[0], content=time_data[1])

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
        with open(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/crawler/app_ids.json', 'r') as f:
            games_ids = json.load(f)
            matches = []
            for game in games_ids['applist']['apps']['app']:
                if query.lower() in game['name'].lower():
                    matches.append(game)
        return JsonResponse({'games': matches})
    else:
        return HttpResponseNotAllowed()
