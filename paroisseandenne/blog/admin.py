from django.contrib import admin
from .models import Jumbotron, Meditation


class JumbotronAdmin(admin.ModelAdmin):
    list_display = ('extrait', 'texte', 'jumbo_url')

class MeditationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'texte')


admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Meditation, MeditationAdmin)
