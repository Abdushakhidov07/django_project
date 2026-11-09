from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')