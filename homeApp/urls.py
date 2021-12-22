from django.urls import path
from django.conf.urls import include
from homeApp import views


app_name = 'homeApp'

urlpatterns = [
    path('', views.home, name='home'),

]