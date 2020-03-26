from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from games_info.api.api.serializers import GameSerializer
from games_info.api.models import Game
from games_info.crawler.main import GameCrawler


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, request):
        searched_game = request.POST.get('searched_game', None)

        if searched_game is None or searched_game == '':
            raise ValidationError(detail='Parameter searched_game not found or empty')

        crawler = GameCrawler(searched_game)
        game_data_steamdb = crawler.get_data_from_steamdb()
        crawler.close()

        game_name = game_data_steamdb['real_name']
        current_price = game_data_steamdb['current_price']
        best_price = game_data_steamdb['best_price']

        try:
            status_code = status.HTTP_200_OK
            game = Game.objects.get(game_name=game_name)
            game.searched_game = searched_game
            game.game_name = game_name
            game.current_price = current_price
            game.best_price = best_price
            game.save()
        except Game.DoesNotExist:
            status_code = status.HTTP_201_CREATED
            game = Game.objects.create(searched_game=searched_game, game_name=game_name,
                                       current_price=current_price, best_price=best_price)
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status_code)