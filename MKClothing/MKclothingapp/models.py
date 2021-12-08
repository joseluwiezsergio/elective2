from django.db import models

# Create your models here.
class Products(models.Model):
    itemname = models.CharField(max_length=20)
    price = models.IntegerField()
    stocks = models.IntegerField()
    filename = models.ImageField(null=True, blank=True)