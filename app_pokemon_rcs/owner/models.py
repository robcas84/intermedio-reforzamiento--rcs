from django.db import models

class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    pais = models.CharField(max_length=30, default='')
    desactivado = models.BooleanField(default=False)