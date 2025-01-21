from django.db import models

# Create your models here.

class Buyer(models.Model):

    login = models.CharField(max_length=90)
    password = models.CharField(max_length=30)
    second_password = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    phone = models.IntegerField()

    flag_zakaz = models.BooleanField(default='False')
    flag_sdelano = models.BooleanField(default='False')

