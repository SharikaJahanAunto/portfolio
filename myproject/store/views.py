from django.shortcuts import render
from .models import About, Social, Service


# Create your views here.
def index(request):
    social = Social.objects.all()
    return render(request,'index.html',{'social':social})

def about(request):
    about = About.objects.get()
    return render(request,'about.html',{'about':about})

def resume(request):
    return render(request,'resume.html')

def service(request):
    service= Service.objects.all()
    return render(request,'services.html',{'service':service})

def service_details(request,pk):
    service_details = Service.objects.get(pk=pk)

    return render(request,'service-details.html',{'service_details':service_details}) 