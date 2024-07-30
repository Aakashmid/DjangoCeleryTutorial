from celery import shared_task
from django.core.mail import send_mail

@shared_task
def SendMail(subject,message,toEmail):
    print(subject,message,toEmail)
    # send_mail(
    #     "Subject here",
    #     "Here is the message.",
    #     "from@example.com",
    #     ["to@example.com"],
    #     fail_silently=False,
    # )
    return toEmail