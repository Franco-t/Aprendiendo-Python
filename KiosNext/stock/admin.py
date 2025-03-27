from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'precio', 'cantidad')  # Campos que se mostrarán en la tabla

admin.site.register(Producto, ProductoAdmin)