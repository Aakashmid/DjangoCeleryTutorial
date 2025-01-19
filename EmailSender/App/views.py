from django.shortcuts import render, HttpResponse
from app.tasks import add, send_email


# Create your views here.
def home(request):
    # Trigger the task asynchronously
    add.delay(10, 20)

    send_email.delay('Welcome to MyApp', 'Thank you for signing up!', ['noreply@example.com'])
    return HttpResponse("Hello, World!")
    # return render(request, 'home.html')
