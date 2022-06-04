from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'Mainapp/main.html')

def mypage(request):
    return render(request, 'Mainapp/mypage.html')