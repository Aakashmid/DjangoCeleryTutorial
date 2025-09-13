## Running Celery Worker

- celery -A your_project_name worker --loglevel=info
- (example) celery -A celeryproject worker --loglevel=info  


## Windows Support for Celery 4.0+

Windows does not support Celery 4.0+ directly. To solve this issue, follow these steps:

1. Install gevent using pip:

`pip install gevent`


2. Run celery with gevent pool:

`celery -A <proj_name> worker -l info -P gevent`


## Using Django Database as Result Backend

1. Install django-celery-results:

`pip install django-celery-results`


2. Add to INSTALLED_APPS in settings.py:
```python
INSTALLED_APPS = (
    ...,
    'django_celery_results',
)
```

3. Migrate database:

`python manage.py migrate django_celery_results`


4. Add to settings.py:

```python
CELERY_RESULT_BACKEND = 'django-db'
```


## Running Periodic Tasks

### Method 1: Using settings.py

```python
CELERY_BEAT_SCHEDULE = {
    'clearCache': {  # task name 
        'task': 'myapp.tasks.schedule_task',  
        'schedule': 10,  # run every 10 seconds 
        'args': (12121,)
    },
    # add more periodic tasks
}
```

### Method 2: Using celery.py

```python
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'schedule_task1': {
        'task': 'myapp.tasks.schedule_task',
        'schedule': timedelta(seconds=10),   # run every 10 seconds
        # 'schedule': crontab(hour=7, minute=30, day_of_week=1),   # run at monday 7:30
        'args': (23,)
    },
}
```


### Run celery beat server:

`celery -A celeryproject beat -l info`


## Useful Documentation
- [Celery User Guide](https://docs.celeryq.dev/en/stable/userguide/index.html#guide)
- [Celery Periodic Tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#beat-custom-schedulers)

## Using django-celery-beat Package

1. Install the package:

`pip install django-celery-beat`


2. Add to INSTALLED_APPS:

```python
INSTALLED_APPS = (
    ...,
    'django_celery_beat',
)
```

3. Migrate database:

`python manage.py migrate`


4. Configure scheduler in settings.py:

```python
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
```


## Monitoring Tasks with Flower

install flower using -  `pip install flower`

Flower is a real-time monitoring tool for Celery.

1. Start Flower:

`celery -A realtime_chat flower`

2. Open the Flower dashboard at http://localhost:5555 to view:
- Active tasks
- Task history
- Worker status


Note: You can also implement scheduling without the admin site through manual coding.
