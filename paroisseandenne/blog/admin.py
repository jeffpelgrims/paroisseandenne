from django.contrib import admin
from .models import Jumbotron, Meditation, Blog


class JumbotronAdmin(admin.ModelAdmin):
    list_display = ('extrait', 'texte', 'jumbo_url')


class MeditationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'texte')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre_article', 'date_article')


admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Meditation, MeditationAdmin)
admin.site.register(Blog, BlogAdmin)
