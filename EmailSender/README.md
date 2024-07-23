

# EmailSender  (Django-Celery project)





###  **celery**   setup 
install celery , for using redis as a broker url
> pip install celery[redis]


visit [celery with django](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)  for more detail


#### for  runnig celery worker in `windows`
first install
> pip install gevent  
  
and then run 
> celery -A project_name worker -l info -P gevent

Use celery beat to run periodic just run another server of beat  
- `celery -A YourProjectName beat --loglevel=info`

### for using djang-db as result backend    
1 . install django-celery-results 
> pip install django-celery-results    

2 . Add django_celery_results to INSTALLED_APPS in your Django project’s settings.py:  

``` python
INSTALLED_APPS = (
    ...,
    'django_celery_results',
)
```

3 . Create the Celery database tables by performing a database migrations:

> python manage.py migrate django_celery_results

4 . add following setting to settings.py  

``` python
CELERY_RESULT_BACKEND = 'django-db'
```