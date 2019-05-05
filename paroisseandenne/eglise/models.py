from django.db import models


class eglise(models.Model):
    nom = models.CharField(max_length=125)
    rue = models.CharField(max_length=125)
    numero = models.IntegerField()
    c_postal = models.IntegerField()
    ville = models.CharField(50)
    description = models.TextField()
    photo_url = models.CharField(1025)