from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .tasks import SendMail
from celery.result import AsyncResult
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Authenticated related views
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialApp
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
# Create your views here.



def send_test_email():
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['aakash.23pcs5102@']  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list)
    print('Email is sent',from_email,settings.EMAIL_HOST_PASSWORD)


# @login_required  #   it redirect to login url if user is unauthenticated
def index(request):
    if request.method=='POST':
        subject=request.POST.get('subject')        
        message=request.POST.get('message')        
        toEmail=request.POST.get('receiver')
        fromEmail=settings.EMAIL_HOST_USER
        # fromEmail=request.user.email
        # mailTask=SendMail.delay(subject,message,toEmail,fromEmail)
        # mailTaskStatus=AsyncResult(mailTask.id)
        # if mailTaskStatus.successful():
        #     messages.success(request,'mail is sent successfuly ')
        # else:
        #     messages.error(request,'Sending mail .. ')

        send_mail(
        subject=subject,
        message=message,
        from_email=fromEmail,
        recipient_list=[toEmail,],
        fail_silently=False,
    )
        return HttpResponseRedirect('/')
    

    # send_test_email()
    return render(request,'App/index.html')





def custom_google_login(request):
    app = SocialApp.objects.get(provider='google')
    client_id = app.client_id
    redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    scope = 'email profile'

    state = get_random_string(32)
    request.session['oauth_state'] = state
    auth_url = (
        f'https://accounts.google.com/o/oauth2/v2/auth'
        f'?client_id={client_id}'
        f'&redirect_uri={redirect_uri}'
        f'&scope={scope}'
        f'&response_type=code'
        f'&access_type=offline'
        f'&state={state}'
    )

    return redirect(auth_url)

    auth_url ='https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=493298721583-obu3h9p2s3tkmouieumu2c0uk2vcoh8t.apps.googleusercontent.com&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Faccounts%2Fgoogle%2Flogin%2Fcallback%2F&scope=email%20profile&responsPe_type=code&state=lEyE2PFMrgyhuBRN9&access_type=offline&service=lso&o2v=2&ddm=0&flowName=GeneralOAuthFlow'

    return redirect(auth_url)


def custom_logout(request):
    logout(request)
    return redirect('/')

