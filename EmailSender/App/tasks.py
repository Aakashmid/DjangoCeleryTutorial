from celery import shared_task
from django.core.mail import send_mail
@shared_task
def SendMail(subject,message,toEmail,fromEmail):
    print(subject,message,toEmail)
    send_mail(
        subject=subject,
        message=message,
        from_email=fromEmail,
        recipient_list=[toEmail,],
        fail_silently=False,
    )
    return toEmail