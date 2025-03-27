from rest_framework import serializers
from .models import Producto

class StockSerializer(serializers.ModelSerializer):  # Usa ModelSerializer correctamente
    class Meta:
        model = Producto
        #fields = ('id', 'codigo', 'nombre', 'descripcion', 'precio', 'cantidad')  # Lista de campos
        fields = '__all__'