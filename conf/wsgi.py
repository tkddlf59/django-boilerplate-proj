"""
WSGI config for django_boilerplate_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DJANGO_SETTINGS_MODULE_PATH = os.environ.get(
    "DJANGO_SETTINGS_MODULE",
    "conf.settings.local"
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE_PATH)
application = get_wsgi_application()
