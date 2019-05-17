from django.contrib import admin
from .models import Agenda


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nom_evenement', 'lieu_evenement', 'date_evenement')


admin.site.register(Agenda, AgendaAdmin)
