from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render


tax_rate = 0.15

def home(request):
    return render(request, 'views/home.html')

def calculate_tax(request, number):
    total_price = number + (number * tax_rate)
    context = {'total_price': total_price}
    return render(request, 'views/calculate_tax.html', context)

def show_tax_rate(request):
    context = {'tax_rate': tax_rate * 100}  # Convert to percentage
    return render(request, 'views/tax_rate.html', context)


    

# Create your views here.
