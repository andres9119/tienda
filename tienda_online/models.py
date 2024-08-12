from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='productos/', default='productos/default.jpg')

    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f'Pedido {self.id} - {self.estado}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Experiencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    experiencia = models.TextField()
    fecha_compartida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Experiencia de {self.usuario.nombre}'

class Autorizacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    permisos = models.TextField()

    def __str__(self):
        return f'Autorización de {self.usuario.nombre}'

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f'Inventario de {self.producto.nombre}'

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago de {self.monto} para el pedido {self.pedido.id}'
