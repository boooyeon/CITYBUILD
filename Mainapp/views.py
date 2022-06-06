from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Lane

def getApi(request):
    lanes = Lane.objects.all()
    lane_list = serializers.serialize('json', lanes)
    return HttpResponse(lane_list, content_type=u"application/json; charset=utf-8")

def main(request):
    return render(request, 'Mainapp/main.html')

def mypage(request):
    return render(request, 'Mainapp/mypage.html')