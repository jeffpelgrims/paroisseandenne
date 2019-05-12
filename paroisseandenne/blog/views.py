from django.shortcuts import render
from .models import Jumbotron, Meditation


def accueil(request):
    jumbotron = Jumbotron.objects.all()
    meditation = Meditation.objects.all()
    return render(
        request, 'index.html',
        {'jumbotron': jumbotron, 'meditation': meditation},
    )