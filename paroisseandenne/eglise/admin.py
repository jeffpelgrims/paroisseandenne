from django.contrib import admin
from .models import Eglise


class EgliseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'ville', 'tag', 'photo_url')


admin.site.register(Eglise, EgliseAdmin)
