from django.db import models
from eglise.models import Eglise


class Agenda(models.Model):
    nom_evenement = models.CharField(max_length=255)
    lieu_evenement = models.ForeignKey('eglise.Eglise',
                                       on_delete=models.CASCADE,
                                       default='1')
    date_evenement = models.DateField()
    heure_evenement = models.TimeField()
    description_evenement = models.TextField()

