
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Home'),

    # authentication related urls
    # path('accounts/google/login/', views.custom_google_login, name='google_login'),
    path('accounts/logout/',views.custom_logout),
]
