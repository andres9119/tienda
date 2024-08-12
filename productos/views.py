# views.py
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria

def lista_productos(request):
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    categorias = Categoria.objects.all()
    
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'categorias': categorias})

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/producto_detalle.html', {'producto': producto})

def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/producto_form.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/producto_form.html', {'form': form})
