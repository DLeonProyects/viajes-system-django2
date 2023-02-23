from django.db import models
from django.db.models import Sum


# Create your models here.




class Viajess(models.Model):
    nombre_conductor = models.CharField(max_length=255)
    precio_viaje = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_viaje = models.CharField(max_length=255)

    def get_total_precios(self):
        total_precios = Viajess.objects.aggregate(Sum('precio_viaje'))['precio_viaje__sum']
        return total_precios

    def __str__(self):
        total_precios = self.get_total_precios()
        total_registros = Viajess.objects.count()
        return f'ID: {self.id}: NOMBRE:   {self.nombre_conductor} PRECIO:   {self.precio_viaje} FECHA:   {self.fecha_viaje}  TOTAL REGISTROS: {total_registros}  TOTAL PRECIOS: {total_precios}'