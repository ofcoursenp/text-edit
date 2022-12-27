from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('home', views.index,name='home'),
    path('result', views.result,name='result'),
    path('help', views.help,name='help'),
]