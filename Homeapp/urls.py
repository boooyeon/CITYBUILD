from django.contrib import admin
from django.urls import path
import Homeapp.views

urlpatterns = [
    path('', Homeapp.views.home, name='home'),
]