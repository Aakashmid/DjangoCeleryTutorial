from django.shortcuts import render
from celeryproject.celery import add
from time import sleep
# Create your views here.


# Enqueue task using delay()
def home(request):
    result= add.delay(18,12)  # it enqueue task (send task for execution )
    print(result)
    return render(request,'index.html')