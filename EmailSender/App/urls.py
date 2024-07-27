
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    # path('accounts/google/login/',views.direct_google_login,name='google_login'),
    # path('accounts/google/login/',views.custom_google_login,name='google_login'),

]
