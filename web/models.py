# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cat= models.CharField(max_length=50)
    sub_cat=models.CharField(max_length=50)

# Create your models here.
class User (User):

    # username=models.CharField(max_length=50 , primary_key=True)
    phone_number = models.CharField(max_length=15)
    # password = models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    # email=models.EmailField(max_length=100)
    rank = models.IntegerField()
    invite_code = models.CharField(max_length=30)
    # token=m
    # list_reguest=




class Book(models.Model):
    name=models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    interpreter=models.CharField(max_length=50)
    book_price = models.DecimalField(max_digits=10 , decimal_places=0)#find better field
    edition = models.IntegerField()
    Publication_date=models.DateField()
    picture= models.ImageField()#TODO width and height determine
    category = models.OneToOneField(Category)


class Post(models.Model):
    STATE=(
        ("sale" ,"sale"),
        ("hire" , "hire")
           )

    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    sales_price = models.DecimalField(max_digits=10 , decimal_places=0)#find better field
    state = models.CharField(max_length=10 , choices=STATE)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    location = models.CharField(max_length=60 )#find beter location
    date = models.DateTimeField()
    special = models.BooleanField()#ToDO better field





class Anouncment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    writer = models.CharField(max_length=100 , null=True)
    book_name = models.CharField(max_length=100 , null=True)
    category = models.OneToOneField(Category)




# class manager():#TODO manager


