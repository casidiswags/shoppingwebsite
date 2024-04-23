# File: app/apps.py

from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Change this if you're using a different field for primary keys
    name = 'app'
    verbose_name = 'My Application'
