from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *





def home_page(request):
    context = { 
        'name': 'Abdullo',
        'age': 20,
        }
    return render(request, 'index.html', context)




def get_products(request):
    products = Products.objects.all()
    return render(request, 'profile.html', {"products": products})




def add_products(request):
    if request.method == "POST":
        Products.objects.create(
            name = request.POST["name"],
            price = request.POST["price"],
            stock = request.POST["count"]
        )
        return redirect('show_products')
    
    return render(request, "add_products.html")
        
    
        
