from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombreMarca = models.CharField(primary_key=True, max_length=50, verbose_name="Nombre de la Marca", null=False, blank=False)
    descripcionMarca = models.TextField(max_length=250, verbose_name="Descripcion de la Marca", null=True, blank=True)

    def __str__(self):
        return self.nombreMarca

class Categoria(models.Model):
    COMESTIBLE = 'comestible'
    NO_COMESTIBLE = 'no_comestible'
    TIPO_CHOICES = [
        (COMESTIBLE, 'Comestible'),
        (NO_COMESTIBLE, 'No Comestible'),
    ]
    nombreCategoria = models.CharField(primary_key=True, max_length=50, verbose_name="Nombre de la Categoria", null=False, blank=False)
    descripcionCategoria = models.TextField(max_length=250, verbose_name="Descripcion de la Categoria", null=True, blank=True)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, default=COMESTIBLE, verbose_name="Tipo de Categoria")

    def __str__(self):
        return self.nombreCategoria

class subcategoria(models.Model):
    RETORNABLE = 'retornable'
    DESCARTABLE = 'descartable'
    TIPO_CHOICES = [
        (RETORNABLE, 'Retornable'),
        (DESCARTABLE, 'Descartable'),
    ]
    nombreSubcategoria = models.CharField(primary_key=True, max_length=50, verbose_name="Nombre de la Subcategoria", null=False, blank=False)
    descripcionSubcategoria = models.TextField(max_length=250, verbose_name="Descripcion de la Subcategoria", null=True, blank=True)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, default=DESCARTABLE, verbose_name="Tipo de subCategoria")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias', verbose_name="Categoria")
    
    def __str__(self):
        return self.nombreSubcategoria

class Producto(models.Model):
    codigoBarra = models.IntegerField(primary_key=True, verbose_name="ID del Producto")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto", null=False, blank=True)
    fechaIngreso = models.DateField(verbose_name="Fecha de Ingreso", null=False, blank=True)
    fechaVencimiento = models.DateField(verbose_name="Fecha de Vencimiento", null=True, blank=True)
    precio = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Precio", null=True, blank=True)
    contenido = models.IntegerField(verbose_name="Contenido", null=True, blank=True)
    cantidad = models.IntegerField(verbose_name="Cantidad", null=True, blank=True)
    descripcion = models.TextField(max_length=250, verbose_name="Descripcion", null=True, blank=True)
    imagen = models.ImageField(upload_to="productos", verbose_name="Imagen", null=True, blank=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='SIN CATEGORIA')
    subcategoria = models.ForeignKey(subcategoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default='SIN MARCA')

    def __str__(self):
        return self.nombreProducto

class Venta(models.Model):
    id = models.AutoField(primary_key=True)  # Campo autoincremental
    fechaVenta = models.DateTimeField(verbose_name="Fecha y Hora de la Venta")
    usuario = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name="Usuario que realizó la Venta")
    ventaRealizada = models.BooleanField(default=False, verbose_name="Venta Realizada")

    def __str__(self):
        return f"Venta {self.fechaVenta} - {self.usuario}"

class ProductoVendido(models.Model):
    id = models.AutoField(primary_key=True)  # Agrega este campo
    venta = models.ForeignKey(Venta, on_delete=models.SET_DEFAULT, default=1, null=False, related_name="productosVendidos", verbose_name="Venta")
    producto = models.ForeignKey(Producto, on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name="Producto")
    cantidad = models.IntegerField(verbose_name="Cantidad Vendida")
    precioAlMomento = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Precio al momento de la Venta", null=True, blank=True)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombreProducto} en {self.venta}"