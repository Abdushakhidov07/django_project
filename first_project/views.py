from django.shortcuts import render
from django.http import HttpResponse



def say_hello(request):
    name = request.GET.get('name', 'Guest')
    return HttpResponse(f"<h1 style=color:blue >Hello world {name}</h1>")




def get_name(request, name):
    return HttpResponse(f"<h1 style=color:blue >Hello world {name}</h1>")