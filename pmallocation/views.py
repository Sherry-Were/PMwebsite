from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'pmallocation/child/home.html')

def login(request):
    return render(request, 'user/login.html')

def photos(request):
    return render(request, 'pmallocation/child/photos.html')

def register(request):
    return render(request, 'pmallocation/child/register.html')

def logout(request):
    return render(request, 'pmallocation/child/logout.html')


def detail(request, person_id):
    return HttpResponse('<h3>Details for person id:' +str(person_id)+'</h3>')
