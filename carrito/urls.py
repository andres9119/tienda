# carrito/urls.py
from django.urls import path
from . import views
from .views import agregar_al_carrito, quitar_del_carrito, ver_carrito,payment_view, success , create_payment_intent


app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar/<int:item_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),    
    path('payment/', payment_view, name='payment_view'),    
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    path('success/', views.success, name='success'),

]




