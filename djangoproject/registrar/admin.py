from django.contrib import admin
from .models import Marca, Categoria, subcategoria, Producto, Venta, ProductoVendido

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto', 'codigoBarra', 'fechaIngreso', 'precio', 'cantidad','Categoria', 'subcategoria', 'marca')
    fields = ('codigoBarra', 'nombreProducto', 'fechaIngreso', 'fechaVencimiento', 'precio', 'cantidad', 'descripcion', 'imagen','Categoria', 'subcategoria', 'marca')
    search_fields = ('nombreProducto', 'codigoBarra')
    list_filter = ('subcategoria', 'marca')

class ProductoVendidoInline(admin.TabularInline):
    model = ProductoVendido
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechaVenta', 'usuario', 'ventaRealizada')
    fields = ('fechaVenta', 'usuario', 'ventaRealizada')
    inlines = [ProductoVendidoInline]
    search_fields = ('usuario__username', 'fechaVenta')
    list_filter = ('ventaRealizada', 'fechaVenta')

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(subcategoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)