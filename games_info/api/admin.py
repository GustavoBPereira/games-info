from django.contrib import admin

from games_info.api.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'currency', 'updated_at')
    ordering = ('updated_at',)


admin.site.register(Game, GameAdmin)
