from django.shortcuts import render
from django.http import HttpResponse
from randomizerapp.moo2randomizer import Result


def index(request):
    result = Result()
    context = {'result': result}
    return render(request, 'randomizerapp/index.html', context)
