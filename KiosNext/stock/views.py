from rest_framework import viewsets
from .serializer import StockSerializer
from .models import Producto
# Create your views here.

class StockViews(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Producto.objects.all()
    
