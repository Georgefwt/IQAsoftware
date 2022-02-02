"""
WSGI config for IQAsoftware project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling,MediaCling
from static_ranges import Ranges

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IQAsoftware.settings')

# application = get_wsgi_application()
application = Ranges(Cling(MediaCling(get_wsgi_application())))