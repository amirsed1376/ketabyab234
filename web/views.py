# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import *


from .models import *
from json import JSONEncoder
from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    # return render()
    # print("helloooooooo")
    elif request.method == 'POST':
        if request.POST.has_key('username') and request.POST.has_key('password'):
            username = request.POST['username']
            password = request.POST['password']
            this_user = get_object_or_404(User, username=username)
            hash_password=
            if password == this_user.password:#TODO check if (check_password(password, this_user.password)):  # authentication
            # if (check_password(password, this_user.password)):  # authentication
            #     this_token = get_object_or_404(Token, user=this_user)
            #     token = this_token.token
                context = {}
                context['result'] = 'ok'
                # context['token'] = token
                # return {'status':'ok','token':'TOKEN'}
                return JsonResponse(context, encoder=JSONEncoder)
            else:
                context = {}
                context['result'] = 'error'
                # return {'status':'error'}
                # return JsonResponse(context, encoder=JSONEncoder)



@csrf_exempt
def sign_up(request):
    if request.method =='GET':
        return render(request, "ketabyab_sign.html")


    elif request.method == 'POST':
        context = {}

        #TODO check validator
        if request.POST.has_key("username") and request.POST.has_key("password") and request.POST.has_key("email") and request.POST.has_key("phone_number") and request.POST.has_key("city")\
         and request.POST.has_key("confirm_password"):
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            city= request.POST['city']
            confirm_password=request.POST.has_key
            phone_number = request.POST['phone_number']
            if User.objects.filter(username=username).exists():
                context['result']="username is already exist"#ToDO render sign upo page
            else:
                if password == confirm_password:
                    this_user = User.objects.create(username=username , password=password , email = email , city=city , phone_number=phone_number ,
                                            rank=0, invite_code=username)
                else :
                    context={"confirm password != password"}#TODO render signup
            # User.objects.save(this_user)
                context['result'] = 'sign up ok'#TODO go to main page
        return JsonResponse(context, encoder=JSONEncoder)




