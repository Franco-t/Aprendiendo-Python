from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Marca, Categoria, subcategoria, Venta, ProductoVendido
from django.http import JsonResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

@login_required
def bienvenidoview(request):
    return render(request, 'registrar/bienvenido.html', {'current_view': 'bienvenido'})

@login_required
def atenderview(request):
    if request.method == 'POST':
        if 'codigo_barra' in request.POST:
            codigo_barra = request.POST.get('codigo_barra')
            try:
                producto = Producto.objects.get(codigoBarra=codigo_barra)
                # Crear una nueva venta si no hay una venta en curso
                venta, created = Venta.objects.get_or_create(
                    fechaVenta=timezone.now(),
                    usuario=request.user,
                    ventaRealizada=False
                )
                producto_vendido, created = ProductoVendido.objects.get_or_create(
                    venta=venta,
                    producto=producto,
                    defaults={'cantidad': 1, 'precioAlMomento': producto.precio}
                )
                if not created:
                    producto_vendido.cantidad += 1
                    producto_vendido.save()
            except Producto.DoesNotExist:
                return render(request, 'registrar/atender.html', {
                    'error_message': 'Producto no encontrado.'
                })
        elif 'cancelar_venta' in request.POST:
            # Eliminar la venta en curso
            Venta.objects.filter(usuario=request.user, ventaRealizada=False).delete()
        elif 'terminar_venta' in request.POST:
            # Guardar la venta en curso
            venta = Venta.objects.filter(usuario=request.user, ventaRealizada=False).first()
            if venta:
                venta.ventaRealizada = True
                venta.save()
        return redirect('atender')

    # No cargar la última venta, siempre empezar con una nueva venta
    venta = None
    productos_vendidos = []

    total = sum(pv.precioAlMomento * pv.cantidad for pv in productos_vendidos)

    return render(request, 'registrar/atender.html', {
        'venta': venta,
        'productos_vendidos': productos_vendidos,
        'total': total
    })


@login_required
def stockearview(request):
    if request.method == 'POST':
        codigo_barra = request.POST.get('codigo_barra')
        nombre_producto = request.POST.get('producto')
        contenido = request.POST.get('contenido')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        marca_nombre = request.POST.get('marca')
        categoria_nombre = request.POST.get('categoria')
        subcategoria_nombre = request.POST.get('subcategoria')

        try:
            marca = Marca.objects.get(nombreMarca=marca_nombre)
            categoria = Categoria.objects.get(nombreCategoria=categoria_nombre)
            subcategoria_obj = subcategoria.objects.get(nombreSubcategoria=subcategoria_nombre)
        except ObjectDoesNotExist:
            return render(request, 'registrar/stockear.html', {
                'marcas': Marca.objects.all(),
                'categorias': Categoria.objects.all(),
                'error_message': 'Marca, categoría o subcategoría no encontrada'
            })

        Producto.objects.create(
            codigoBarra=codigo_barra,
            nombreProducto=nombre_producto,
            contenido=contenido,
            precio=precio,
            cantidad=cantidad,
            fechaIngreso=fecha_ingreso,
            marca=marca,
            Categoria=categoria,
            subcategoria=subcategoria_obj
        )
        return redirect('stockear')

    return render(request, 'registrar/stockear.html', {
        'marcas': Marca.objects.all(),
        'categorias': Categoria.objects.all()
    })

@login_required
def consultarview(request):
    producto = None
    error_message = None

    if request.method == 'POST':
        if 'codigo_barra' in request.POST:
            # Buscar producto
            codigo_barra = request.POST.get('codigo_barra')
            if codigo_barra:
                try:
                    producto = Producto.objects.get(codigoBarra=codigo_barra)
                except Producto.DoesNotExist:
                    error_message = "Producto no encontrado"
        else:
            # Actualizar producto
            codigo_barra = request.POST.get('codigo de barra')
            try:
                producto = Producto.objects.get(codigoBarra=codigo_barra)
                producto.nombreProducto = request.POST.get('producto')
                producto.contenido = request.POST.get('contenido')
                producto.precio = request.POST.get('precio')
                producto.cantidad = request.POST.get('cantidad')
                producto.fechaVencimiento = request.POST.get('Fecha de Vencimiento')
                producto.fechaIngreso = request.POST.get('Fecha de Ingreso')
                producto.marca.nombreMarca = request.POST.get('marca')
                producto.Categoria.nombreCategoria = request.POST.get('categoria')
                producto.subcategoria.nombreSubcategoria = request.POST.get('subcategoria')
                producto.save()
            except Producto.DoesNotExist:
                error_message = "Producto no encontrado"

    return render(request, 'registrar/consultar.html', {'producto': producto, 'error_message': error_message, 'current_view': 'consultar'})

@login_required
def stockgeneralview(request):
    productos = Producto.objects.all()
    return render(request, 'registrar/stockgeneral.html', {'productos': productos, 'current_view': 'stockgeneral'})

@login_required
def agregarmarcaview(request):
    if request.method == 'POST':
        nombre_marca = request.POST.get('nombre_marca')
        descripcion_marca = request.POST.get('descripcion_marca')
        if nombre_marca:
            Marca.objects.create(nombreMarca=nombre_marca, descripcionMarca=descripcion_marca)
            return redirect('stockear')
    return render(request, 'registrar/agregarmarca.html')

@login_required
def agregarcategoriaview(request):
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')
        descripcion_categoria = request.POST.get('descripcion_categoria')
        tipo_categoria = request.POST.get('tipo_categoria')
        if nombre_categoria:
            Categoria.objects.create(nombreCategoria=nombre_categoria, descripcionCategoria=descripcion_categoria, tipo=tipo_categoria)
            return redirect('stockear')
    return render(request, 'registrar/agregarcategoria.html')

@login_required
def agregarsubcategoriaview(request):
    if request.method == 'POST':
        nombre_subcategoria = request.POST.get('nombre_subcategoria')
        descripcion_subcategoria = request.POST.get('descripcion_subcategoria')
        tipo_subcategoria = request.POST.get('tipo_subcategoria')
        categoria_nombre = request.POST.get('categoria')
        try:
            categoria = Categoria.objects.get(nombreCategoria=categoria_nombre)
        except ObjectDoesNotExist:
            return render(request, 'registrar/agregarsubcategoria.html', {
                'categorias': Categoria.objects.all(),
                'error_message': 'Categoría no encontrada'
            })
        if nombre_subcategoria:
            subcategoria.objects.create(
                nombreSubcategoria=nombre_subcategoria,
                descripcionSubcategoria=descripcion_subcategoria,
                tipo=tipo_subcategoria,
                categoria=categoria
            )
            return redirect('stockear')
    categorias = Categoria.objects.all()
    return render(request, 'registrar/agregarsubcategoria.html', {'categorias': categorias})

@login_required
def get_subcategorias(request):
    categoria_nombre = request.GET.get('categoria')
    if categoria_nombre:
        subcategorias = subcategoria.objects.filter(categoria__nombreCategoria=categoria_nombre)
        subcategorias_list = list(subcategorias.values('nombreSubcategoria'))
        return JsonResponse({'subcategorias': subcategorias_list})
    return JsonResponse({'error': 'No se proporcionó una categoría'}, status=400)

