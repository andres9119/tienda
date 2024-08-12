from django.shortcuts import render
from .models import Producto  # Asegúrate de importar el modelo correspondiente

def inventario_list(request):
    productos = Producto.objects.all()  # Obtén todos los productos del inventario
    return render(request, 'inventario/inventario_list.html', {'productos': productos})
