from django.shortcuts import render
from .models import Eglise


nav = Eglise.objects.all()


def accueil(request):
    return render(request, 'eglise.html', {'nav' : nav})


def detail(request, tag):
    try:
        eglise = Eglise.objects.filter(tag=tag)
    except Eglise.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    context = {
        'eglise': eglise,
        'nav': nav,
    }
    return render(request, 'eglise_det.html', context)