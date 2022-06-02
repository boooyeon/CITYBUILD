from django.urls import path

from Accountsapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_accounts, name='login'),
    path('logout/', views.logout_accounts, name='logout'),
]
