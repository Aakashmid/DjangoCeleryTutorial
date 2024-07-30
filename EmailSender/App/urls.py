
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Home'),

    path('accounts/logout/',views.custom_logout),
]
