from django.urls import path
import Mainapp.views

urlpatterns = [
    path('road/', Mainapp.views.main, name='main'),
]