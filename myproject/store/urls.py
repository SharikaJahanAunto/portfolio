from django.urls import path
from . views import index, about, resume, service, service_details

urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('resume/',resume, name='resume'),
    path('services/',service, name='service'),
    path('service-details/<int:pk>',service_details, name='service_details'),
]
