

# EmailSender  (Django-Celery project)


### Used  Technogies   
- Django 
- celery
- TailwindCss 
- django-allauth (for social authentication)


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


### django-allauth setup
we are using django-allauth for social authentication (like login with google,github etc .)
> pip install "django-allauth[socialaccount]"     




Now start your server, visit your admin pages (e.g. http://localhost:8000/admin/) and follow these steps:
- For each OAuth based provider, either add a SocialApp (socialaccount app) containing the required client credentials, or, make sure that these are configured via the SOCIALACCOUNT_PROVIDERS[<provider>]['APP'] in  settings.

- in settings.py add this configuration
```python
INSTALLED_APPS = [
    ...
    # django-allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', # provider 
]
```
add allauth account middleware to settings middleware    

```python 
MIDDLEWARE=[
    ...
    # account middleware
    "allauth.account.middleware.AccountMiddleware",
]
```

```python 
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
      'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
    },
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```


visit  [django-allauth-docs](https://docs.allauth.org/en/latest/installation/quickstart.html) for more details



