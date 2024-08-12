# pedidos/views.py
from django.shortcuts import render

def pedido_list(request):
    # Lógica para manejar la solicitud
    return render(request, 'pedidos/pedido_list.html')
