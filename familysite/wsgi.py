import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project directory to the path (important for Vercel)
path = os.path.expanduser('/var/task')
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'familysite.settings')

application = get_wsgi_application()
