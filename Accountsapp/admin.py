from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

# # Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user_id', 'username', 'email', 'phone', 'user_type']
#     list_display_links = ['id', 'user_id']


# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)