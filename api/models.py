from django.db import models


# Create your models here.
class Company(models.Model):
    companyName = models.CharField(max_length=255)


class Laptop(models.Model):
    companyName = models.CharField(max_length=255, default='')
    laptopName = models.CharField(max_length=255, default='NA')
    cpu = models.CharField(max_length=255, default='NA')
    storage = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
