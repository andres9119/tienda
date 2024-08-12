# carrito/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import CarritoItem, Carrito
from productos.models import Producto
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt




stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount')  

            if not amount:
                return JsonResponse({'error': 'Falta el monto'}, status=400)

            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
            )

            # Devolver el client_secret al cliente
            return JsonResponse({'clientSecret': intent['client_secret']})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Algo salió mal'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

    
def obtener_carrito(request):
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
        return CarritoItem.objects.filter(carrito=carrito)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        return CarritoItem.objects.filter(carrito__isnull=True)  

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('carrito:ver_carrito')


def quitar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id)
    carrito_item.delete()
    return redirect('carrito:ver_carrito')

def ver_carrito(request):
    carrito_items = obtener_carrito(request)
    total = sum(item.subtotal() for item in carrito_items)
    return render(request, 'carrito/ver_carrito.html', {'carrito_items': carrito_items, 'total': total})


def success(request):
    return render(request, 'carrito/success.html')




def payment_view(request):
    return render(request, 'carrito/payment.html')
