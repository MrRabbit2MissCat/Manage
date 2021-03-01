from django.db import models

# Create your models here.
from django.forms import forms


class Seedtable(models.Model):
    name = models.CharField(max_length=20)
    xingtai = models.CharField(max_length=15)
    level = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    number = models.IntegerField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    cost = models.FloatField()
    time = models.DateField()
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'seedtable'
        ordering=['name']
class Waretable(models.Model):
    name = models.CharField(max_length=20)
    xingtai = models.CharField(max_length=15)
    level = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    number = models.IntegerField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    cost = models.FloatField()
    time = models.DateField()
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'waretable'


