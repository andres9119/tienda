from django.shortcuts import render, get_object_or_404
from tienda_online.models import Producto



def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {'producto': producto})


def index(request):
    productos_destacados = Producto.objects.filter(destacado=True)
    return render(request, 'inicio/index.html', {'productos_destacados': productos_destacados})
