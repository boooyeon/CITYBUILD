from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import AuthenticationForm, UserCreationForm

LOGIN_URL = '/accounts/login'


@csrf_exempt
def signup(request):
    if request.user.is_authenticated:
        return redirect('main')
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context['form'] = form

    return render(request, 'Accountsapp/signup.html', context)


@csrf_exempt
def login_accounts(request):
    if request.user.is_authenticated:
        return redirect('road')

    context = {}

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user_id = request.POST['user_id']
            password = request.POST['password']
            user = authenticate(user_id=user_id, password=password)
            if user:
                login(request, user)
                return redirect('road')
        else:
            context['form'] = form

    return render(request, 'Accountsapp/signin.html', context)


@login_required(login_url=LOGIN_URL)
def logout_accounts(request):
    logout(request)
    return redirect('home')
