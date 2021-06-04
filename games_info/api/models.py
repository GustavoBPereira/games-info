from django.db import models

from games_info.api.managers import GameManager


class Game(models.Model):
    objects = GameManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    app_id = models.IntegerField()
    currency = models.CharField(max_length=32)

    game_name = models.CharField(max_length=128)
    type = models.CharField(max_length=64, blank=True, null=True)
    short_description = models.TextField()
    supported_languages = models.TextField()

    metacritic_score = models.FloatField(null=True, blank=True)
    metacritic_url = models.URLField(null=True, blank=True)
    recommendations = models.IntegerField(null=True, blank=True)
    coming_soon = models.BooleanField()
    release_date = models.CharField(max_length=32)

    is_free = models.BooleanField()
    discount_percent = models.FloatField(null=True, blank=True)
    initial_formatted = models.CharField(null=True, blank=True, max_length=64)
    final_formatted = models.CharField(null=True, blank=True, max_length=64)

    header_image = models.URLField()
    background_image = models.URLField(blank=True, null=True)

    def as_dict(self):
        return {
            'id': self.pk,
            'app_id': self.app_id,
            'type': self.type,
            'game_name': self.game_name,
            'short_description': self.short_description,
            'supported_languages': self.supported_languages,
            'metacritic_score': self.metacritic_score,
            'metacritic_url': self.metacritic_url,
            'recommendations': self.recommendations,
            'comming_soon': self.coming_soon,
            'release_date': self.release_date,
            'is_free': self.is_free,
            'discount_percent': self.discount_percent,
            'initial_formatted': self.initial_formatted,
            'final_formatted': self.final_formatted,
            'time_information': [time_info.as_dict() for time_info in self.timedata_set.all()],
            'header_image': self.header_image,
            'background_image': self.background_image,
            'platforms': [
                {'platform': platform.platform, 'supported': platform.supported} for platform in self.platform_set.all()
            ],
            'genres': [genre.name for genre in self.genre_set.all()]
        }

    @classmethod
    def create_from_crawl_data(cls, crawler_data, app_id):
        steam_data = crawler_data['steamdb']
        game = cls.objects.create(
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
        for time_data in crawler_data['how_long']:
            TimeData.objects.create(game=game, description=time_data[0], content=time_data[1])

        for platform in steam_data['platforms'].items():
            Platform.objects.create(game=game, platform=platform[0], supported=platform[1])

        for genre in steam_data['genres']:
            Genre.objects.create(game=game, name=genre['description'])
        return game

class TimeData(models.Model):
    description = models.CharField(max_length=64)
    content = models.CharField(max_length=64)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def as_dict(self):
        return {
            'description': self.description,
            'content': self.content
        }


class Platform(models.Model):
    platform = models.CharField(max_length=128)
    supported = models.BooleanField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
