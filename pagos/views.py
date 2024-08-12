from django.shortcuts import render

def pago_list(request):
    # Tu lógica aquí
    return render(request, 'pagos/pago_list.html')
