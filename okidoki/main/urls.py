from django.urls import path
from .views import *
from django.conf.urls import include


urlpatterns = [
    path('', index, name = 'home'),
    path('delivery', delivery, name='delivery'),
    path('pay', pay, name='pay'),
    path('contacts', contacts, name='contacts')
    
]