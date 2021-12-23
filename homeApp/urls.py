from django.urls import path
from django.conf.urls import include
from homeApp.views import HomeView


app_name = 'homeApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]