from django.core.management.base import BaseCommand

from games_info.crawler.models import SteamApp


class Command(BaseCommand):
    help = 'Put in the database steam apps to be used in develop'
    apps = [
        {
            'app_id': 753640,
            'name': 'Outer Wilds'
        },
        {
            'app_id': 683320,
            'name': 'GRIS'
        }
    ]

    def handle(self, *args, **options):
        print(' Running crawler_setup...')
        for app in self.apps:
            SteamApp.objects.get_or_create(name=app['name'], app_id=app['app_id'])
