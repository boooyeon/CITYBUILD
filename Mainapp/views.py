from tabnanny import check
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Accountsapp.models import User
from .models import Lane, Report, Scrap
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
    user = request.user.id

    user_scraps = Scrap.objects.filter(user_id=user)
    print(user_scraps)
    return render(request, 'Mainapp/mypage.html', {'user_scraps':user_scraps})

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

def scrap(request):
    if request.method == 'POST':
        pk = int(request.POST.get('pk',""))
        part = request.POST.get('part',"")

        lane = Lane.objects.get(id=pk)
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if part == "1":
            try:
                # 객체가 있다면
                Scrap.objects.get(lane_id=lane, user_id=user)
                return JsonResponse({'status':'yes'})
            
            except:
                # 객체가 없다면
                return JsonResponse({'status':'no'})
        
        else:
            try:
                scrap = Scrap.objects.get(lane_id=lane, user_id=user)
                scrap.delete()
                return JsonResponse({'status':'delete', 'pk':pk})
            
            except:
                scrap = Scrap.objects.create(lane_id=lane, user_id=user)
                scrap.save()
                return JsonResponse({'status':'create', 'pk':pk})
            

        

        