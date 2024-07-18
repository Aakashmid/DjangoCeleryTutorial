from django.shortcuts import render
from celeryproject.celery import add
from celery.result import AsyncResult
from .tasks import sub
from time import sleep
# Create your views here.


# Enqueue task using delay()
# def home(request):
#     result= add.delay(18,12)  # it enqueue task (send task for execution )
#     print('result1 :',result)

#     result=sub.delay(30,10)
#     print('result2 :',result)
#     return render(request,'index.html')

# ---------------------------------------

# using apply_async 
# def home(request):
#     result= add.apply_async(args=[18,12])  # it enqueue task (send task for execution )
#     print('result1 :',result)
#     return render(request,'index.html')


# ---------------------------------------

def home(request):
    result=add.delay(10,20)
    return  render(request,'index.html',{'result':result})

def result(request,task_id):
    # retriveing task result by its id 
    result= AsyncResult(task_id)
    return  render(request,'result.html',{'result':result})
    


