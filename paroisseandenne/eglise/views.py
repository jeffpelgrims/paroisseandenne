from django.shortcuts import render
from .models import Eglise


def accueil(request):
    nav = Eglise.objects.all()
    return render(request, 'eglise.html', {'nav' : nav})


def detail(request, tag):
    nav = Eglise.objects.all()
    eglise = Eglise.objects.filter(tag=tag)
    context = {
        'eglise': eglise,
        'nav': nav,
    }
    return render(request, 'eglise_det.html', context)