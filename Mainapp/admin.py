from ast import Add
from django.contrib import admin
from .models import Lane, Report, Scrap

admin.site.register(Lane)

admin.site.register(Report)

admin.site.register(Scrap)