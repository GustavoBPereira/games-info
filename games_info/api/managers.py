from django.db import models


class GameManager(models.Manager):

    def existing_game_object(self, app_id, currency):
        return self.filter(app_id=app_id, currency=currency).first()
