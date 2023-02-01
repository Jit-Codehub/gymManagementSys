from django.shortcuts import render
from .models import *

def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3]
    return render(request, "main/home.html",{"banners":banners,"services":services})
