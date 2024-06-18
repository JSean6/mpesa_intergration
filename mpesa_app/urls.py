from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'), 
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
]