from django.urls import path
from . views import index, about, resume

urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('resume/',resume, name='resume')
]
