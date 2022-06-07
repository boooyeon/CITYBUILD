from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Lane
from django.db.models import Q


def getApi(request):
    lanes = Lane.objects.all()
    lane_list = serializers.serialize('json', lanes)
    return HttpResponse(lane_list, content_type=u"application/json; charset=utf-8")


def getSearchApi(request):
    lanes = Lane.objects.all()
    keyword = request.POST.get('keyword',"")
    print(keyword)

    if keyword:
        lane_search = lanes = lanes.filter(
            Q(road_address__icontains = keyword)
        )
    
        search_list = serializers.serialize('json', lane_search)
        print(search_list)
        return HttpResponse(search_list, content_type=u"application/json; charset=utf-8")
    else:
        return render(request, 'Mainapp/main.html')

def main(request):
    return render(request, 'Mainapp/main.html')

def mypage(request):
    return render(request, 'Mainapp/mypage.html')