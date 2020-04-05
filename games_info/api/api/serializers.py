from rest_framework import serializers

from games_info.api.models import Game, TimeData


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeData
        fields = ['description', 'content']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    time_information = TimeSerializer(many=True)

    class Meta:
        model = Game
        fields = (
            'pk',
            'created_at',
            'updated_at',
            'searched_game',
            'game_name',
            'best_price',
            'current_price',
            'time_information'
        )
        read_only_fields = (
            'created_at',
            'updated_at',
            'game_name',
            'best_price',
            'current_price'
        )
