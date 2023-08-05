import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "metasharks.settings")

# Create a Celery app instance.
app = Celery("metasharks")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks in all installed apps
app.autodiscover_tasks()
