# usuarios/urls.py
from django.urls import path
from .views import registro, CustomLoginView, actualizar_perfil
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileUpdateView, CustomLogoutView, RegisterView

app_name = 'usuarios'

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),  # Asegúrate de que esta línea esté presente
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='usuarios/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('update/', actualizar_perfil, name='update_profile'),
    path('actualizar-perfil/', actualizar_perfil, name='actualizar_perfil'),
]
