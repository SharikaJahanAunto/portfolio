from django.urls import path
from . views import *

urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('resume/',resume, name='resume'),
    path('services/',service, name='service'),
    path('contact/',contact, name='contact'),
    path('service-details/<int:pk>',service_details, name='service_details'),
    
]
