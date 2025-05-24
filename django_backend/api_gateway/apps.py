from django.apps import AppConfig


class ApiGatewayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_gateway'
    def ready(self):
        import api_gateway.signals