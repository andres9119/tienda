
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('crear/', views.producto_crear, name='producto_crear'),
    path('<int:pk>/editar/', views.producto_editar, name='producto_editar'),
]

    
   