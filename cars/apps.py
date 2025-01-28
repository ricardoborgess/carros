from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self): # Função pra quando iniciar a aplicação
        import cars.signals  # Carrega o signals quando iniciar a aplicação