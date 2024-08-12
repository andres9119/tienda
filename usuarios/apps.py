from django.apps import AppConfig


"""class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'"""


class UsuariosConfig(AppConfig):
    name = 'usuarios'

    def ready(self):
        import usuarios.signals  # Asegúrate de que el archivo signals.py existe y contiene las señales.






    
