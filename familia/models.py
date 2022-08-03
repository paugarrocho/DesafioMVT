import string
from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    fechaNacimiento = models.DateField()
    edad = models.IntegerField(null=True, blank=True)
