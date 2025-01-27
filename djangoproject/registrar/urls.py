from django.urls import path
from .views import bienvenidoview, atenderview, stockearview, consultarview, stockgeneralview, agregarmarcaview, agregarcategoriaview, agregarsubcategoriaview, get_subcategorias

urlpatterns = [
    path('', bienvenidoview, name='bienvenido'),
    path('bienvenido/', bienvenidoview, name='bienvenido'),
    path('atender/', atenderview, name='atender'),
    path('stockear/', stockearview, name='stockear'),
    path('consultar/', consultarview, name='consultar'),
    path('stockgeneral/', stockgeneralview, name='stockgeneral'),
    path('agregarmarca/', agregarmarcaview, name='agregarmarca'),
    path('agregarcategoria/', agregarcategoriaview, name='agregarcategoria'),
    path('agregarsubcategoria/', agregarsubcategoriaview, name='agregarsubcategoria'),
    path('api/subcategorias/', get_subcategorias, name='get_subcategorias'),
]