from django.db import models

# Create your models here.

class Producto (models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Precio: {self.precio}, Cantidad: {self.cantidad})"