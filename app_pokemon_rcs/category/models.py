from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=40)