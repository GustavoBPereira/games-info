from django.core.management.base import BaseCommand
from django.db import IntegrityError

from games_info.crawler.models import SteamApp
from games_info.crawler.utils import get_app_ids


class Command(BaseCommand):
    help = 'Put in the database all steam apps'

    def handle(self, *args, **options):
        print(' Running crawler_steam_appids...')
        app_ids = get_app_ids()
        try:
            apps = app_ids['applist']['apps']['app']
        except KeyError:
            raise KeyError('get_app_ids function returned a json without apps')
        
        for app in apps:
            try:
                SteamApp.objects.create(name=app['name'], app_id=app['appid'])
            except IntegrityError:
                print(f"Integrity Error app_id={app['appid']} | name={app['name']}")
        
        print(' Ok')