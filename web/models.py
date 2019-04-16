# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


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
    category_obj = Category()
    name=models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    interpreter=models.CharField(max_length=50 , null=True)
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
    book_obj = Book()
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    sales_price = models.DecimalField(max_digits=10 , decimal_places=0)#find better field
    state = models.CharField(max_length=10 , choices=STATE ,)
    owner = models.ForeignKey(User , on_delete=models.CASCADE ,)
    location = models.CharField(max_length=60 )#find beter location
    put_date = models.DateTimeField(default=datetime.now())
    special = models.BooleanField(default=False)#ToDO better field


    def post_information(self):
        print(self.book.fname)
        export={}
        export["name"]=self.book_obj.name
        export['writer'] = self.book_obj.writer
        if self.book_obj.interpreter is not None :
            export['interpreter'] = self.book_obj.interpreter
        export['book_price'] = self.book_obj.book_price
        export['edition'] = self.book_obj.edition
        export['Publication_date'] = self.book_obj.Publication_date
        export['picture'] = self.book_obj.picture
        export['Publication_date'] = self.book_obj.Publication_date
        export['category'] = self.book_obj.category_obj.cat
        export['sub_category'] = self.book_obj.category_obj.sub_cat
        export['sales_price'] = self.sales_price
        export['state'] = self.state
        export['owner'] = self.owner
        export['location'] = self.location
        export['put_date'] = self.put_date
        export['special'] = self.special
        return export







class Anouncment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    writer = models.CharField(max_length=100 , null=True)
    book_name = models.CharField(max_length=100 , null=True)
    category = models.OneToOneField(Category)




# class manager():#TODO manager


