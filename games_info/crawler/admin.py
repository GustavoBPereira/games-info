from django.contrib import admin

from games_info.crawler.models import SteamApp


class SteamAppAdmin(admin.ModelAdmin):
    list_display = ('app_id', 'name')
    search_fields = ('app_id', 'name')

admin.site.register(SteamApp, SteamAppAdmin)
