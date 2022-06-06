from django.shortcuts import render
from django.core import serializers
from .models import Lane
# Create your views here.
def main(request):
    lanes = Lane.objects.all()
    return render(request, 'Mainapp/main.html', {'lanes':lanes})

def mypage(request):
    return render(request, 'Mainapp/mypage.html')