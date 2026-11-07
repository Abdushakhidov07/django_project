from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('show_products', get_products, name='show_products'),
    path('add_product', add_products, name='add_product'),

]
