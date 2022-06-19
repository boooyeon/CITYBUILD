from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from Accountsapp.models import User
from django.db.models import Q
from .models import Lane, Report, Scrap
from .geocoding import lat2tile, lon2tile
from PIL import Image
from datetime import datetime

import os
import pandas as pd
import numpy as np
import urllib
import csv



def getApi(request):
    lanes = Lane.objects.all()
    lane_list = serializers.serialize("json", lanes)
    return HttpResponse(lane_list, content_type="application/json; charset=utf-8")


def getSearchApi(request):
    lanes = Lane.objects.all()
    keyword = request.POST.get("keyword", "")

    if keyword:
        lane_search = lanes.filter(Q(road_address__icontains=keyword))
        search_list = serializers.serialize("json", lane_search)
        return HttpResponse(search_list, content_type="application/json; charset=utf-8")
    else:
        return render(request, "Mainapp/main.html")


def main(request):
    return render(request, "Mainapp/main.html")


def scrap_download(request):
    cols = ["lat", "lon", "address"]
    info = pd.DataFrame(columns=cols)

    user = request.user.id
    user_scraps = Scrap.objects.filter(user_id=user)

    for scraps in user_scraps:
        lane = scraps.lane_id

        ret = pd.DataFrame(
            [(lane.latitude, lane.longitude, lane.road_address)],
            columns=cols,
        )

        info = pd.concat(
            [info, ret],
            ignore_index=True,
        )

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={datetime.now()}.csv"

    info.to_csv(path_or_buf=response, sep=",", index=True)
    return response


def mypage(request):
    user = request.user.id
    user_scraps = Scrap.objects.filter(user_id=user)

    return render(request, "Mainapp/mypage.html", {"user_scraps": user_scraps})


def reports_create(request):
    if request.method == "POST":
        pk = int(request.POST.get("lane_id", ""))
        lane = Lane.objects.get(id=pk)

        content = request.POST.get("content")
        report_img = request.POST.get("report_img")
        print(lane, content, report_img)

        report = Report.objects.create(
            lane_id=lane, content=content, report_images=report_img
        )
        report.save()

        return render(request, "Mainapp/main.html")

    else:
        return render(request, "Mainapp/main.html")


def scrap(request):
    if request.method == "POST":
        pk = int(request.POST.get("pk", ""))
        part = request.POST.get("part", "")

        lane = Lane.objects.get(id=pk)

        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if part == "1":
            try:
                # 객체가 있다면
                Scrap.objects.get(lane_id=lane, user_id=user)
                return JsonResponse({"status": "yes"})

            except:
                # 객체가 없다면
                return JsonResponse({"status": "no"})

        else:
            try:
                scrap = Scrap.objects.get(lane_id=lane, user_id=user)
                scrap.delete()
                return JsonResponse({"status": "delete", "pk": pk})

            except:
                scrap = Scrap.objects.create(lane_id=lane, user_id=user)
                scrap.save()
                return JsonResponse({"status": "create", "pk": pk})


def add_db(request):
    base_dir = os.getcwd()
    file_dir = os.path.join(base_dir, "csv/")
    csv_list = os.listdir(file_dir)

    if len(csv_list) > 0:
        for file in csv_list:
            file = file_dir + f"{file}"
            if os.path.isfile(file):
                df = pd.read_csv(file, index_col=False)

                for idx in range(len(df)):
                    lat = df.loc[idx]["pred_lat"]
                    lon = df.loc[idx]["pred_lon"]
                    address = df.loc[idx]["address"]

                    lane = Lane.objects.create(
                        latitude=lat, longitude=lon, damage=2, road_address=address
                    )
                    lane.save()

                # db에 반영했으면 삭제
                os.remove(file)

    return redirect("home")


def img_load(request, lat, lon):
    x_tile = lon2tile(float(lon))
    y_tile = lat2tile(float(lat))

    url = f"https://skymaps.co.kr/map/wmts/wmts2020/19/{x_tile}/{y_tile}?api_key=66dd0019-905a-4d66-a0b7-eed7c418dbf0"
    img = urllib.request.urlopen(url).read()

    if len(img) == 0:
        with open("ready.jpg", "rb") as f:
            img = f.read()

    return HttpResponse(img, content_type="image/jpg")
