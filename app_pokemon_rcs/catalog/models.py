from django.db import models

class Catalog(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    