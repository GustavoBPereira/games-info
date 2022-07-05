from django.db import models


class SteamApp(models.Model):
    name = models.CharField(verbose_name='Name', max_length=319)
    app_id = models.PositiveIntegerField(verbose_name='app_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Steam App'
        verbose_name_plural = ' Steam Apps'
        unique_together = (('name', 'app_id'),)
