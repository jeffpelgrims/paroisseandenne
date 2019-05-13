from django.shortcuts import render
from .models import Jumbotron, Meditation, Blog


def accueil(request):
    jumbotron = Jumbotron.objects.all()
    meditation = Meditation.objects.all()
    blog = Blog.objects.all().order_by('-date_article')[:5]
    context = {
        'jumbotron': jumbotron,
        'meditation': meditation,
        'blog': blog
    }
    return render(
        request,
        'index.html',
        context
    )