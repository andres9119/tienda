from django.urls import path
from . import views

urlpatterns = [
    path('', views.pago_list, name='pago_list'),
]


