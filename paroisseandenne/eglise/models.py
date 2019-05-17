from django.db import models


class Eglise(models.Model):
    nom = models.CharField(max_length=125)
    tag = models.CharField(max_length=50, default='None')
    rue = models.CharField(max_length=125)
    numero = models.IntegerField()
    c_postal = models.IntegerField()
    ville = models.CharField(max_length=50)
    description = models.TextField()
    photo_url = models.CharField(max_length=1025)
    maps_url = models.CharField(max_length=1025, default='None')

    def __str__(self):
        return self.ville

    def get_absolute_url(self):
        return f"/eglise/{self.tag}"