from django.shortcuts import render
from .models import Lane, Address
# Create your views here.
def main(request):
    lanes = Lane.objects.all()
    address = Address.objects.all()
    context = {
        'lanes' : lanes,
        'address' : address,
    }
    return render(request, 'Mainapp/main.html', context)

def mypage(request):
    return render(request, 'Mainapp/mypage.html')