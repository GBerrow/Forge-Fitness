import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the FORGE-FITNESS directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the default settings module for the 'django' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forge_fitness.settings')

# Get the WSGI application
application = get_wsgi_application()

# Optional: Add logging for easier debugging in production
import logging

logger = logging.getLogger('django')
logger.info("WSGI application initialized for Forge Fitness")
