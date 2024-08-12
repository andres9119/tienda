from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiencia_list, name='experiencia_list'),
]
