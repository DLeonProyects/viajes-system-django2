from django.db import models

# Create your models here.

class Viajes(models.Model):
    nombre_conductor = models.CharField(max_length=255)
    precio_viaje = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_viaje = models.CharField(max_length=255)

