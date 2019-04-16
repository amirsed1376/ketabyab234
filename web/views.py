# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


from .models import *
from json import JSONEncoder
from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render

# Create your views here.
@csrf_exempt
def login(request):
    # return render()
    # print("helloooooooo")
    if request.POST.has_key('username') and request.POST.has_key('password'):
        username = request.POST['username']
        password = request.POST['password']
        this_user = get_object_or_404(User, username=username)
        print("user=",username , "           password=",password)
        print("this user =" ,this_user.password)
        if password == this_user.password:#TODO check if (check_password(password, this_user.password)):  # authentication
        # if (check_password(password, this_user.password)):  # authentication
            # this_token = get_object_or_404(Token, user=this_user)
            # token = this_token.token
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
def asli(request):
    return  render(request ,"login.html")
