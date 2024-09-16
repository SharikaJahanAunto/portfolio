from django.shortcuts import redirect, render
from .models import About, Social, Service
from .forms import *

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

def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


    return render(request,"contact.html",{'form':form})