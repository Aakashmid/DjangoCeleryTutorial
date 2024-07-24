from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required  #   it redirect to login url if user is unauthenticated
def index(request):
    return render(request,'App/index.html')