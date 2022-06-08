from tabnanny import check
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Lane, Report
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

def reports_create(request):
    if request.method == 'POST':
        pk = int(request.POST.get('lane_id',""))
        lane = Lane.objects.get(id=pk)
        
        content = request.POST.get('content')
        report_img = request.POST.get('report_img')
        print(lane, content, report_img)

        report = Report.objects.create(lane_id=lane, content=content, report_images=report_img)
        report.save()
        
        return render(request, 'Mainapp/main.html')

    else: 
        return render(request, 'Mainapp/main.html')
