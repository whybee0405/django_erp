from django.db import models

# Create your models here.

# Base (non-normalized) Inventory data table
class Inventory(models.Model):
    """Inventory objects that contains descriptions, price and other properties of stock"""
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=30, unique=True)
    category_1 = models.CharField(max_length=100)
    category_2 = models.CharField(max_length=100, blank=True)
    category_3 = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    attribute_1 = models.CharField(max_length=20,default="", blank=True)
    attribute_2 = models.CharField(max_length=20,default="", blank=True)
    attribute_3 = models.CharField(max_length=20,default="", blank=True)
    retail_price = models.FloatField(default=0.00)
    branch_price = models.FloatField(default=0.00)
    cost_price = models.FloatField(default=0.00)
    supplier_name = models.CharField(max_length=20,default="", blank=True)
    backorder_qty = models.IntegerField(default=0)
    stock_available = models.IntegerField(default=0)