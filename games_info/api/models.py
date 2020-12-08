from django.db import models


class TimeData(models.Model):
    description = models.CharField(max_length=64)
    content = models.CharField(max_length=64)

    def as_dict(self):
        return {
            'description': self.description,
            'content': self.content
        }


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    app_id = models.IntegerField()
    currency = models.CharField(max_length=32)

    game_name = models.CharField(max_length=128)
    short_description = models.TextField()
    supported_languages = models.TextField()

    metacritic_score = models.FloatField()
    metacritic_url = models.URLField()
    recommendations = models.IntegerField()
    coming_soon = models.BooleanField()
    release_date = models.CharField(max_length=32)

    is_free = models.BooleanField()
    discount_percent = models.FloatField(null=True, blank=True)
    initial_formatted = models.CharField(null=True, blank=True, max_length=64)
    final_formatted = models.CharField(null=True, blank=True, max_length=64)

    time_information = models.ManyToManyField(TimeData, related_name='time_information')

    def as_dict(self):
        return {
            'id': self.app_id,
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
            'time_information': [time_info.as_dict() for time_info in self.time_information.all()]
        }


class Platform(models.Model):
    platform = models.CharField(max_length=128)
    supported = models.BooleanField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(max_length=64)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
