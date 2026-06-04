from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.models import User

        username = "admin"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@adsys.com",
                password="Admin123456!"
            )