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
    searched_game = models.CharField(max_length=128)
    game_name = models.CharField(max_length=128)
    best_price = models.CharField(max_length=25)
    current_price = models.CharField(max_length=25)
    time_information = models.ManyToManyField(TimeData, related_name='time_information')

    def as_dict(self):
        return {
            'id': self.pk,
            'searched_game': self.searched_game,
            'game_name': self.game_name,
            'best_price': self.best_price,
            'current_price': self.current_price,
            'time_information': [time_info.as_dict() for time_info in self.time_information.all()]
        }
