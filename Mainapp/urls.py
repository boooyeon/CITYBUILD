from django.urls import path
import Mainapp.views

urlpatterns = [
    path('road/', Mainapp.views.main, name='road'),
    path('mypage/', Mainapp.views.mypage, name='mypage'),
    path('report/', Mainapp.views.reports_create, name='report'),
    path('getApi/', Mainapp.views.getApi, name='getApi'),
    path('getSearchApi/', Mainapp.views.getSearchApi, name='getSearchApi'),
]