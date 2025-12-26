"""
ASGI config for cedric_admin project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cedric_admin.settings')

application = get_asgi_application()
