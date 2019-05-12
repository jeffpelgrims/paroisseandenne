from django.db import models


class Jumbotron(models.Model):
    extrait = models.CharField(max_length=255, null=False)
    texte = models.TextField(null=False)
    jumbo_url = models.CharField(null=True, max_length=1025)


class Meditation(models.Model):
    titre = models.CharField(max_length=255, null=False)
    texte = models.TextField(null=False)