from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialApp


# Create your views here.

# @login_required  #   it redirect to login url if user is unauthenticated
def index(request):
    return render(request,'App/index.html')


# Authenticated related views
from django.shortcuts import redirect
import urllib.parse

# def custom_google_login(request):
#     # Construct the Google OAuth2 authorization URL manually
#     base_url = "https://accounts.google.com/o/oauth2/v2/auth"
#     params = {
#         'response_type': 'code',
#         'client_id': SocialApp.client_id,
#         'redirect_uri': request.build_absolute_uri('/accounts/google/login/callback/'),
#         'scope': 'profile email',
#         'response_type':'code',
#         "state": "2dq7rIOnrtfnA8Eg",
#         'access_type': 'offline',
#     }
#     auth_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    
#     return redirect(auth_url)
# def direct_google_login(request):
#     app=SocialApp.objects.get(provider='google')
#     callback_url=request.build_absolute_uri('/accounts/google/login/callback/')
#     access_token_url='https://oauth2.googleapis.com/token'
#     client=OAuth2Client(request,app.client_id,app.secret,app.key,access_token_url=access_token_url,callback_url=callback_url)
#     adapter=GoogleOAuth2Adapter(request)
#     provider=adapter.get_provider()
#     authorize_url=provider.get_authorize_url(request,callback_url,client)
#     return redirect(authorize_url)




