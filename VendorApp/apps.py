from django.apps import AppConfig


class VendorappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VendorApp'

    def ready(self):
        import VendorApp.signals
