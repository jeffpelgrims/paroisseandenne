from django.shortcuts import render
from django.http import Http404
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


def blog_detail(request, post_id):
    try:
        obj = Blog.objects.get(id=post_id)
    except Blog.DoesNotExist:
        raise Http404
    template_name = 'blog_detail.html'
    context = {"object" : obj}
    return render(request, template_name, context)