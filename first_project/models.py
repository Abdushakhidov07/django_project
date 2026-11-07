from django.db import models

# Create your models here.

class Products(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=100)
    stock =  models.PositiveIntegerField()