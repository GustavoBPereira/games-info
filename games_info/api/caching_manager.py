from datetime import timedelta

import pytz
from decouple import config
from django.conf import settings
from django.http import JsonResponse
from django.utils.datetime_safe import datetime


def check_range_time(game):
    return game.updated_at > pytz.utc.localize(datetime.today()) - timedelta(hours=settings.CACHE_HOURS)


def check_cached_response(game):
    if game is not None and config('CACHED_CRAWLER', default=True, cast=bool) and check_range_time(game):
        return True


def cached_response(game):
    return JsonResponse(game.as_dict(), safe=False, status=200)
