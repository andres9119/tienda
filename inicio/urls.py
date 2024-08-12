

from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),
]





