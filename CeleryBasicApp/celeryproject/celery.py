import os
from time import sleep
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(name="addition_task")   # naming task 
def add(x,y):
    sleep(10)
    return x+y



# Methode 2 for schedule tasks 

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'schedule_task1': {
        'task': 'myapp.tasks.schedule_task',
        'schedule': timedelta(seconds=10),   # run in every 10 seconds
        # 'schedule': crontab(hour=7, minute=30, day_of_week=1),   # run at monday 7:30
        'args': (23,)
    },
}


# app.conf.beat_schedule = {
#     # Executes every Monday morning at 7:30 a.m.
#     'add-every-monday-morning': {
#         'task': 'tasks.add',
#         'schedule': crontab(hour=7, minute=30, day_of_week=1),   # run at monday 7:30
#         'args': (16, 16),
#     },
# }