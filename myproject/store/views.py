from django.shortcuts import render
from .models import About


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    about = About.objects.get()
    return render(request,'about.html',{'about':about})

def resume(request):
    return render(request,'resume.html')