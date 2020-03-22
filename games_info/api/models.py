from django.db import models


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    searched_game = models.CharField(max_length=128)
    game_name = models.CharField(max_length=128)
    best_price = models.CharField(max_length=25)
    current_price = models.CharField(max_length=25)
