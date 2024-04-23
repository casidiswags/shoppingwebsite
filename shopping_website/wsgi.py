# File: shopping_website/wsgi.py

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_website.settings')

application = get_wsgi_application()
