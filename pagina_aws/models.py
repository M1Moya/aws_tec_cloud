from django.db import models

# Create your models here.
class Dudas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=15)
    dudas = models.CharField(max_length=250)

class Suscripcion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=15)