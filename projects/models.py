from django.db import models

class Autos(models.Model):
    marca = models.CharField(max_length=50)
    cantidad_pasajeros=models.CharField(max_length=3)

