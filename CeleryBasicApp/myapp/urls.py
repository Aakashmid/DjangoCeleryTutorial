from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home),
    path('result/<str:task_id>', views.result,name='check_result'),
]
