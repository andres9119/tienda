from django.urls import path
from . import views

app_name = 'nosotros'

urlpatterns = [
    path('', views.about, name='about'),  # Ruta para la vista about de la aplicación nosotros
]

