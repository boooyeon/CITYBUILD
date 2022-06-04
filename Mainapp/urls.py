from django.urls import path
import Mainapp.views

urlpatterns = [
    path('road/', Mainapp.views.main, name='road'),
    path('mypage/', Mainapp.views.mypage, name='mypage'),
]