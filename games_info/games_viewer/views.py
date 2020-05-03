from django.shortcuts import render


def home(request):
    from django.http import HttpResponse
    return HttpResponse('Hello :D')
