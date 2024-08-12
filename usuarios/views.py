from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm


from .forms import ProfileUpdateForm, RegistroForm
from .models import UserProfile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'usuarios/profile_update.html'
    success_url = reverse_lazy('inicio:index')

    def get_object(self, queryset=None):
        # Obtén el perfil del usuario asociado
        return self.request.user.userprofile

class CustomLogoutView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('inicio:index')  # Cambia esto por la URL a la que quieras redirigir después del logout

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    next_page = 'inicio:index'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('inicio:index')

@login_required
def actualizar_perfil(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('inicio:index')
    else:
        form = ProfileUpdateForm(instance=request.user.userprofile)
    return render(request, 'usuarios/profile_update.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio:index')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})
