from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

# models.py

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)  
    
    def __str__(self):
        return f"Carrito de {self.usuario} ({'Activo' if self.activo else 'Inactivo'})"

    def total(self):
        total = sum(item.subtotal() for item in self.items.all())
        return total

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    agregado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def subtotal(self):
        return self.cantidad * self.producto.precio


