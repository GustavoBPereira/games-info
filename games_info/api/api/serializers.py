from rest_framework import serializers

from games_info.api.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'pk',
            'created_at',
            'updated_at',
            'searched_game',
            'game_name',
            'best_price',
            'current_price'
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'game_name',
            'best_price',
            'current_price'
        )
