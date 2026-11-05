from django.urls import path
from .views import *


urlpatterns = [
    path('hello/',  say_hello),
    path('get_name/<str:name>',  get_name)
]
