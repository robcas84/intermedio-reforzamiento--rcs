from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    numero = models.IntegerField(default=0)