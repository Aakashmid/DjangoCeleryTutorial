from celery import shared_task
from django.core.mail import send_mail
import time


@shared_task
def add(x, y):
    time.sleep(5)  # Simulate a time-consuming task
    return x + y


# task for sending email
@shared_task
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'noreply@myapp.com',
        recipient_list,
        fail_silently=False,
    )
