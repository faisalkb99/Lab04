from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

     path('', views.home, name='home'),
    path('calculate_tax/', views.calculate_tax, name='calculate_tax'),
    path('taxrate/', views.show_tax_rate, name='show_tax_rate'),
]
