"""
WSGI config for django_default project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


server = os.getenv('dds','DEV')
settings = "django_default.settings_dev"

if server == 'STAGE':
    settings = "django_default.settings_stage" 
elif server == 'PROD':
    settings = "django_default.settings_prod"
      
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
