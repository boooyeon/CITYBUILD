from django.shortcuts import render, redirect
from .models import User


def signup(request):
    
    return render(request, 'signup.html')

