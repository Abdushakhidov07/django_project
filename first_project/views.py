from django.shortcuts import render
from django.http import HttpResponse





def home_page(request):
    context = { 
        'name': 'Abdullo',
        'age': 20,
        }
    return render(request, 'index.html', context)




def profile_page(request):
    context = { 
    'username':'Abdullopromax',
    'model': 'X6',
    'RAM': "16"
        }
    return render(request, 'profile.html', context)


