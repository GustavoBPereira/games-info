from django.db.models.functions import Length
from django.http import JsonResponse
from django.views.generic.base import View

from games_info.api.caching_manager import check_cached_response, cached_response
from games_info.api.models import Game
from games_info.crawler import accepted_currency
from games_info.crawler.models import SteamApp
from games_info.crawler.utils import Crawler


class GameInfo(View):

    def post(self, *args, **kwargs):
        app_id = self.request.POST.get('app_id', None)
        currency = self.request.POST.get('currency', 'us')
        if app_id is None:
            error_data = {'error': True, 'message': 'Required parameter app_id not found or empty'}
            return JsonResponse(status=422, data=error_data)

        game_obj = Game.objects.existing_game_object(app_id, accepted_currency[currency]['code'])
        if check_cached_response(game_obj):
            return cached_response(game_obj)

        crawler = Crawler(app_id, currency=currency)
        game_data = crawler.get_data()

        if not game_obj:
            game_obj = Game.create_from_crawl_data(app_id=app_id, crawler_data=game_data)
            status_code = 201
        else:
            status_code = 200
        return JsonResponse(game_obj.as_dict(), safe=False, status=status_code)

    def get(self, *args, **kwargs):
        registered_games = Game.objects.all()
        data = [game.as_dict() for game in registered_games]
        return JsonResponse(data, safe=False)


class AppIds(View):

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        if query is None:
            error_data = {'error': True, 'message': 'Required parameter q not found or empty'}
            return JsonResponse(status=422, data=error_data)
        return JsonResponse({'games': [{'name':app.name, 'appid':app.app_id} for app in SteamApp.objects.filter(name__icontains=query).order_by(Length('name'))]})
