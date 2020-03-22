from django.http import JsonResponse


def game_api(request):
    return JsonResponse({'hello': True})
