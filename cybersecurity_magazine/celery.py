import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybersecurity_magazine.settings')
app = Celery('cybersecurity_magazine')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()