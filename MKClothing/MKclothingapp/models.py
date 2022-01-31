from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.forms import EmailField

# Create your models here.
class Products(models.Model):
    itemname = models.CharField(max_length=20)
    price = models.IntegerField()
    stocks = models.IntegerField()
    filename = models.ImageField(null=True, blank=True)

class History(models.Model):
    name = models.CharField(max_length=20)
    pname = models.CharField(max_length=20)
    quan = models.IntegerField()
    total = models.IntegerField()
    email = models.EmailField(max_length=100,null=True)
    address = models.CharField(max_length=100)

class orderc(models.Model):
    cancel = models.IntegerField(default=0)
    success = models.IntegerField(default=0)
    
