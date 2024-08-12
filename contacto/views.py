


# contacto/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import MensajeContacto

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            MensajeContacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contacto:contacto')  # Redirige usando el nombre de la aplicación
        else:
            messages.error(request, 'Ocurrió un error al enviar tu mensaje. Por favor, inténtalo de nuevo.')
    else:
        form = ContactForm()

    return render(request, 'contacto/contacto.html', {'form': form})
