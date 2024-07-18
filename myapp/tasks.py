from celery import shared_task 
from time import sleep

@shared_task
def sub(x,y):
    return x-y