from celery import shared_task
from time import sleep


@shared_task
def sub(x, y):
    return x - y


@shared_task
def schedule_task(id):
    # logic for deleteing session cache w
    print(id)
    return id


@shared_task
def clear_redis_cache(key):
    print(key)
    return key
