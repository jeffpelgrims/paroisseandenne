from django.shortcuts import render
from django.http import Http404
from .models import Eglise


nav = Eglise.objects.all()


def accueil(request):
    return render(request, 'eglise.html', {'nav' : nav})


def detail(request, tag):
    eglise = Eglise.objects.filter(tag=tag)
    context = {
        'eglise': eglise,
        'nav': nav,
    }
    return render(request, 'eglise_det.html', context)