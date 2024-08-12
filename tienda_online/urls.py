from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('inicio.urls')),        # Incluye las URLs de la aplicación inicio
    path('', include('inicio.urls', namespace='inicio')),
    path('nosotros/', include('nosotros.urls')),  # Incluye las URLs de la aplicación nosotros
    path('contacto/', include('contacto.urls')),  # Incluye las URLs de la aplicación contacto
    
    path('blog/', include('blog.urls')),          # Incluye las URLs de la aplicación blog
    #path('experiencias/', include('experiencia.urls')), # Incluye las URLs de la aplicación experiencias
    #path('inventario/', include('inventario.urls')), # Incluye las URLs de la aplicación inventario
    #path('pagos/', include('pagos.urls')), # Incluye las URLs de la aplicación pagos
    #path('pedidos/', include('pedidos.urls')), # Incluye las URLs de la aplicación pedidos
    
    path('productos/', include('productos.urls', namespace='productos')), # Incluye las URLs de la aplicación productos
    path('usuarios/', include('usuarios.urls')), # Incluye las URLs de la aplicación usuarios
    path('carrito/', include('carrito.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Agrega aquí las rutas de otras aplicaciones de tu proyecto

