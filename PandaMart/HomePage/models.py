from django.db import models

# Create your models here.

class ProductInfo(models.Model):

    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    view = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    
